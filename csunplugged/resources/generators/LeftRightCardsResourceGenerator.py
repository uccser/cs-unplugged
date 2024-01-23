"""Class for Left and Right Cards resource generator."""

from PIL import Image, ImageDraw
from math import pi
from utils.TextBoxDrawer import TextBoxDrawer, TextBox
from django.utils.translation import gettext_lazy as _
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from resources.utils.coords import calculate_box_vertices

FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
FONT_SIZE = 300
LABEL_DATA = {
    "left": {
        "text": _("Left"),
        "areas": [
            ((13, 84), 660, 315),
            ((701, 84), 660, 315),
            ((1389, 84), 660, 315),
            ((2077, 84), 660, 315),
        ],
        "rotation": 0,
    },
    "right": {
        "text": _("Right"),
        "areas": [
            ((13, 1660), 660, 315),
            ((701, 1660), 660, 315),
            ((1389, 1660), 660, 315),
            ((2077, 1660), 660, 315),
        ],
        "rotation": pi,
    },
}


class LeftRightCardsResourceGenerator(BaseResourceGenerator):
    """Class for Left and Right Cards resource generator."""

    def data(self):
        """Create data for a copy of the Left and Right Cards resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        image_path = "static/img/resources/left-right-cards/left-right-cards.png"
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        textbox_drawer = TextBoxDrawer(image, draw)
        for label, label_data in LABEL_DATA.items():
            label_text = label_data["text"]
            for (top_left, width, height) in label_data["areas"]:
                vertices = calculate_box_vertices(top_left, width, height)
                box = TextBox(
                    vertices,
                    width,
                    height,
                    font_path=FONT_PATH,
                    font_size=FONT_SIZE,
                    angle=label_data["rotation"]
                )
                textbox_drawer.write_text_box(
                    box,
                    label_text,
                    horiz_just="center",
                )
        image = image.rotate(90, expand=True)
        return {"type": "image", "data": image}
