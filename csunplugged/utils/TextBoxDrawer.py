"""Module for TextBoxDrawer class."""

from PIL import ImageFont
import xml.etree.ElementTree as ET


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
        vbx, vby, vbw, vbh = map(int, self.svg.attrib['viewBox'].split())
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
        element = self.svg.find('{{http://www.w3.org/2000/svg}}rect[@id="{}"]'.format(box_id))
        return TextBox(
            x=float(element.attrib.get('x', 0)) * self.width_ratio,
            y=float(element.attrib.get('y', 0)) * self.height_ratio,
            width=float(element.attrib['width']) * self.width_ratio,
            height=float(element.attrib['height']) * self.height_ratio
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

    def write_text_box_object(self, text_box, text, font_path="static/fonts/NotoSans-Regular.ttf",
                              font_size=11, horiz_just='left', vert_just='top',
                              justify_last_line=False, **kwargs):
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
            line_height = self.get_font_height(font)
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
            text_height = len(lines) * line_height

            if text_height <= text_box.height:
                font_size_is_ok = True
            else:
                font_size = max(int(0.9 * font_size), 1)

        if vert_just == 'top':
            height = text_box.y
        elif vert_just == 'center':
            height = text_box.y + (text_box.height - text_height)/2
        elif vert_just == 'bottom':
            height = text_box.y + (text_box.height - text_height)
        for index, line in enumerate(lines):
            if horiz_just == 'left':
                self.draw.text((text_box.x, height), line, font=font, **kwargs)
            elif horiz_just == 'right':
                total_width = self.get_text_width(font, line)
                x_left = text_box.x + text_box.width - total_width
                self.draw.text((x_left, height), line, font=font, **kwargs)
            elif horiz_just == 'center':
                total_width = self.get_text_width(font, line)
                x_left = int(text_box.x + ((text_box.width - total_width) / 2))
                self.draw.text((x_left, height), line, font=font, **kwargs)
            elif horiz_just == 'justify':
                words = line.split()
                if (index == len(lines) - 1 and not justify_last_line) or \
                   len(words) == 1:
                    self.draw.text((text_box.x, height), line, font=font, **kwargs)
                    continue
                line_without_spaces = ''.join(words)
                total_width = self.get_text_width(font, line_without_spaces)
                space_width = (text_box.width - total_width) / (len(words) - 1.0)
                start_x = text_box.x
                for word in words[:-1]:
                    self.draw.text((start_x, height), word, font=font, **kwargs)
                    word_width = self.get_text_width(font, word)
                    start_x += word_width + space_width
                last_word_width = self.get_text_width(font, words[-1])
                last_word_x = text_box.x + text_box.width - last_word_width
                self.draw.text((last_word_x, height), words[-1], font=font, **kwargs)
            height += line_height
