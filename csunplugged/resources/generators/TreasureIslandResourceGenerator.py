"""Class for Treasure Island resource generator."""

from django.utils.translation import ugettext_lazy as _
from PIL import Image, ImageDraw
from utils.TextBoxDrawer import TextBoxDrawer, TextBox
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from resources.utils.resource_parameters import EnumResourceParameter
from resources.utils.coords import calculate_box_vertices

BASE_PATH = "static/img/resources/treasure-island/{}.png"
MAP_TYPE = "map"
ISLAND_TYPE = "island"
TYPE_VALUES = {
    MAP_TYPE: _("Student map"),
    # ISLAND_TYPE: _("Islands"),
}
FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
FONT_COLOUR = "#000000"
ISLANDS = {
    "dead-mans-island": {
        "name": _("Dead Man's Island"),
        "map-location": {
            "top-left-coords": (1206, 480),
            "width": 732,
            "height": 216,
        },
        "a": "musket-hill",
        "b": "shipwreck-bay",
    },
    "musket-hill": {
        "name": _("Musket Hill"),
        "map-location": {
            "top-left-coords": (537, 2080),
            "width": 831,
            "height": 141,
        },
        "a": "pirates-island",
        "b": "mutineers-island",
    },
    "mutineers-island": {
        "name": _("Mutineers' Island"),
        "map-location": {
            "top-left-coords": (1422, 1640),
            "width": 690,
            "height": 159,
        },
        "a": "smugglers-cove",
        "b": "dead-mans-island",
    },
    "pirates-island": {
        "name": _("Pirates' Island"),
        "map-location": {
            "top-left-coords": (72, 1370),
            "width": 885,
            "height": 204,
        },
        "a": "shipwreck-bay",
        "b": "musket-hill",
    },
    "shipwreck-bay": {
        "name": _("Shipwreck Bay"),
        "map-location": {
            "top-left-coords": (51, 555),
            "width": 831,
            "height": 225,
        },
        "a": "musket-hill",
        "b": "dead-mans-island",
    },
    "smugglers-cove": {
        "name": _("Smugglers' Cove"),
        "map-location": {
            "top-left-coords": (2298, 1220),
            "width": 702,
            "height": 204,
        },
        "a": "pirates-island",
        "b": "treasure-island",
    },
    "treasure-island": {
        "name": _("Treasure Island"),
        "map-location": {
            "top-left-coords": (2286, 450),
            "width": 711,
            "height": 237,
        },
        "goal": True,
    },
}


class TreasureIslandResourceGenerator(BaseResourceGenerator):
    """Class for Treasure Island resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for TreasureIslandResourceGenerator."""
        return {
            "type": EnumResourceParameter(
                name="type",
                description=_("Printable type"),
                values=TYPE_VALUES,
                default="map"
            )
        }

    def data(self):
        """Create data for a copy of the Treasure Island resource.

        Returns:
            A dictionary of the data for the resource.
        """
        pages = []
        if self.options["type"].value == MAP_TYPE:
            pages.append(self.create_map_page())
        return pages

    def create_map_page(self):
        path = BASE_PATH.format(MAP_TYPE)
        image = Image.open(path)
        draw = ImageDraw.Draw(image)
        textbox_drawer = TextBoxDrawer(image, draw)

        for island_id, island_data in ISLANDS.items():
            box_data = island_data["map-location"]
            top_left_coords = box_data["top-left-coords"]
            width = box_data["width"]
            height = box_data["height"]
            vertices = calculate_box_vertices(top_left_coords, width, height)
            box = TextBox(
                vertices,
                width,
                height,
                font_path=FONT_PATH,
                font_size=80,
                color=FONT_COLOUR,
            )
            textbox_drawer.write_text_box(
                box,
                island_data["name"],
                horiz_just="center",
                vert_just="top",
            )

        image = image.rotate(90, expand=True)
        page_data = {
            "type": "image",
            "data": image
        }
        return page_data

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        printable_type = self.options["type"].value
        return "{} - {}".format(TYPE_VALUES[printable_type], super().subtitle)
