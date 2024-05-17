"""Class for Sorting Network Cards resource generator."""

import os.path
from random import sample
from PIL import Image, ImageDraw, ImageFont
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import gettext_lazy as _
from resources.utils.resource_parameters import EnumResourceParameter

IMAGE_SIZE_X = 2000
IMAGE_SIZE_Y = 2800
LINE_COLOUR = "#000000"
LINE_WIDTH = 3

SEPERATOR = ","
DEFAULT_FONT = "static/fonts/PatrickHand-Regular.ttf"
CARD_TYPE_DATA = {
    "small_numbers": {
        "label": _("Small numbers (1 to 10)"),
        "font-size": 800,
    },
    "large_numbers": {
        "label": _("Large numbers (7 digit numbers)"),
        "font-size": 500,
    },
    "letters": {
        "label": _("Letters"),
        # Translators: A set of letters from your language's alphabet, seperated by commas
        "values": _("L,O,N,K,E,D,S,P,G,B,I,Y"),
        "font-size": 800,
        "translated": True,
    },
    "words": {
        "label": _("Words"),
        # Translators: A set of words from your language with similar spelling, seperated by commas
        "values": _("crocodile,crochet,kiwi,weka,kiwi,kiwano"),
        "font-size": 500,
        "translated": True,
    },
    "fractions": {
        "label": _("Fractions"),
        "values": [u"\u00bd", u"\u2153", u"\u2154", u"\u215c", u"\u00be", u"\u215d"],
        "font-size": 900,
        "font": "static/fonts/NotoSans-Regular.ttf",
    },
    "butterfly": {
        "label": _("Butterfly life cycle"),
        "images": [
            "butterfly-story-leaf.png",
            "butterfly-story-baby-caterpillar.png",
            "butterfly-story-caterpillar.png",
            "butterfly-story-young-pupa.png",
            "butterfly-story-mature-pupa.png",
            "butterfly-story-butterfly.png",
        ]
    },
    "riding_hood": {
        "label": _("Little Red Riding Hood"),
        "images": [
            "little-red-riding-hood-1.png",
            "little-red-riding-hood-2.png",
            "little-red-riding-hood-3.png",
            "little-red-riding-hood-4.png",
            "little-red-riding-hood-5.png",
            "little-red-riding-hood-6.png",
        ]
    },
    "kauri_tree": {
        "label": _("Kauri tree"),
        "images": [
            "kauri-tree/kauri-1.png",
            "kauri-tree/kauri-2.png",
            "kauri-tree/kauri-3.png",
            "kauri-tree/kauri-4.png",
            "kauri-tree/kauri-5.png",
            "kauri-tree/kauri-6.png",
        ],
    },
}


class SortingNetworkCardsResourceGenerator(BaseResourceGenerator):
    """Class for Sorting Network Cards resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for SortingNetworkCardsResourceGenerator."""
        return {
            "type": EnumResourceParameter(
                name="type",
                description=_("Card Type"),
                values=create_key_labels(),
                default="large_numbers"
            )
        }

    def data(self):
        """Create a image for Sorting Network Cards resource.

        Returns:
            A list of dictionaries for each resource page.
        """
        card_type = self.options["type"].value

        # Create card outlines
        card_outlines = Image.new("RGB", (IMAGE_SIZE_X, IMAGE_SIZE_Y), "#fff")
        draw = ImageDraw.Draw(card_outlines)
        for x_coord in range(0, IMAGE_SIZE_X, IMAGE_SIZE_X - LINE_WIDTH):
            draw.line([(x_coord, 0), (x_coord, IMAGE_SIZE_Y)], fill=LINE_COLOUR, width=LINE_WIDTH)
        for y_coord in range(0, IMAGE_SIZE_Y, int(IMAGE_SIZE_Y / 2 - LINE_WIDTH)):
            draw.line([(0, y_coord), (IMAGE_SIZE_X, y_coord)], fill=LINE_COLOUR, width=LINE_WIDTH)

        card_centers = [
            (IMAGE_SIZE_X / 2, IMAGE_SIZE_Y / 4),
            (IMAGE_SIZE_X / 2, (IMAGE_SIZE_Y / 4) * 3),
        ]

        # Add text to cards
        pages = []
        type_data = CARD_TYPE_DATA[card_type]
        if "images" in type_data:
            images = type_data["images"]
            IMAGE_PADDING = 20
            MAX_IMAGE_X = IMAGE_SIZE_X - IMAGE_PADDING * 2
            MAX_IMAGE_Y = IMAGE_SIZE_Y / 2 - IMAGE_PADDING * 2
            BASE_PATH = "static/img/resources/sorting-network-cards/"
            for (image_number, filename) in enumerate(images):
                image = Image.open(os.path.join(BASE_PATH, filename))
                (width, height) = image.size
                if height > MAX_IMAGE_Y or width > MAX_IMAGE_X:
                    height_ratio = MAX_IMAGE_Y / height
                    width_ratio = MAX_IMAGE_X / width
                    ratio = min(height_ratio, width_ratio)
                    width *= ratio
                    height *= ratio
                    image = image.resize((int(width), int(height)), Image.LANCZOS)
                if image_number % 2 == 0:
                    page = card_outlines.copy()
                    draw = ImageDraw.Draw(page)
                    (x, y) = card_centers[0]
                else:
                    (x, y) = card_centers[1]
                coords = (int(x - (width / 2)), int(y - (height / 2)))
                page.paste(image, box=coords, mask=image)
                # If image on second card but not last page
                if image_number % 2 == 1 and image_number != len(images) - 1:
                    pages.append({"type": "image", "data": page})
        else:
            if card_type == "small_numbers":
                text = [str(i) for i in range(1, 11)]
            elif card_type == "large_numbers":
                text = []
                numbers = sample(range(1700000, 2100000), 10)
                for number in numbers:
                    text.append("{:,}".format(number))
            elif type_data.get("translated", False):
                text = type_data["values"].split(SEPERATOR)
            else:
                text = type_data["values"]

            font_path = type_data.get("font", DEFAULT_FONT)
            font = ImageFont.truetype(font_path, type_data["font-size"])

            for (text_number, text_string) in enumerate(text):
                if text_number % 2 == 0:
                    page = card_outlines.copy()
                    draw = ImageDraw.Draw(page)
                    (x, y) = card_centers[0]
                else:
                    (x, y) = card_centers[1]

                left, top, right, bottom = draw.textbbox((0, 0), text_string, font=font)
                text_width, text_height = right - left, bottom - top
                coord_x = x - (text_width / 2)
                coord_y = y - text_height
                draw.text(
                    (coord_x, coord_y),
                    text_string,
                    font=font,
                    fill="#000"
                )
                # If text on second card but not last page
                if text_number % 2 == 1 and text_number != len(text) - 1:
                    pages.append({"type": "image", "data": page})

        pages.append({"type": "image", "data": page, "thumbnail": True})
        return pages

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        return "{} - {}".format(
            CARD_TYPE_DATA[self.options["type"].value]["label"],
            super().subtitle
        )


def create_key_labels():
    """Return dictionary of option labels.

    Returns:
        Dictionary of values used for options.
    """
    labels = dict()
    for key, data in CARD_TYPE_DATA.items():
        labels[key] = data["label"]
    return labels
