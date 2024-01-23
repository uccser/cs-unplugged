"""Class for Binary Cards resource generator."""

import os.path
from PIL import Image, ImageDraw, ImageFont
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import gettext_lazy as _
from resources.utils.resource_parameters import BoolResourceParameter

BASE_IMAGE_PATH = "static/img/resources/binary-cards/"
IMAGE_SIZE_X = 2480
IMAGE_SIZE_Y = 3508
IMAGE_DATA = [
    ("binary-cards-1-dot.png", 1),
    ("binary-cards-2-dots.png", 2),
    ("binary-cards-4-dots.png", 4),
    ("binary-cards-8-dots.png", 8),
    ("binary-cards-16-dots.png", 16),
    ("binary-cards-32-dots.png", 32),
    ("binary-cards-64-dots.png", 64),
    ("binary-cards-128-dots.png", 128),
]


class BinaryCardsResourceGenerator(BaseResourceGenerator):
    """Class for Binary Cards resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for BinaryCardsResourceGenerator."""
        return {
            "display_numbers": BoolResourceParameter(
                name="display_numbers",
                description=_("Display Numbers"),
                default=True
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
        """Create a image for Binary Cards resource.

        Returns:
            A dictionary or list of dictionaries for each resource page.
        """
        # Retrieve parameters
        display_numbers = self.options["display_numbers"].value
        black_back = self.options["black_back"].value
        image_size_y = IMAGE_SIZE_Y

        if display_numbers:
            font_path = "static/fonts/PatrickHand-Regular.ttf"
            font = ImageFont.truetype(font_path, 600)
            BASE_COORD_X = IMAGE_SIZE_X / 2
            BASE_COORD_Y = image_size_y - 100
            image_size_y = image_size_y + 300

        pages = []

        for (image_path, number) in IMAGE_DATA:
            image = Image.open(os.path.join(BASE_IMAGE_PATH, image_path))
            if display_numbers:
                background = Image.new("RGB", (IMAGE_SIZE_X, image_size_y), "#FFF")
                background.paste(image, mask=image)
                draw = ImageDraw.Draw(background)
                text = str(number)
                text_width, text_height = draw.textsize(text, font=font)
                coord_x = BASE_COORD_X - (text_width / 2)
                coord_y = BASE_COORD_Y - (text_height / 2)
                draw.text(
                    (coord_x, coord_y),
                    text,
                    font=font,
                    fill="#000"
                )
                image = background
            page = {"type": "image", "data": image}
            if number == 8:
                page["thumbnail"] = True
            pages.append(page)

            if black_back:
                black_card = Image.new("1", (IMAGE_SIZE_X, image_size_y))
                pages.append({"type": "image", "data": black_card})

        return pages

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str)
        """
        if self.options["display_numbers"].value:
            display_numbers_text = _("with numbers")
        else:
            display_numbers_text = _("without numbers")

        if self.options["black_back"].value:
            black_back_text = _("with black back")
        else:
            black_back_text = _("without black back")

        text = "{} - {} - {}".format(
            display_numbers_text,
            black_back_text,
            super().subtitle
        )
        return text
