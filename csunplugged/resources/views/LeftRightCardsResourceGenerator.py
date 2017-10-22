"""Class for Left and Right Cards resource generator."""

from PIL import Image
from utils.BaseResourceGenerator import BaseResourceGenerator


class LeftRightCardsResourceGenerator(BaseResourceGenerator):
    """Class for Left and Right Cards resource generator."""

    def data(self):
        """Create data for a copy of the Left and Right Cards resource.

        Returns:
            A dictionary of the one page for the resource.
        """

        image_path = "static/img/resources/left-right-cards/left-right-cards.png"
        image = Image.open(image_path)
        return {"type": "image", "data": image}
