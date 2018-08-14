"""Class for Treasure Hunt resource generator."""

from PIL import Image, ImageDraw, ImageFont
from random import sample
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import ugettext as _
from utils.TextBoxDrawer import TextBoxDrawer, TextBox
from resources.utils.resource_parameters import EnumResourceParameter, BoolResourceParameter
from resources.utils.coords import calculate_box_vertices

IMAGE_PATH = "static/img/resources/treasure-hunt/{}.png"
FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
PREFILLED_VALUES_VALUES = {
    "easy": _("Easy Numbers (2 digits)"),
    "medium": _("Medium Numbers (3 digits)"),
    "hard": _("Hard Numbers (4 digits)"),
    "blank": _("None (Blank)")
}
NUMBER_ORDER_VALUES = {
    "sorted": _("Sorted Numbers"),
    "unsorted": _("Unsorted Numbers")
}
LABEL_DATA = {
    "title": {
        "text": _("The hidden treasure"),
        "top-left-coords": (411, 30),
        "width": 842,
        "height": 288,
        "font-size": 120,
        "horiz-just": "center",
        "vert-just": "center",
    },
    "subtitle": {
        "top-left-coords": (411, 321),
        "width": 842,
        "height": 146,
        "font-size": 80,
        "horiz-just": "center",
        "vert-just": "center",
    },
    "player-1-box-title": {
        "text": _("My Boxes"),
        "top-left-coords": (2, 28),
        "width": 372,
        "height": 100,
        "font-size": 60,
        "horiz-just": "center",
        "vert-just": "bottom",
    },
    "player-2-box-title": {
        "text": _("Opponent's Boxes"),
        "top-left-coords": (1290, 28),
        "width": 372,
        "height": 100,
        "font-size": 60,
        "horiz-just": "center",
        "vert-just": "bottom",
    },
    "player-1-goal": {
        "text": _("Opponent is looking for:"),
        "top-left-coords": (412, 602),
        "width": 344,
        "height": 136,
        "font-size": 60,
        "horiz-just": "center",
        "vert-just": "center",
    },
    "player-2-goal": {
        "text": _("I'm looking for:"),
        "top-left-coords": (903, 602),
        "width": 344,
        "height": 136,
        "font-size": 60,
        "horiz-just": "center",
        "vert-just": "center",
    },
    "player-2-guesses": {
        "text": _("Opponent's total guesses:"),
        "top-left-coords": (412, 3255),
        "width": 344,
        "height": 136,
        "font-size": 60,
        "horiz-just": "center",
        "vert-just": "center",
    },
    "player-1-guesses": {
        "text": _("My total guesses:"),
        "top-left-coords": (903, 3255),
        "width": 344,
        "height": 136,
        "font-size": 60,
        "horiz-just": "center",
        "vert-just": "center",
    },
}


class TreasureHuntResourceGenerator(BaseResourceGenerator):
    """Class for Treasure Hunt resource generator."""

    copies = True

    @classmethod
    def get_additional_options(cls):
        """Additional options for TreasureHuntResourceGenerator."""
        return {
            "prefilled_values": EnumResourceParameter(
                name="prefilled_values",
                description=_("Prefill with Numbers"),
                values=PREFILLED_VALUES_VALUES,
                default="easy"
            ),
            "number_order": EnumResourceParameter(
                name="number_order",
                description=_("Numbers Unsorted/Sorted"),
                values=NUMBER_ORDER_VALUES,
                default="sorted"
            ),
            "instructions": BoolResourceParameter(
                name="instructions",
                description=_("Include instruction sheets"),
                default=True
            ),
        }

    def data(self):
        """Create data for a copy of the Treasure Hunt resource.

        Returns:
            A dictionary of the two pages for the resource.
        """
        pages = []
        font_path = "static/fonts/PatrickHand-Regular.ttf"

        prefilled_values = self.options["prefilled_values"].value
        number_order = self.options["number_order"].value
        instructions = self.options["instructions"].value
        if instructions:
            image = Image.open(IMAGE_PATH.format("instructions"))
            ImageDraw.Draw(image)
            pages.append({"type": "image", "data": image})

        image = Image.open(IMAGE_PATH.format("template"))
        draw = ImageDraw.Draw(image)
        textbox_drawer = TextBoxDrawer(image, draw)

        # Add text labels
        for label_id, label_data in LABEL_DATA.items():
            if label_id == "subtitle":
                label_text = self.subtitle_text()
            else:
                label_text = label_data["text"]
            top_left_coords = label_data["top-left-coords"]
            width = label_data["width"]
            height = label_data["height"]
            vertices = calculate_box_vertices(top_left_coords, width, height)
            box = TextBox(
                vertices,
                width,
                height,
                font_path=FONT_PATH,
                font_size=label_data["font-size"],
            )
            textbox_drawer.write_text_box(
                box,
                label_text,
                horiz_just=label_data["horiz-just"],
                vert_just=label_data["vert-just"],
            )

        # Add numbers to image (if required)
        if prefilled_values != "blank":
            range_min, range_max, font_size = self.get_number_range(prefilled_values)
            total_numbers = 31
            numbers = sample(range(range_min, range_max), total_numbers)
            if number_order == "sorted":
                numbers.sort()

            coord_x = 106
            base_coord_y = 161
            coord_y_increment = 107.5
            width = 264
            height = 88
            for i, number in enumerate(numbers):
                coord_y = base_coord_y + (coord_y_increment * i)
                vertices = calculate_box_vertices((coord_x, coord_y), width, height)
                box = TextBox(
                    vertices,
                    width,
                    height,
                    font_path=font_path,
                    font_size=font_size,
                )
                textbox_drawer.write_text_box(
                    box,
                    str(number),
                    horiz_just="center",
                    vert_just="center",
                )
        pages.append({"type": "image", "data": image, "thumbnail": True})
        return pages

    def subtitle_text(self):
        """Return the subtitle string of the resource as a subtitle.

        Returns:
            text for subtitle (str)
        """
        prefilled_values = self.options["prefilled_values"].value
        number_order = self.options["number_order"].value

        if prefilled_values == "blank":
            range_text = _("blank")
        else:
            range_min, range_max, font_size = self.get_number_range(prefilled_values)
            range_text = _("{} to {}").format(range_min, range_max - 1)
            number_order_text = number_order.title()
            range_text = "{} - {}".format(number_order_text, range_text)
        return range_text

    @property
    def subtitle(self):
        """Return the subtitle string of the resource for a filename.

        Returns:
            text for subtitle (str)
        """
        if self.options["instructions"].value:
            instructions_text = _("with instructions")
        else:
            instructions_text = _("without instructions")
        return "{} - {} - {}".format(self.subtitle_text(), instructions_text, super().subtitle)

    @staticmethod
    def get_number_range(range_descriptor):
        """Return number range tuple for resource.

        Returns:
            Tuple of (range_min, range_max, font_size)
        """
        # prefilled_values = self.options["prefilled_values"].value
        range_min = 0
        if range_descriptor == "easy":
            range_max = 100
            font_size = 70
        elif range_descriptor == "medium":
            range_max = 1000
            font_size = 65
        elif range_descriptor == "hard":
            range_max = 10000
            font_size = 60
        else:
            raise ValueError("Unknown number range descriptor {}, "
                             "wanted one of [easy, medium, hard".format(range_descriptor))
        return (range_min, range_max, font_size)
