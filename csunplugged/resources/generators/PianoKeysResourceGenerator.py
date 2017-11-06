"""Class for Piano Keys resource generator."""

from PIL import Image, ImageDraw
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from utils.bool_to_yes_no import bool_to_yes_no

KEY_DATA = {
    "A": {
        "colour": "hsl(356, 95%, 85%)",
        "areas": [
            ((1002, 21), (1005, 711), (1200, 716), (1193, 15)),
            ((2392, 15), (2356, 720), (2541, 720), (2552, 17)),
        ],
    },
    "B": {
        "colour": "hsl(21, 90%, 85%)",
        "areas": [
            ((1193, 15), (1200, 716), (1369, 719), (1400, 15)),
            ((2552, 17), (2541, 720), (2713, 720), (2756, 20)),
        ],
    },
    "C": {
        "colour": "hsl(52, 100%, 85%)",
        "areas": [
            ((15, 15), (51, 711), (255, 715), (186, 21)),
            ((1395, 24), (1371, 720), (1566, 717), (1590, 18)),
        ],
    },
    "D": {
        "colour": "hsl(140, 87%, 85%)",
        "areas": [
            ((186, 21), (255, 715), (408, 714), (390, 15)),
            ((1590, 18), (1566, 717), (1760, 718), (1794, 12)),
        ],
    },
    "E": {
        "colour": "hsl(205, 85%, 85%)",
        "areas": [
            ((390, 15), (408, 714), (603, 717), (585, 12)),
            ((1794, 12), (1760, 718), (1979, 720), (2004, 19)),
        ],
    },
    "F": {
        "colour": "hsl(293, 45%, 85%)",
        "areas": [
            ((585, 12), (603, 717), (828, 720), (717, 15)),
            ((2004, 19), (1979, 720), (2163, 720), (2192, 15)),
        ],
    },
    "G": {
        "colour": "hsl(238, 51%, 85%)",
        "areas": [
            ((717, 15), (828, 720), (1005, 711), (1002, 21)),
            ((2192, 15), (2163, 720), (2356, 720), (2392, 15)),
        ],
    },
}


class PianoKeysResourceGenerator(BaseResourceGenerator):
    """Class for Piano Keys resource generator."""

    additional_valid_options = {
        "highlight": [False, "A", "B", "C", "D", "E", "F", "G"],
    }

    def data(self):
        """Create a image for Piano Keys resource.

        Returns:
            A list of dictionaries for each resource page.
        """
        highlight = self.requested_options["highlight"]
        image_path = "static/img/resources/piano-keys/keyboard.png"
        image = Image.open(image_path)
        page = Image.new("RGB", image.size, "#FFF")

        if highlight:
            self.highlight_key_areas(page, KEY_DATA.get(highlight))

        # Add piano keys overlay
        page.paste(image, mask=image)

        page = page.rotate(90, expand=True)
        return {"type": "image", "data": page}

    def highlight_key_areas(self, image, key_data):
        """Highlights the page of keys.

        Args:
            image: PillowImage of page.
            key_data: Dictionary of highlight colour and areas (dict).
        """
        draw = ImageDraw.Draw(image)
        for area in key_data["areas"]:
            draw.polygon(area, fill=key_data["colour"])

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        return "{} highlight - {}".format(
            bool_to_yes_no(self.requested_options["highlight"]),
            super().subtitle
        )
