"""Class for Binary Cards (small) resource generator."""

from PIL import Image, ImageDraw, ImageFont
import os.path
from resources.utils.BaseResourceGenerator import BaseResourceGenerator

BASE_IMAGE_PATH = "static/img/resources/binary-cards-small/"
IMAGE_SIZE_X = 2480
IMAGE_SIZE_Y = 3044
IMAGE_DATA = [
    ("binary-cards-small-1.png", 4),
    ("binary-cards-small-2.png", 8),
    ("binary-cards-small-3.png", 12),
]


class BinaryCardsSmallResourceGenerator(BaseResourceGenerator):
    """Class for Binary Cards (small) resource generator."""

    additional_valid_options = {
        "number_bits": ["4", "8", "12"],
        "dot_counts": [True, False],
        "black_back": [True, False],
    }

    def data(self):
        """Create a image for Binary Cards (small) resource.

        Returns:
            A dictionary or list of dictionaries for each resource page.
        """
        if self.requested_options["dot_counts"]:
            font_path = "static/fonts/PatrickHand-Regular.ttf"
            font = ImageFont.truetype(font_path, 200)
            TEXT_COORDS = [
                (525, 1341),
                (1589, 1341),
                (525, 2889),
                (1589, 2889),
            ]

        pages = []

        for (image_path, image_bits) in IMAGE_DATA:
            if image_bits <= int(self.requested_options["number_bits"]):
                image = Image.open(os.path.join(BASE_IMAGE_PATH, image_path))
                if self.requested_options["dot_counts"]:
                    draw = ImageDraw.Draw(image)
                    for number in range(image_bits - 4, image_bits):
                        text = str(pow(2, number))
                        text_width, text_height = draw.textsize(text, font=font)
                        coord_x = TEXT_COORDS[number % 4][0] - (text_width / 2)
                        coord_y = TEXT_COORDS[number % 4][1] - (text_height / 2)
                        draw.text(
                            (coord_x, coord_y),
                            text,
                            font=font,
                            fill="#000"
                        )
                pages.append({"type": "image", "data": image})

                if self.requested_options["black_back"]:
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
        if self.requested_options["dot_counts"]:
            display_numbers_text = "with dot counts"
        else:
            display_numbers_text = "without dot counts"
        if self.requested_options["black_back"]:
            black_back_text = "with black back"
        else:
            black_back_text = "without black back"
        text = "{} bits - {} - {} - {}".format(
            self.requested_options["number_bits"],
            display_numbers_text,
            black_back_text,
            super().subtitle
        )
        return text
