"""Class for Treasure Hunt resource generator."""

from PIL import Image, ImageDraw, ImageFont
from random import sample
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import ugettext as _
from collections import OrderedDict
from resources.utils.resource_parameters import EnumResourceParameter, BoolResourceParameter

IMAGE_PATH = "static/img/resources/treasure-hunt/{}.png"

PREFILLED_VALUES_VALUES = {
    "easy": _("Easy Numbers (2 digits)"),
    "medium": _("Medium Numbers (3 digits)"),
    "hard": _("Hard Numbers (4 digits)"),
    "blank": _("None (Blank)")
}

NUMBER_ORDER_VALUES = {
    "sorted": _("Sorted Numbers"),
    "unsorted": _("Unsorted Numbers")
}

ART_VALUES = {
    "bw": _("Table only - Little ink usage."),
    "colour": _("Table and artwork - Uses a lot of colour ink."),
}


class TreasureHuntResourceGenerator(BaseResourceGenerator):
    """Class for Treasure Hunt resource generator."""
    copies = True

    def get_additional_options(self):
        return {
            "prefilled_values": EnumResourceParameter(
                name="prefilled_values",
                description=_("Prefill with Numbers"),
                values=PREFILLED_VALUES_VALUES,
                default="easy"
            ),
            "number_order": EnumResourceParameter(
                name="number_order",
                description=_("Numbers Unsorted/Sorted"),
                values=NUMBER_ORDER_VALUES,
                default="sorted"
            ),
            "instructions": BoolResourceParameter(
                name="instructions",
                description=_("Include instruction sheets"),
                default=True
            ),
            "art": EnumResourceParameter(
                name="art",
                description=_("Printing mode"),
                values=ART_VALUES,
                default="bw"
            ),
        }

    def data(self):
        """Create data for a copy of the Treasure Hunt resource.

        Returns:
            A dictionary of the two pages for the resource.
        """

        pages = []
        font_path = "static/fonts/PatrickHand-Regular.ttf"

        prefilled_values = self.options["prefilled_values"].value
        number_order = self.options["number_order"].value
        instructions = self.options["instructions"].value
        art_style = self.options["art"].value

        if instructions:
            image = Image.open(IMAGE_PATH.format("instructions"))
            ImageDraw.Draw(image)
            pages.append({"type": "image", "data": image})

        image = Image.open(IMAGE_PATH.format(art_style))
        draw = ImageDraw.Draw(image)

        # Add numbers to image if required
        if prefilled_values != "blank":
            range_min, range_max, font_size = self.get_number_range(prefilled_values)
            font = ImageFont.truetype(font_path, font_size)

            total_numbers = 26
            numbers = sample(range(range_min, range_max), total_numbers)
            if number_order == "sorted":
                numbers.sort()

            base_coord_y = 506
            coord_y_increment = 199
            base_coords_x = [390, 700]
            for i in range(0, total_numbers):
                text = str(numbers[i])
                text_width, text_height = draw.textsize(text, font=font)

                coord_x = base_coords_x[i % 2] - (text_width / 2)
                coord_y = base_coord_y - (text_height / 2)
                if i % 2 == 1:
                    coord_y -= 10
                    base_coord_y += coord_y_increment
                draw.text(
                    (coord_x, coord_y),
                    text,
                    font=font,
                    fill="#000"
                )

            text = "{} - {} to {}".format(number_order.title(), range_min, range_max - 1)
            font = ImageFont.truetype(font_path, 75)
            text_width, text_height = draw.textsize(text, font=font)
            coord_x = 1220 - (text_width / 2)
            coord_y = 520 - (text_height / 2)
            draw.text(
                (coord_x, coord_y),
                text,
                font=font,
                fill="#000",
            )
        pages.append({"type": "image", "data": image, "thumbnail": True})
        return pages

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str)
        """
        prefilled_values = self.options["prefilled_values"].value
        number_order = self.options["number_order"].value
        instructions = self.options["instructions"].value
        art_style = self.options["art"].value

        if prefilled_values == "blank":
            range_text = "blank"
        else:
            range_min, range_max, font_size = self.get_number_range(prefilled_values)
            template = "{} - {} to {}"
            number_order_text = number_order.title()
            range_text = template.format(number_order_text, range_min, range_max - 1)

        if art_style == "colour":
            art_style_text = "full colour"
        else:
            art_style_text = "black and white"

        if instructions:
            instructions_text = "with instructions"
        else:
            instructions_text = "without instructions"

        return "{} - {} - {} - {}".format(range_text, art_style_text, instructions_text, super().subtitle)

    def get_number_range(self, range_descriptor):
        """Return number range tuple for resource.

        Returns:
            Tuple of (range_min, range_max, font_size)
        """
        # prefilled_values = self.options["prefilled_values"].value
        range_min = 0
        if range_descriptor == "easy":
            range_max = 100
            font_size = 55
        elif range_descriptor == "medium":
            range_max = 1000
            font_size = 50
        elif range_descriptor == "hard":
            range_max = 10000
            font_size = 45
        else:
            raise Exception("Unknown number range descriptor {}, wanted one of [easy, medium, hard".format(range_descriptor))
        return (range_min, range_max, font_size)
