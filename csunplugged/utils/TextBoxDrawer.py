"""Module for TextBoxDrawer class."""

from django.utils.translation import get_language, get_language_bidi
from PIL import ImageFont, Image, ImageDraw
from lxml import etree as ET
import tinycss
import os
from bidi.algorithm import get_display
from uniseg.linebreak import line_break_units
import math
from utils.errors.TextBoxDrawerErrors import (
    MissingSVGFile,
    TextBoxNotFoundInSVG
)

DEFAULT_FONT = "static/fonts/NotoSans-Regular.ttf"
DEFAULT_FONT_OVERRIDES = {
    "ja": "static/fonts/NotoSansCJKjp-Regular.otf",
    "he": "static/fonts/OpenSansHebrew-Regular.ttf",
    "ar": "static/fonts/DejaVuSans.ttf",
    "zh-hans": "static/fonts/NotoSansCJKsc-Regular.otf",
}
DEFAULT_FONT_SIZE = 20
DEFAULT_COLOR = (0, 0, 0)

# TODO: Automate detection of supported characters in TextBoxDrawer
# https://github.com/uccser/cs-unplugged/issues/993
FONT_MAX_ORD = {
    "NotoSans-Regular": 255,
    "PatrickHand-Regular": 255,
}


class TextBox(object):
    """Class to store position/dimensions of a text box."""

    def __init__(self, vertices, width, height, color=None, font_path=None, font_size=None, angle=0):
        """Initialise TextBox.

        Args:
            vertices: (list of 4 (x,y) tuples) vertex coords - in PNG coordinate
                space - ordered clockwise from top left
            width: (float) width of textbox in PNG space
            height: (float) height of textbox in PNG space
            color: (RGB 3-tuple or HEX string) text color, if given in SVG
            font_path: (str) path to font, if given in SVG
            font_size: (int) font size, if given in SVG
            angle: (float) rotation angle of textbox, anti-clockwise, in radians
        """
        self.vertices = vertices
        self.width = width
        self.height = height
        self.color = color
        self.font_path = font_path
        self.font_size = font_size
        self.angle = angle  # In radians


