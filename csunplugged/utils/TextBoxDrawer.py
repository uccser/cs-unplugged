"""Module for TextBoxDrawer class."""

from django.utils.translation import get_language, get_language_bidi
from PIL import ImageFont
from lxml import etree as ET
import tinycss
import os
from bidi.algorithm import get_display
from uniseg.linebreak import line_break_units
import arabic_reshaper

DEFAULT_FONT = "static/fonts/NotoSans-Regular.ttf"
DEFAULT_FONT_OVERRIDES = {
    "ja": "static/fonts/NotoSansCJKjp-Regular.otf",
    "he": "static/fonts/OpenSansHebrew-Regular.ttf",
    "ar": "static/fonts/DejaVuSans.ttf",
}
DEFAULT_FONT_SIZE = 20
DEFAULT_COLOR = (0, 0, 0)

FONT_MAX_ORD = {
    "PatrickHand-Regular": 255,
}


class TextBox(object):
    """Class to store position/dimensions of a text box."""

    def __init__(self, x, y, width, height, color, font_path, font_size):
        """Initialise TextBox."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font_path = font_path
        self.font_size = font_size


class TextBoxDrawer(object):
    """Class to draw text boxes onto an image.

    Text_box layout is defined by elements in an exported SVG.
    """

    def __init__(self, image, draw, svg_path):
        """Initialise TextBoxDrawer.

        Args:
            image: PIL Image object
            draw: PIL ImageDraw object
            svg_path: (str) path to SVG file for text box layout
        """
        self.image = image
        self.draw = draw
        self.svg = self.load_svg(svg_path)
        self.width_ratio, self.height_ratio = self.get_dimension_ratios()

    def load_svg(self, svg_path):
        """Load SVG element tree."""
        return ET.parse(svg_path).getroot()

    def get_dimension_ratios(self):
        """Get ratios between SVG and image coordinate spaces.

        Returns:
            (width_ratio, height_ratio) tuple.
        """
        vbx, vby, vbw, vbh = map(float, self.svg.attrib['viewBox'].split())
        width, height = self.image.size
        width_ratio = width / vbw
        height_ratio = height / vbh
        return width_ratio, height_ratio

    def get_box(self, box_id):
        """Get TextBox object representing the box with the given ID.

        Args:
            box_id: (str) identifier of the textbox, matching the 'id' attribute
                of a rectangle element in the SVG
        Returns:
            TextBox object
        """
        text_layer = self.svg.find('{http://www.w3.org/2000/svg}g[@id="text"]')
        text_elem = text_layer.find('{{http://www.w3.org/2000/svg}}text[@id="{}"]'.format(box_id))
        box_elem = text_elem.getprevious()

        tspan_element = text_elem.find('{http://www.w3.org/2000/svg}tspan')
        if tspan_element is not None:
            # Use style of the first line of text
            style_attrib = tspan_element.attrib['style']
        else:
            # Use style of the only line of text
            style_attrib = text_elem.attrib['style']
        rules, _ = tinycss.make_parser().parse_style_attr(style_attrib)
        style = {}
        for rule in rules:
            style[rule.name] = rule.value[0].value
        color = style.get('fill')
        font = style.get('font-family')
        size = style.get('font-size')
        if size:
            font_size = int(size * self.height_ratio)  # Convert font size into image coord space
        else:
            font_size = None

        return TextBox(
            x=float(box_elem.attrib.get('x', 0)) * self.width_ratio,
            y=float(box_elem.attrib.get('y', 0)) * self.height_ratio,
            width=float(box_elem.attrib['width']) * self.width_ratio,
            height=float(box_elem.attrib['height']) * self.height_ratio,
            color=color,
            font_path="static/fonts/{}.ttf".format(font),
            font_size=font_size
        )

    def write_text_box(self, box_id, string, **kwargs):
        """Write text onto image in the space defined by the given textbox.

        Args:
            box_id: (str) identifier of the textbox, matching the 'id' attribute
                of a rectangle element in the SVG
            string: (str) text to write
        """
        box = self.get_box(box_id)
        self.write_text_box_object(box, string, **kwargs)

    def get_text_width(self, font, text):
        """Get width of given text in given font.

        Args:
            font: PIL.ImageFont object
            text: (str) text to get width of
        """
        return font.getsize(text)[0]

    def get_font_height(self, font):
        """Get height of given font.

        Args:
            font: PIL.ImageFont object
        """
        ascent, descent = font.getmetrics()
        return ascent + descent

    def get_font(self, font_path, font_size):
        """Get ImageFont instance for given font path/size."""
        return ImageFont.truetype(font_path, font_size)

    def get_default_font(self):
        """Get default font for the current language."""
        language = get_language()
        if language in DEFAULT_FONT_OVERRIDES:
            return DEFAULT_FONT_OVERRIDES[language]
        return DEFAULT_FONT

    def write_text_box_object(self, text_box, text, font_path=None,
                              font_size=None, horiz_just='left', vert_just='top',
                              line_spacing=4, color=None):
        """Write text into text_box by modifying line breaks and font size as required.

        Args:
            text_box: TextBox object
            text: (str) text to write
            font_path: (str) path to font .ttf file. This parameter is checked
                first, followed by an attempt to match the font from the SVG,
                and then a fallback language
            font_size: (int) target font size, may be reduced to fit if required.
                This parameter is checked first, falling back to the original
                font size from the SVG
            horiz_just: (str) left, center, right or justify
            vert_just: (str) top, center, bottom
            line_spacing: (int) number of pixels between text lines
            color: (RGB 3-tuple or HEX string) text color. This parameter is
                checked first, falling back to the original color from the SVG
        """
        if get_language() == 'ar':
            text = arabic_reshaper.reshape(text)

        font_path = font_path or text_box.font_path
        if font_path:
            font_name = os.path.splitext(os.path.basename(font_path))[0]
            max_ord_allowed = FONT_MAX_ORD[font_name]
            max_ord = ord(max(text, key=ord))
            if max_ord > max_ord_allowed:
                # Text contains codepoints without a glyph in requested font
                font_path = self.get_default_font()
        else:
            font_path = self.get_default_font()

        font_size = font_size or text_box.font_size or DEFAULT_FONT_SIZE
        color = color or text_box.color or DEFAULT_COLOR

        font_size_is_ok = False
        while not font_size_is_ok:
            font = self.get_font(font_path, font_size)
            lines = []
            line = ""
            breakable_units = line_break_units(text)
            for unit in breakable_units:
                potential_line = line + unit
                size = self.get_text_width(font, potential_line)
                if size >= text_box.width:
                    lines.append(line)
                    line = unit
                else:
                    line += unit

            if line:
                lines.append(line)
            text_width, text_height = self.draw.multiline_textsize(
                '\n'.join(lines),
                font=font,
                spacing=line_spacing)

            # Reduce text_height by offset at top
            (_, _), (_, offset_y) = font.font.getsize(text)
            text_height -= offset_y

            if text_height <= text_box.height:
                font_size_is_ok = True
            else:
                # Decrease font size exponentially, and try again
                font_size = max(int(0.9 * font_size), 1)

        text = '\n'.join(lines)
        if get_language_bidi():
            # Get RTL text
            text = get_display(text)
            # Flip horizontal justification
            if horiz_just == "right":
                horiz_just = "left"
            elif horiz_just == "left":
                horiz_just = "right"

        if vert_just == 'top':
            y = text_box.y
        elif vert_just == 'center':
            y = text_box.y + (text_box.height - text_height)/2
        elif vert_just == 'bottom':
            y = text_box.y + (text_box.height - text_height)

        if horiz_just == 'left':
            x = text_box.x
        elif horiz_just == 'center':
            x = text_box.x + (text_box.width - text_width)/2
        elif horiz_just == 'right':
            x = text_box.x + (text_box.width - text_width)

        # Remove offset from top line, to mimic AI textbox behavior
        y -= offset_y

        self.draw.multiline_text(
            (x, y),
            text,
            fill=color,
            font=font,
            align=horiz_just,
            spacing=line_spacing
        )
