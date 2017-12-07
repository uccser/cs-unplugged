"""Class for Binary Windows resource generator."""

import os.path
from PIL import Image, ImageDraw, ImageFont
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import ugettext as _
from resources.utils.resource_parameters import EnumResourceParameter, BoolResourceParameter

BASE_IMAGE_PATH = "static/img/resources/binary-windows/"
FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
FONT = ImageFont.truetype(FONT_PATH, 300)
SMALL_FONT = ImageFont.truetype(FONT_PATH, 180)

NUMBER_BITS_VALUES = {
    "4": _("Four (1 to 8)"),
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
        number_of_bits = self.options["number_bits"].value
        value_type = self.options["value_type"].value
        dot_counts = self.options["dot_counts"].value

        pages = []
        page_sets = [("binary-windows-1-to-8.png", 8)]
        if number_of_bits == "8":
            page_sets.append(("binary-windows-16-to-128.png", 128))

        for (filename, dot_count_start) in page_sets:
            image = Image.open(os.path.join(BASE_IMAGE_PATH, filename))
            image = self.add_digit_values(image, value_type, True, 660, 724, 1700, FONT)
            if dot_counts:
                image = self.add_dot_counts(image, dot_count_start, SMALL_FONT)
            image = image.rotate(90, expand=True)
            pages.append({"type": "image", "data": image})
            pages.append(self.back_page(value_type))
        pages[0]["thumbnail"] = True
        return pages

    def back_page(self, value_type):
        """Return a Pillow object of back page of Binary Windows.

        Args:
            value_type: Type of value representation used (str).

        Returns:
            A dictionary for the back page.
        """
        image = Image.open(os.path.join(BASE_IMAGE_PATH, "binary-windows-blank.png"))
        image = self.add_digit_values(image, value_type, False, 660, 724, 650, FONT)
        image = image.rotate(90, expand=True)
        return {"type": "image", "data": image}

    def add_dot_counts(self, image, starting_value, font):
        """Add dot count text onto image.

        Args:
            image: The image to add text to (Pillow Image).
            starting_value: Number on left window (int).
            font: Font used for adding text (Pillow Font).

        Returns:
            Pillow Image with text added (Pillow Image).
        """
        value = starting_value
        draw = ImageDraw.Draw(image)
        coord_x = 660
        coord_x_increment = 724
        coord_y = 1000
        for i in range(4):
            text = str(value)
            text_width, text_height = draw.textsize(text, font=font)
            text_coord_x = coord_x - (text_width / 2)
            text_coord_y = coord_y - (text_height / 2)
            draw.text(
                (text_coord_x, text_coord_y),
                text,
                font=font,
                fill="#000"
            )
            coord_x += coord_x_increment
            value = int(value / 2)
        return image

    def add_digit_values(self, image, value_type, on, x_coord_start, x_coord_increment, base_y_coord, font):
        """Add binary values onto image.

        Args:
            image: The image to add binary values to (Pillow Image).
            value_type: Either "binary" for 0's and 1's, or "lightbulb" for
                        lit and unlit lightbulbs (str).
            on: True if binary value is on/lit, otherwise False (bool).
            x_coord_start: X co-ordinate starting value (int).
            x_coord_increment: X co-ordinate increment value (int).
            base_y_coord: Y co-ordinate value (int).
            font: Font used for adding text (Pillow Font).

        Returns:
            Pillow Image with binary values (Pillow Image).
        """
        text_coord_x = x_coord_start

        if value_type == "binary":
            if on:
                text = "1"
            else:
                text = "0"
        else:  # lightbulb
            if on:
                image_file = "col_binary_lightbulb.png"
            else:
                image_file = "col_binary_lightbulb_off.png"
            lightbulb = Image.open(os.path.join("static/img/topics/", image_file))
            (width, height) = lightbulb.size
            scale_factor = 0.6
            lightbulb = lightbulb.resize((int(width * scale_factor), int(height * scale_factor)))
            (width, height) = lightbulb.size
            lightbulb_width = int(width / 2)
            lightbulb_height = int(height / 2)
            if not on:
                lightbulb = lightbulb.rotate(180)

        for i in range(4):
            draw = ImageDraw.Draw(image)
            if value_type == "binary":

                text_width, text_height = draw.textsize(text, font=font)
                coord_x = text_coord_x - (text_width / 2)
                coord_y = base_y_coord - (text_height / 2)
                draw.text(
                    (coord_x, coord_y),
                    text,
                    font=font,
                    fill="#000"
                )
            else:  # lightbulb
                coords = (text_coord_x - lightbulb_width, base_y_coord - lightbulb_height + 75)
                image.paste(lightbulb, box=coords, mask=lightbulb)
            text_coord_x += x_coord_increment
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
            count_text = "with dot counts"
        else:
            count_text = "without dot counts"
        TEMPLATE = "{} bits - {} - {} - {}"
        text = TEMPLATE.format(
            self.options["number_bits"].value,
            self.options["value_type"].value,
            count_text,
            super().subtitle
        )
        return text
