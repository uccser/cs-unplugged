"""Class for Left and Right Cards resource generator."""

from PIL import Image, ImageDraw
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import ugettext as _
from utils.TextBoxDrawer import TextBoxDrawer


class LeftRightCardsResourceGenerator(BaseResourceGenerator):
    """Class for Left and Right Cards resource generator."""

    def data(self):
        """Create data for a copy of the Left and Right Cards resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        # image_path = "static/img/resources/left-right-cards/left-right-cards.png"
        # image = Image.open(image_path)
        # return {"type": "image", "data": image}

        path = "static/img/resources/left-right-cards/left-right"
        image_path = "{}.png".format(path)
        svg_path = "{}.svg".format(path)
        image = Image.open(image_path)

        draw = ImageDraw.Draw(image)
        textbox_drawer = TextBoxDrawer(image, draw, svg_path)

        for i in range(1, 5):
            textbox_drawer.write_text_box(
                "left{}".format(i),
                _("LEFT"),
                horiz_just="center"
            )
            textbox_drawer.write_text_box(
                "right{}".format(i),
                _("RIGHT"),
                horiz_just="center"
            )

        return {"type": "image", "data": image}
