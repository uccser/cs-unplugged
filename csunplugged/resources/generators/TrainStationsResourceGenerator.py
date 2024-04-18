"""Class for Train Stations resource generator."""

from PIL import Image
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import gettext_lazy as _
from resources.utils.resource_parameters import EnumResourceParameter

TRACKS_VALUES = {
    "circular": _("Circular"),
    "twisted": _("Twisted")
}


class TrainStationsResourceGenerator(BaseResourceGenerator):
    """Class for Train Stations resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for TrainStationsResourceGenerator."""
        return {
            "tracks": EnumResourceParameter(
                name="tracks",
                description=_("Train track shape"),
                values=TRACKS_VALUES,
                default="circular"
            )
        }

    def data(self):
        """Create a image for Train Stations resource.

        Returns:
            A list of dictionaries for each resource page.
        """
        image_path = "static/img/resources/train-stations/train-stations-tracks-{}.png"
        image = Image.open(image_path.format(self.options["tracks"].value))
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
        return "{} - {}".format(
            TRACKS_VALUES[self.options["tracks"].value],
            super().subtitle
        )
