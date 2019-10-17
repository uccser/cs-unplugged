"""Class for Pixel Demonstration resource generator."""

from PIL import Image
from resources.utils.BaseResourceGenerator import BaseResourceGenerator


class PixelsDemonstrationResourceGenerator(BaseResourceGenerator):
    """Class for Pixel Demonstration resource generator."""

    def data(self):
        """Create data for a copy of the pixel demonstration resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        image = Image.open("static/img/resources/pixels-demonstration/pixel-visible-grid-with-letter-no-numbers.png")
        return {"type": "image", "data": image}
