"""Class for Binary Windows resource generator."""

import os.path
from PIL import Image, ImageDraw, ImageFont
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import ugettext_lazy as _
from resources.utils.resource_parameters import EnumResourceParameter, BoolResourceParameter

BASE_IMAGE_PATH = "static/img/resources/binary-windows/"
FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
FONT = ImageFont.truetype(FONT_PATH, 300)
SMALL_FONT = ImageFont.truetype(FONT_PATH, 180)
IMAGE_SIZE_X = 2334
IMAGE_SIZE_Y = 1650
LINE_COLOUR = "#000000"
LINE_WIDTH = 1

NUMBER_BITS_VALUES = {
    "4": _("Four (1 to 8)"),
    "5": _("Five (1 to 16)"),
    "6": _("Six (1 to 32)"),
    "8": _("Eight (1 to 128)"),
}

VALUE_TYPE_VALUES = {
    "binary": _("Binary (0 or 1)"),
    "lightbulb": _("Lightbulb (off or on)"),
}


class BinaryWindowsResourceGenerator(BaseResourceGenerator):
    """Class for Binary Windows resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for BinaryWindowsResourceGenerator."""
        return {
            "number_bits": EnumResourceParameter(
                name="number_bits",
                description=_("Number of Bits"),
                values=NUMBER_BITS_VALUES,
                default="4"
            ),
            "dot_counts": BoolResourceParameter(
                name="dot_counts",
                description=_("Display Dot Counts"),
                default=True
            ),
            "value_type": EnumResourceParameter(
                name="value_type",
                description=_("Value Representation"),
                values=VALUE_TYPE_VALUES,
                default="binary"
            ),
        }

    def data(self):
        """Create a image for Binary Windows resource.

        Returns:
            A dictionary or list of dictionaries for each resource page.
        """
        # Retrieve parameters
        number_of_bits = int(self.options["number_bits"].value)
        value_type = self.options["value_type"].value
        show_bits_value = self.options["dot_counts"].value

        # Define variables
        column_width = IMAGE_SIZE_X / number_of_bits

        # Get page outline
        page_outline = self.page_outline(number_of_bits, column_width)
        front_page = self.front_page(
            value_type,
            column_width,
            show_bits_value,
            page_outline.copy()
        )
        back_page = self.back_page(
            value_type,
            column_width,
            page_outline.copy()
        )
        pages = [front_page, back_page]
        return pages

    def page_outline(self, number_of_bits, column_width):
        """Create outline (lines without content) for page.

        Args:
            number_of_bits (int): Number of bits on page.
            column_width (int): Width of each bit on page.

        Return:
            Page outline as type Image.
        """
        page_outline = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#fff")
        draw = ImageDraw.Draw(page_outline)
        image_midpoint_y = int(IMAGE_SIZE_Y / 2)

        # Draw outline
        draw.rectangle(
            [(0, 0), (IMAGE_SIZE_X - LINE_WIDTH, IMAGE_SIZE_Y - LINE_WIDTH)],
            outline=LINE_COLOUR,
            fill="#ffffff",
            width=LINE_WIDTH,
        )

        # Draw internal separator lines
        for line_number in range(1, number_of_bits):
            x_coord = line_number * column_width
            draw.line(
                [(x_coord, 0), (x_coord, image_midpoint_y)],
                fill=LINE_COLOUR,
                width=LINE_WIDTH,
            )

        # Draw dashed line
        dash_size = 10
        for x_coord in range(0, IMAGE_SIZE_X, dash_size * 3):
            draw.line(
                [(x_coord, image_midpoint_y), (x_coord + dash_size, image_midpoint_y)],
                fill="#666666",
                width=LINE_WIDTH,
            )

        return page_outline

    def front_page(self, value_type, column_width, show_bits_value, page_outline):
        """Return a Pillow object of front page of Binary Windows.

        Args:
            value_type (str): Type of value representation used.
            column_width (float): Width of a bit column.
            show_bits_value (bool): True if bit value labels should be shown.
            page_outline (Pillow Draw): Outline of page to draw on.

        Returns:
            A dictionary for the back page.
        """
        image = self.add_dots(page_outline, column_width, show_bits_value)
        image = self.add_digit_values(page_outline, column_width, value_type, True)
        image = image.rotate(90, expand=True)
        return {"type": "image", "data": image, "thumbnail": True}

    def back_page(self, value_type, column_width, page_outline):
        """Return a Pillow object of back page of Binary Windows.

        Args:
            value_type (str): Type of value representation used.
            column_width (float): Width of a bit column.
            page_outline (Pillow Draw): Outline of page to draw on.

        Returns:
            A dictionary for the back page.
        """
        image = self.add_digit_values(page_outline, column_width, value_type, False)
        image = image.rotate(90, expand=True)
        return {"type": "image", "data": image}

    def add_dots(self, image, column_width, show_bits_value):
        """Add binary values onto image.

        Note: This method adds dots from right to left on the page.

        Args:
            image (Pillow Image): The image to add binary values to.
            column_width (float): Width of a bit column.
            show_bits_value (bool): True if bit value labels should be shown.

        Returns:
            Pillow Image with dots (Pillow Image).
        """
        draw = ImageDraw.Draw(image)
        coord_x_start = IMAGE_SIZE_X - (column_width / 2)
        coord_x_increment = column_width
        coord_x = coord_x_start
        base_image_coord_y = IMAGE_SIZE_Y * 0.2
        base_text_coord_y = IMAGE_SIZE_Y * 0.4
        dots_value = 1

        while coord_x > 0:
            # Select dots image
            image_file = f"dots-{dots_value}.png"
            dots_image = Image.open(os.path.join(BASE_IMAGE_PATH, image_file))

            # Scale image to fit dots to 80% of column width
            (dots_width, dots_height) = dots_image.size
            x_scale_factor = (column_width / dots_width) * 0.9
            y_scale_factor = (IMAGE_SIZE_Y * 0.3) / dots_height
            scale_factor = min(x_scale_factor, y_scale_factor)
            dots_image = dots_image.resize((
                int(dots_width * scale_factor),
                int(dots_height * scale_factor),
            ))

            # Paste into image
            (dots_width, dots_height) = dots_image.size
            coords = (
                int(coord_x - (dots_width / 2)),
                int(base_image_coord_y - (dots_height / 2)),
            )
            image.paste(dots_image, box=coords, mask=dots_image)

            if show_bits_value:
                text = str(dots_value)
                text_width, text_height = draw.textsize(text, font=SMALL_FONT)
                text_coord_x = coord_x - (text_width / 2)
                text_coord_y = base_text_coord_y - (text_height / 2)
                draw.text(
                    (text_coord_x, text_coord_y),
                    text,
                    font=SMALL_FONT,
                    fill="#000"
                )

            # Update variables
            coord_x -= coord_x_increment
            dots_value *= 2
        return image

    def add_digit_values(self, image, column_width, value_type, on):
        """Add binary values onto image.

        Args:
            image (Pillow Image): The image to add binary values to.
            column_width (float): Width of a bit column.
            value_type (str): Either "binary" for 0's and 1's, or "lightbulb" for
                              lit and unlit lightbulbs.
            on (bool): True if binary value is on/lit, otherwise False.

        Returns:
            Pillow Image with binary values (Pillow Image).
        """
        coord_x_start = column_width / 2
        coord_x_increment = column_width

        if value_type == "binary":
            if on:
                text = "1"
            else:
                text = "0"
        else:  # Lightbulb
            if on:
                image_file = "lightbulb-on.png"
            else:
                image_file = "lightbulb-off.png"
            lightbulb = Image.open(os.path.join(BASE_IMAGE_PATH, image_file))
            (lightbulb_width, lightbulb_height) = lightbulb.size
            # Scale image to fit lightbulb to 80% of column width
            scale_factor = (column_width / lightbulb_width) * 0.8
            lightbulb = lightbulb.resize((
                int(lightbulb_width * scale_factor),
                int(lightbulb_height * scale_factor),
            ))
            (lightbulb_width, lightbulb_height) = lightbulb.size
            if not on:
                lightbulb = lightbulb.rotate(180)

        draw = ImageDraw.Draw(image)
        coord_x = coord_x_start

        if on:
            base_coord_y = IMAGE_SIZE_Y * 0.75
        else:
            base_coord_y = IMAGE_SIZE_Y * 0.25

        while coord_x < IMAGE_SIZE_X:
            if value_type == "binary":
                text_width, text_height = draw.textsize(text, font=FONT)
                text_coord_x = coord_x - (text_width / 2)
                text_coord_y = base_coord_y - (text_height * .7)
                draw.text(
                    (text_coord_x, text_coord_y),
                    text,
                    font=FONT,
                    fill="#000"
                )
            else:  # lightbulb
                coords = (
                    int(coord_x - (lightbulb_width / 2)),
                    int(base_coord_y - (lightbulb_height / 2)),
                )
                image.paste(lightbulb, box=coords, mask=lightbulb)
            coord_x += coord_x_increment
        return image

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        dot_counts = self.options["dot_counts"].value
        if dot_counts:
            count_text = _("with dot counts")
        else:
            count_text = _("without dot counts")
        TEMPLATE = "{} - {} - {} - {}"
        text = TEMPLATE.format(
            NUMBER_BITS_VALUES[self.options["number_bits"].value],
            VALUE_TYPE_VALUES[self.options["value_type"].value],
            count_text,
            super().subtitle
        )
        return text
