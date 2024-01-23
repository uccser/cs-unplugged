"""Class for Parity Cards resource generator."""

from PIL import Image, ImageDraw
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import gettext_lazy as _
from resources.utils.resource_parameters import EnumResourceParameter

CARDS_COLUMNS = 4
CARDS_ROWS = 5
CARD_SIZE = 500
IMAGE_SIZE_X = CARD_SIZE * CARDS_COLUMNS
IMAGE_SIZE_Y = CARD_SIZE * CARDS_ROWS
LINE_COLOUR = "#000000"
LINE_WIDTH = 3

BACK_COLOUR_VALUES = {
    "black": _("Black"),
    "blue": _("Blue"),
    "green": _("Green"),
    "purple": _("Purple"),
    "red": _("Red"),
}


class ParityCardsResourceGenerator(BaseResourceGenerator):
    """Class for Parity Cards resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for ParityCardsResourceGenerator."""
        return {
            "back_colour": EnumResourceParameter(
                name="back_colour",
                description=_("Card back colour"),
                values=BACK_COLOUR_VALUES,
                default="black"
            )
        }

    def data(self):
        """Create a image for Parity Cards resource.

        Returns:
            A list of dictionaries for each resource page.
        """
        front_page = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#fff")
        draw = ImageDraw.Draw(front_page)
        for x_coord in range(0, IMAGE_SIZE_X, CARD_SIZE):
            draw.line(
                [(x_coord, 0), (x_coord, IMAGE_SIZE_Y)],
                fill=LINE_COLOUR,
                width=LINE_WIDTH
            )
        draw.line(
            [(IMAGE_SIZE_X - 1, 0), (IMAGE_SIZE_X - 1, IMAGE_SIZE_Y)],
            fill=LINE_COLOUR,
            width=LINE_WIDTH
        )
        for y_coord in range(0, IMAGE_SIZE_Y, CARD_SIZE):
            draw.line(
                [(0, y_coord), (IMAGE_SIZE_X, y_coord)],
                fill=LINE_COLOUR,
                width=LINE_WIDTH
            )
        draw.line(
            [(0, IMAGE_SIZE_Y - 1), (IMAGE_SIZE_X, IMAGE_SIZE_Y - 1)],
            fill=LINE_COLOUR,
            width=LINE_WIDTH
        )

        back_colour = self.options["back_colour"].value

        if back_colour == "black":
            back_colour_hex = "#000000"
        elif back_colour == "blue":
            back_colour_hex = "#3366ff"
        elif back_colour == "green":
            back_colour_hex = "#279f2d"
        elif back_colour == "purple":
            back_colour_hex = "#6e3896"
        else:
            back_colour_hex = "#cc0423"
        pages = [
            {
                "type": "image",
                "data": front_page,
                "thumbnail": True
            },
            {
                "type": "image",
                "data": Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), back_colour_hex)
            }
        ]
        return pages

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        text = "{} - {}".format(
            BACK_COLOUR_VALUES[self.options["back_colour"].value],
            super().subtitle
        )
        return text