class TextBoxDrawer(object):
    """Class to draw text boxes onto an image.

    Text_box layout is defined by elements in an exported SVG.
    """

    def __init__(self, image, draw, svg_path=None):
        """Initialise TextBoxDrawer.

        Args:
            image: PIL Image object
            draw: PIL ImageDraw object
            svg_path: (str) path to SVG file for text box layout. If None,
                an instantiated TextBox objects will have to be provided for
                each call to write_text_box
        """
        self.image = image
        self.draw = draw
        if svg_path:
            self.svg = self.load_svg(svg_path)
            self.width_ratio, self.height_ratio = self.get_dimension_ratios()

    @staticmethod
    def load_svg(svg_path):
        """Load SVG element tree.

        Args:
            svg_path: (str) path to svg file

        Returns:
            (ElementTree) root node of SVG

        Raises:
            MissingSVGFile: SVG file could not be found at given path
        """
        try:
            svg = ET.parse(svg_path).getroot()
            # Remove comments within SVG to avoid errors
            ET.strip_tags(svg, ET.Comment)
            return svg
        except OSError:
            raise MissingSVGFile(svg_path)

    def get_dimension_ratios(self):
        """Get ratios between SVG and image coordinate spaces.

        Returns:
            (width_ratio, height_ratio) tuple.
        """
        vbx, vby, vbw, vbh = map(float, self.svg.attrib["viewBox"].split())
        width, height = self.image.size
        width_ratio = width / vbw
        height_ratio = height / vbh
        return width_ratio, height_ratio

    def get_box(self, box_id):
        """Get TextBox object representing the box with the given ID.

        Args:
            box_id: (str) identifier of the textbox, matching the "id" attribute
                of a rectangle element in the SVG
        Returns:
            TextBox object

        Raises:
            TextBoxNotFoundInSVG: No textbox could be found with the given id
        """
        # Replace underscores with hex code (mimic AI export behavior)
        box_id = box_id.replace('_', '_x5F_')
        # If starts with digit, replace with hex code (mimic AI export behavior)
        if box_id[0].isdigit():
            box_id = "_x{}_{}".format(hex(ord(box_id[0]))[2:], box_id[1:])
        text_layer = self.svg.find("{http://www.w3.org/2000/svg}g[@id=\"TEXT\"]")
        namespaces = {
            "x": "http://www.w3.org/2000/svg",
            "re": "http://exslt.org/regular-expressions"
        }
        try:
            text_elem = text_layer.xpath(
                "x:text[re:test(@id, '{}(_[0-9]_)?')]".format(box_id),
                namespaces=namespaces
            )[0]
            box_elem = text_elem.getprevious()
            assert box_elem is not None
        except Exception:
            try:
                box_elem = text_layer.xpath(
                    "x:rect[re:test(@id, '{}(_[0-9]_)?')]".format(box_id),
                    namespaces=namespaces
                )[0]
                text_elem = box_elem.getnext()
                assert text_elem is not None
            except Exception:
                raise TextBoxNotFoundInSVG(box_id)

        tspan_element = text_elem.find("{http://www.w3.org/2000/svg}tspan")
        if tspan_element is not None:
            # Use style of the first line of text
            style_attrib = tspan_element.attrib["style"]
        else:
            # Use style of the only line of text
            style_attrib = text_elem.attrib["style"]
        rules, _ = tinycss.make_parser().parse_style_attr(style_attrib)
        style = {}
        for rule in rules:
            style[rule.name] = rule.value[0].value
        color = style.get("fill")
        font = style.get("font-family")
        font_size = style.get("font-size")

        x = float(box_elem.attrib.get("x", 0))
        y = float(box_elem.attrib.get("y", 0))
        width = float(box_elem.attrib["width"])
        height = float(box_elem.attrib["height"])

        # SVG coord space
        vertices = [
            (x, y), (x + width, y), (x + width, y + height), (x, y + height)
        ]

        rect_transform = box_elem.attrib.get("transform")
        if rect_transform and rect_transform.startswith("matrix"):
            a, b, c, d, e, f = list(map(float, rect_transform[7:-1].split()))
            for i, (x, y) in enumerate(vertices):
                new_x = (a*x) + (c*y) + e
                new_y = (b*x) + (d*y) + f
                vertices[i] = (new_x, new_y)
            # x, y = new_x, new_y
            # Assume rotation without scaling
            angle = math.acos(a)
        else:
            angle = 0

        # Convert into PNG Coordinate Space
        vertices = [(x * self.width_ratio, y * self.height_ratio) for (x, y) in vertices]
        width *= self.width_ratio
        height *= self.height_ratio
        if font_size:
            font_size = int(font_size * self.height_ratio)

        return TextBox(
            vertices=vertices,
            width=width,
            height=height,
            color=color,
            font_path="static/fonts/{}.ttf".format(font),
            font_size=font_size,
            angle=angle,
        )

    def write_text_box(self, box, string, **kwargs):
        """Write text onto image in the space defined by the given textbox.

        Args:
            box: (str or TextBox) either the id of a text element in the SVG,
                or an instantiated TextBox object defining the area to fill
                with text. If an svg path was not given to __init__, this must
                be a TextBox object.
            string: (str) text to write
        """
        if isinstance(box, str):
            # We've been given a box id- retrieve from SVG
            box = self.get_box(box)
        self.write_text_box_object(self.image, self.draw, box, string, **kwargs)

    @staticmethod
    def get_text_width(font, text):
        """Get width of given text in given font.

        Args:
            font: PIL.ImageFont object
            text: (str) text to get width of
        """
        left, top, right, bottom = font.getbbox(text)
        width = right - left
        return width

    @staticmethod
    def get_font(font_path, font_size):
        """Get ImageFont instance for given font path/size."""
        return ImageFont.truetype(font_path, font_size)

    @staticmethod
    def get_default_font():
        """Get default font for the current language."""
        language = get_language()
        if language in DEFAULT_FONT_OVERRIDES:
            return DEFAULT_FONT_OVERRIDES[language]
        return DEFAULT_FONT

    @classmethod
    def fallback_font_if_required(cls, font_path, text):
        """Check if the given text can be rendered in the requested font.

        Returns:
            (str) <font_path> if all chars can be rendered, otherwise a default.
        """
        if font_path:
            font_name = os.path.splitext(os.path.basename(font_path))[0]
            max_ord_allowed = FONT_MAX_ORD[font_name]
            max_ord = ord(max(text, key=ord))
            if max_ord > max_ord_allowed:
                # Text contains codepoints without a glyph in requested font
                font_path = cls.get_default_font()
        else:
            font_path = cls.get_default_font()
        return font_path

    @staticmethod
    def get_font_y_offset(font):
        """Get vertical offset of a given font.

        When rendering a line of text in a given font, there is a vertical
        offset between the given height, and the top of the character.
        See https://stackoverflow.com/questions/43060479/ for details.

        Args:
            font: (ImageFont)
        """
        (_, _), (_, offset_y) = font.font.getsize("A")
        return offset_y

    @classmethod
    def fit_text(cls, text, box_width, box_height, font_path, font_size, line_spacing):
        """Fit given text into given dimensons by modifying line breaks and font size.

        Args:
            text: (str) text to fit
            box_width: (int) width of available area
            box_height: (int) height of available area
            font_path: (str) path to font file
            font_size: (int) size of font, in pixels
            line_spacing: (int) number of pixels spacing between lines

        Returns:
            4-tuple: (
                modified font size (int),
                lines of text (list of strings),
                width of fitted text (int),
                height of fitted text (int)
            )
        """
        if text:
            font_size_is_ok = False
            lines, text_width, text_height = cls.fit_text_for_font_size(
                text,
                box_width,
                box_height,
                font_path,
                font_size,
                line_spacing
            )
            if text_height <= box_height:
                font_size_is_ok = True

            while not font_size_is_ok:
                # Decrease font size exponentially, and try again
                font_size = max(int(0.9 * font_size), 1)
                lines, text_width, text_height = cls.fit_text_for_font_size(
                    text,
                    box_width,
                    box_height,
                    font_path,
                    font_size,
                    line_spacing
                )
                if text_height <= box_height:
                    font_size_is_ok = True
            return font_size, lines, text_width, text_height
        else:
            return 0, "", 0, 0

    @classmethod
    def fit_text_for_font_size(cls, text, box_width, box_height, font_path, font_size, line_spacing):
        """Fit given text into given dimensons by modifying line breaks for given font size.

        Args:
            text: (str) text to fit
            box_width: (int) width of available area
            box_height: (int) height of available area
            font_path: (str) path to font file
            font_size: (int) size of font, in pixels
            line_spacing: (int) number of pixels spacing between lines

        Returns:
            3-tuple: (
                lines of text (list of strings),
                width of fitted text (int),
                height of fitted text (int)
            )
        """
        font = cls.get_font(font_path, font_size)
        lines = []
        line = ""
        breakable_units = line_break_units(text)
        for unit in breakable_units:
            potential_line = line + unit
            size = cls.get_text_width(font, potential_line)
            if size >= box_width:
                lines.append(line)
                line = unit
            else:
                line += unit

        lines.append(line)

        # Dummy image draw because multiline_textsize isn't a @classmethod
        dummy_img = Image.new("1", (1, 1))
        dummy_draw = ImageDraw.Draw(dummy_img)
        text_width, text_height = dummy_draw.multiline_textsize(
            "\n".join(lines),
            font=font,
            spacing=line_spacing)

        # Reduce text_height by offset at top
        text_height -= cls.get_font_y_offset(font)
        return lines, text_width, text_height

    @classmethod
    def write_text_box_object(cls, image, draw, text_box, text, font_path=None,
                              font_size=None, horiz_just="left", vert_just="top",
                              line_spacing=4, color=None):
        """Write text into text_box by modifying line breaks and font size as required.

        Args:
            image: (Image.Image) Base resource image
            draw: (ImageDraw.Draw) ImageDraw object for the resource image
            text_box: (TextBox) object containing textbox properties
            text: (str) text to write
            font_path: (str) path to font .ttf file. This parameter is checked
                first, followed by an attempt to match the font from the SVG,
                and then a fallback language
            font_size: (int) target font size, may be reduced to fit if required.
                This parameter is checked first, falling back to the original
                font size from the SVG
            horiz_just: (str) left, center, right
            vert_just: (str) top, center, bottom
            line_spacing: (int) number of pixels between text lines
            color: (RGB 3-tuple or HEX string) text color. This parameter is
                checked first, falling back to the original color from the SVG
        """
        # TODO: Reshape Arabic textbox
        # Issue: https://github.com/uccser/cs-unplugged/issues/769
        # import arabic_reshaper
        # if get_language() == "ar":
        #     text = arabic_reshaper.reshape(text)

        font_path = font_path or text_box.font_path
        font_path = cls.fallback_font_if_required(font_path, text)
        font_size = font_size or text_box.font_size or DEFAULT_FONT_SIZE
        font_size, lines, text_width, text_height = cls.fit_text(
            text,
            text_box.width,
            text_box.height,
            font_path,
            font_size,
            line_spacing
        )

        font = cls.get_font(font_path, font_size)
        text = "\n".join(lines)
        color = color or text_box.color or DEFAULT_COLOR

        if get_language_bidi():
            # Get RTL text
            text = get_display(text)
            # Flip horizontal justification
            if horiz_just == "right":
                horiz_just = "left"
            elif horiz_just == "left":
                horiz_just = "right"

        if vert_just == "top":
            y = 0
        elif vert_just == "center":
            y = (text_box.height - text_height)/2
        else:  # bottom
            y = (text_box.height - text_height)

        if horiz_just == "left":
            x = 0
        elif horiz_just == "center":
            x = (text_box.width - text_width)/2
        else:  # right
            x = (text_box.width - text_width)

        # Remove offset from top line, to mimic AI textbox behavior
        y -= cls.get_font_y_offset(font)

        if text_box.angle != 0:
            text_img = Image.new("RGBA", (int(text_box.width), int(text_box.height)))
            draw_text = ImageDraw.Draw(text_img)
            draw_text.multiline_text(
                (x, y),
                text,
                fill=color,
                font=font,
                align=horiz_just,
                spacing=line_spacing
            )
            text_img = text_img.rotate(math.degrees(text_box.angle), expand=1)
            vertices_xvals, vertices_yvals = zip(*text_box.vertices)
            px = int(min(vertices_xvals))
            py = int(min(vertices_yvals))
            image.paste(text_img, (px, py), text_img)
        else:
            topleft_x, topleft_y = text_box.vertices[0]
            x += topleft_x
            y += topleft_y
            draw.multiline_text(
                (x, y),
                text,
                fill=color,
                font=font,
                align=horiz_just,
                spacing=line_spacing
            )
