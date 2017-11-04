"""Module for TextBoxDrawer class."""

from PIL import ImageFont
from lxml import etree as ET

class TextBox(object):
    """Class to store position/dimensions of a text box."""

    def __init__(self, x, y, width, height):
        """Initialise TextBox."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height


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

        return TextBox(
            x=float(box_elem.attrib.get('x', 0)) * self.width_ratio,
            y=float(box_elem.attrib.get('y', 0)) * self.height_ratio,
            width=float(box_elem.attrib['width']) * self.width_ratio,
            height=float(box_elem.attrib['height']) * self.height_ratio
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

    def write_text_box_object(self, text_box, text, font_path="static/fonts/PatrickHand-Regular.ttf",
                              font_size=11, horiz_just='left', vert_just='top',
                              justify_last_line=False, line_spacing=4, color=(0, 0, 0)):
        """Write text into text_box by modifying line breaks and font size as required.

        Args:
            text_box: TextBox object
            text: (str) text to write
            font_path: (str) path to font .ttf file
            font_size: (int) target font size, may be reduced to fit if required
            horiz_just: (str) left, center, right or justify
            vert_just: (str) top, center, bottom
            justify_last_line: (bool) if True, fully justify the last line
        """
        font_size_is_ok = False
        while not font_size_is_ok:
            font = self.get_font(font_path, font_size)
            lines = []
            line = []
            words = text.split()
            for word in words:
                new_line = ' '.join(line + [word])
                size = self.get_text_width(font, new_line)
                if size <= text_box.width:
                    line.append(word)
                else:
                    lines.append(line)
                    line = [word]
            if line:
                lines.append(line)
            lines = [' '.join(line) for line in lines if line]
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
                font_size = max(int(0.9 * font_size), 1)

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
        elif horiz_just == 'top':
            x = text_box.x + (text_box.width - text_width)

        # Remove offset from top line, to mimic AI textbox behavior
        y -= offset_y

        self.draw.multiline_text(
            (x, y),
            '\n'.join(lines),
            fill=color,
            font=font,
            align=horiz_just,
            spacing=line_spacing
        )
