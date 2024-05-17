"""Class for Binary Cards (small) resource generator."""

from PIL import Image, ImageDraw, ImageFont
import os.path
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import ugettext_lazy as _
from resources.utils.resource_parameters import EnumResourceParameter, BoolResourceParameter


BASE_IMAGE_PATH = "static/img/resources/binary-cards-small/"
IMAGE_SIZE_X = 2480
IMAGE_SIZE_Y = 3044
IMAGE_DATA = [
    ("binary-cards-small-1.png", 4),
    ("binary-cards-small-2.png", 8),
    ("binary-cards-small-3.png", 12),
]

NUMBER_BITS_VALUES = {
    "4": _("Four (1 to 8)"),
    "8": _("Eight (1 to 128)"),
    "12": _("Twelve (1 to 2048)")
}


class BinaryCardsSmallResourceGenerator(BaseResourceGenerator):
    """Class for Binary Cards (small) resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for BinaryCardsSmallResourceGenerator."""
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
                default=True,
            ),
            "black_back": BoolResourceParameter(
                name="black_back",
                description=_("Black on Card Back"),
                default=False,
                true_text=_("Yes - Uses a lot of black ink, but conveys clearer card state. Print double sided."),
                false_text=_("No - Print single sided.")
            )
        }

    def data(self):
        """Create a image for Binary Cards (small) resource.

        Returns:
            A dictionary or list of dictionaries for each resource page.
        """
        if self.options["dot_counts"].value:
            font_path = "static/fonts/PatrickHand-Regular.ttf"
            font = ImageFont.truetype(font_path, 200)
            TEXT_COORDS = [
                (525, 1311),
                (1589, 1311),
                (525, 2859),
                (1589, 2859),
            ]

        pages = []

        for (image_path, image_bits) in IMAGE_DATA:
            if image_bits <= int(self.options["number_bits"].value):
                image = Image.open(os.path.join(BASE_IMAGE_PATH, image_path))
                if self.options["dot_counts"].value:
                    draw = ImageDraw.Draw(image)
                    for number in range(image_bits - 4, image_bits):
                        text = str(pow(2, number))
                        left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
                        text_width, text_height = right - left, bottom - top
                        coord_x = TEXT_COORDS[number % 4][0] - (text_width / 2)
                        coord_y = TEXT_COORDS[number % 4][1] - (text_height / 2)
                        draw.text(
                            (coord_x, coord_y),
                            text,
                            font=font,
                            fill="#000"
                        )
                pages.append({"type": "image", "data": image})

                if self.options["black_back"].value:
                    black_card = Image.new("1", (IMAGE_SIZE_X, IMAGE_SIZE_Y))
                    pages.append({"type": "image", "data": black_card})
        pages[0]["thumbnail"] = True
        return pages

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str)
        """
        if self.options["dot_counts"].value:
            display_numbers_text = _("with dot counts")
        else:
            display_numbers_text = _("without dot counts")
        if self.options["black_back"].value:
            black_back_text = _("with black back")
        else:
            black_back_text = _("without black back")
        text = "{} - {} - {} - {}".format(
            NUMBER_BITS_VALUES[self.options["number_bits"].value],
            display_numbers_text,
            black_back_text,
            super().subtitle
        )
        return text
