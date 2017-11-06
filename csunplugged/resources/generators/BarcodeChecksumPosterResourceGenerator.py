"""Class for Barcode Checksum Poster resource generator."""

from PIL import Image
from resources.utils.BaseResourceGenerator import BaseResourceGenerator


class BarcodeChecksumPosterResourceGenerator(BaseResourceGenerator):
    """Class for Grid resource generator."""

    additional_valid_options = {
        "barcode_length": ["12", "13"]
    }

    def data(self):
        """Create data for a copy of the Grid resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        image_path = "static/img/resources/barcode-checksum-poster/{}-digits.png"
        image_path = image_path.format(self.requested_options["barcode_length"])
        image = Image.open(image_path)
        return {"type": "image", "data": image}

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        barcode_length = self.requested_options["barcode_length"]
        return "{} digits - {}".format(barcode_length, super().subtitle)
