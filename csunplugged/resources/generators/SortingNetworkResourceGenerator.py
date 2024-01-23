"""Class for Sorting Network resource generator."""

from PIL import Image, ImageDraw, ImageFont
from random import sample
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import gettext_lazy as _
from resources.utils.resource_parameters import EnumResourceParameter

PREFILLED_VALUES_VALUES = {
    "easy": _("Easy Numbers (1 digits)"),
    "medium": _("Medium Numbers (2 digits)"),
    "hard": _("Hard Numbers (3 digits)"),
    "blank": _("None (Blank - Useful as template)")
}


class SortingNetworkResourceGenerator(BaseResourceGenerator):
    """Class for Sorting Network resource generator."""

    copies = True

    @classmethod
    def get_additional_options(cls):
        """Additional options for SortingNetworkResourceGenerator."""
        return {
            "prefilled_values": EnumResourceParameter(
                name="prefilled_values",
                description=_("Prefill with Numbers"),
                values=PREFILLED_VALUES_VALUES,
                default="none"
            ),
        }

    def data(self):
        """Create data for a copy of the Sorting Network resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        image_path = "static/img/resources/resource-sorting-network-colour.png"
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        (range_min, range_max, font_size) = self.number_range()

        if self.options["prefilled_values"].value != "blank":
            font = ImageFont.truetype(font_path, font_size)
            numbers = sample(range(range_min, range_max), 6)
            base_coord_x = 70
            base_coord_y = 2560
            coord_x_increment = 204
            for number in numbers:
                text = str(number)
                text_width, text_height = draw.textsize(text, font=font)
                coord_x = base_coord_x - (text_width / 2)
                coord_y = base_coord_y - (text_height / 2)
                draw.text(
                    (coord_x, coord_y),
                    text,
                    font=font,
                    fill="#000"
                )
                base_coord_x += coord_x_increment
        return {"type": "image", "data": image}

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        range_text = PREFILLED_VALUES_VALUES[self.options["prefilled_values"].value]
        return "{} - {}".format(range_text, super().subtitle)

    def number_range(self):
        """Return number range tuple for resource.

        Returns:
            Tuple of (range_min, range_max, font_size).
        """
        prefilled_values = self.options["prefilled_values"].value
        range_min = 0
        range_max = 0
        font_size = 150
        if prefilled_values == "easy":
            range_min = 1
            range_max = 10
        elif prefilled_values == "medium":
            range_min = 10
            range_max = 100
            font_size = 120
        elif prefilled_values == "hard":
            range_min = 100
            range_max = 1000
            font_size = 90
        return (range_min, range_max, font_size)
