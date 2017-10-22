"""Class for Arrows resource generator."""

from PIL import Image
from utils.BaseResourceGenerator import BaseResourceGenerator


class ArrowsResourceGenerator(BaseResourceGenerator):
    """Class for Arrows resource generator."""

    def data(self):
        """Create data for a copy of the Arrows resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        image = Image.open("static/img/resources/arrows/arrows.png")
        return {"type": "image", "data": image}
