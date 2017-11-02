"""Class for Train Stations resource generator."""

from PIL import Image
from utils.BaseResourceGenerator import BaseResourceGenerator


class TrainStationsResourceGenerator(BaseResourceGenerator):
    """Class for Train Stations resource generator."""

    additional_valid_options = {
        "tracks": ["circular", "twisted"],
    }

    def data(self):
        """Create a image for Train Stations resource.

        Returns:
            A list of dictionaries for each resource page.
        """
        image_path = "static/img/resources/train-stations/train-stations-tracks-{}.png"
        image = Image.open(image_path.format(self.requested_options["tracks"]))
        image = image.rotate(90, expand=True)
        return {"type": "image", "data": image}

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        return "{} tracks - {}".format(
            self.requested_options["tracks"],
            super().subtitle
        )
