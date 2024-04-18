"""Class for Treasure Island resource generator."""

from django.utils.translation import gettext_lazy as _
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
    ISLAND_TYPE: _("Island posters"),
}
FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
FONT_COLOUR = "#000000"
BOX_WIDTH = 700
BOX_HEIGHT = int(BOX_WIDTH * 2 * 1.4 / 4)
PAGE_WIDTH = BOX_WIDTH * 2
PAGE_HEIGHT = BOX_HEIGHT * 4
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
        if self.options["type"].value == MAP_TYPE:
            pages = self.create_map_page()
        else:
            pages = self.create_island_posters()
        return pages

    def create_map_page(self):
        """Create map page for students.

        Returns:
            A dictionary of the data for the page.
        """
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

    def create_island_posters(self):
        """Create pages for island posters.

        Layout of each island page (comprised of 5 boxes):
        ┌─────────┐
        │         │
        │    A    │  A) Island
        │         │  B) Boat A for island
        ├────┬────┤  C) Boat B for island
        │ B  │  C │  D) Destination for Boat A
        ├────┼────┤  E) Destination for Boat B
        │ D  │  E │
        └────┴────┘

        Returns:
            List of dictionaries of data for island pages.
        """
        pages = []

        for island_id, island_data in ISLANDS.items():
            page = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), "#fff")
            draw = ImageDraw.Draw(page)

            self.add_island_box(page, island_id, island_data)
            if not island_data.get("goal", False):
                # Section B
                self.add_boat_box(page, "left", island_data["name"])
                # Section C
                self.add_boat_box(page, "right", island_data["name"])
                # Section D
                self.add_destination_box(page, "left", ISLANDS[island_data["a"]]["name"])
                # Section E
                self.add_destination_box(page, "right", ISLANDS[island_data["b"]]["name"])

            # Draw grid lines
            lines = [
                # Top left to top right
                ([(0, 0), (PAGE_WIDTH, 0)], 5, "#000"),
                # Bottom left to bottom right
                ([(0, PAGE_HEIGHT - 1), (PAGE_WIDTH, PAGE_HEIGHT - 1)], 5, "#000"),
                # Top left to bottom left
                ([(0, 0), (0, PAGE_HEIGHT)], 5, "#000"),
                # Top right to bottom right
                ([(PAGE_WIDTH - 1, 0), (PAGE_WIDTH - 1, PAGE_HEIGHT)], 5, "#000"),
                # Mid left to mid right
                ([(0, PAGE_HEIGHT / 2), (PAGE_WIDTH, PAGE_HEIGHT / 2)], 5, "#000"),
                # Three quarter left to three quarter right
                ([(0, PAGE_HEIGHT * 0.75), (PAGE_WIDTH, PAGE_HEIGHT * 0.75)], 1, "#555"),
                # Center to bottom mid
                ([(PAGE_WIDTH / 2, PAGE_HEIGHT / 2), (PAGE_WIDTH / 2, PAGE_HEIGHT - 1)], 5, "#000"),
            ]
            for line_coords, line_width, line_colour in lines:
                # line_coords = [(int(x), int(y)) for (x, y) in line_coords]
                draw.line(line_coords, fill=line_colour, width=line_width)
            pages.append({"type": "image", "data": page})
        pages[0]["thumbnail"] = True
        return pages

    def add_island_box(self, page, island_id, island_data):
        """Add island label to top of page.

        Args:
            page (Image): Page to add image to.
            island_id (str): ID of island.
            island_data (dict): Data of island.
        """
        draw = ImageDraw.Draw(page)
        textbox_drawer = TextBoxDrawer(page, draw)
        island_image = Image.open(BASE_PATH.format(island_id))
        island_width, island_height = island_image.size
        coords = (int(BOX_WIDTH - (island_width / 2)), int(((BOX_HEIGHT * 2 * 0.7) - island_height) / 2))
        page.paste(island_image, box=coords)
        island_name_width = BOX_WIDTH * 2
        island_name_height = BOX_HEIGHT * 2 * 0.3
        vertices = calculate_box_vertices(
            (0, BOX_HEIGHT * 2 * 0.7),
            island_name_width,
            island_name_height
        )
        box = TextBox(
            vertices,
            island_name_width,
            island_name_height,
            font_path=FONT_PATH,
            font_size=200,
            color=FONT_COLOUR,
        )
        textbox_drawer.write_text_box(
            box,
            island_data["name"],
            horiz_just="center",
            vert_just="top",
        )

    def add_boat_box(self, page, direction, island_name):
        """Add boat boxes to page.

        Args:
            page (Image): Page to add image to.
            direction (str): Direction boat is travelling.
            island_name (str): Name of island.
        """
        box = Image.new("RGB", (BOX_WIDTH, BOX_HEIGHT), "#fff")
        box_draw = ImageDraw.Draw(box)
        box_textbox_drawer = TextBoxDrawer(box, box_draw)

        # Add image
        boat_image = Image.open(BASE_PATH.format("boat"))
        boat_width, boat_height = boat_image.size
        # Boxes are 70% boat image, 10% island name, 20% boat name
        ratio = (BOX_HEIGHT * 0.7) / boat_height
        boat_image = boat_image.resize(
            (int(boat_width * ratio), int(boat_height * ratio))
        )
        if direction == "left":
            boat_image = boat_image.transpose(Image.FLIP_LEFT_RIGHT)
        boat_width, boat_height = boat_image.size

        box.paste(
            boat_image,
            box=(int((BOX_WIDTH / 2) - (boat_width / 2)), 0)
        )
        # First Line Text
        text_width = BOX_WIDTH
        text_height = BOX_HEIGHT * 0.1
        vertices = calculate_box_vertices(
            (0, BOX_HEIGHT * 0.7),
            text_width,
            text_height,
        )
        text_box = TextBox(
            vertices,
            text_width,
            text_height,
            font_path=FONT_PATH,
            font_size=50,
            color=FONT_COLOUR,
        )
        box_textbox_drawer.write_text_box(
            text_box,
            island_name,
            horiz_just="center",
            vert_just="center",
        )
        # Second line of text
        text_width = BOX_WIDTH
        text_height = BOX_HEIGHT * 0.2
        vertices = calculate_box_vertices(
            (0, BOX_HEIGHT * 0.8),
            text_width,
            text_height,
        )
        text_box = TextBox(
            vertices,
            text_width,
            text_height,
            font_path=FONT_PATH,
            font_size=70,
            color=FONT_COLOUR,
        )
        if direction == "left":
            boat_text = _("Boat A")
            x_position = 0
        else:
            boat_text = _("Boat B")
            x_position = BOX_WIDTH
        box_textbox_drawer.write_text_box(
            text_box,
            boat_text,
            horiz_just="center",
            vert_just="center",
        )
        box = box.transpose(Image.ROTATE_180)
        page.paste(
            box,
            box=(x_position, BOX_HEIGHT * 2)
        )

    def add_destination_box(self, page, direction, destination_name):
        """Add destination boxes to page.

        Args:
            page (Image): Page to add image to.
            direction (str): Direction boat is travelling.
            destination_name (str): Name of destination island.
        """
        draw = ImageDraw.Draw(page)
        textbox_drawer = TextBoxDrawer(page, draw)
        if direction == "left":
            x_position = 0
        else:
            x_position = BOX_WIDTH
        vertices = calculate_box_vertices(
            (x_position, BOX_HEIGHT * 3),
            BOX_WIDTH,
            BOX_HEIGHT,
        )
        text_box = TextBox(
            vertices,
            BOX_WIDTH,
            BOX_HEIGHT,
            font_path=FONT_PATH,
            font_size=50,
            color=FONT_COLOUR,
        )
        textbox_drawer.write_text_box(
            text_box,
            destination_name,
            horiz_just="center",
            vert_just="center",
        )

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
