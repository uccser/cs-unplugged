"""Class for Number Hunt resource generator."""

from PIL import Image, ImageDraw
from random import sample
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import gettext_lazy as _
from utils.TextBoxDrawer import TextBoxDrawer, TextBox
from resources.utils.resource_parameters import EnumResourceParameter
from resources.utils.coords import calculate_box_vertices

IMAGE_PATH = "static/img/resources/number-hunt/{}.png"
FONT_PATH = "static/fonts/NotoSans-Regular.ttf"
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
        "text": _("Number Hunt"),
        "top-left-coords": (388, 4),
        "width": 1435,
        "height": 156,
        "font-size": 120,
        "font-colour": "#000000",
        "horiz-just": "center",
        "vert-just": "center",
    },
    "subtitle": {
        "top-left-coords": (388, 176),
        "width": 1435,
        "height": 156,
        "font-size": 80,
        "font-colour": "#000000",
        "horiz-just": "center",
        "vert-just": "top",
    },
    "player-1-box-title": {
        "text": _("My Boxes"),
        "top-left-coords": (2, 28),
        "width": 372,
        "height": 100,
        "font-size": 60,
        "font-colour": "#000000",
        "horiz-just": "center",
        "vert-just": "bottom",
    },
    "player-2-box-title": {
        "text": _("Opponent's Boxes"),
        "top-left-coords": (1866, 28),
        "width": 372,
        "height": 100,
        "font-size": 60,
        "font-colour": "#000000",
        "horiz-just": "center",
        "vert-just": "bottom",
    },
}

INSTRUCTIONS_HTML = _("""
<h5>Instructions</h5>

<p>
    <strong>Step 1:</strong>
    Choose a number in your boxes for your opponent to find.
</p>

<p>
    The number my opponent is looking for: _____
</p>

<p>
    <strong>Step 2:</strong>
    Write down the number your opponent has chosen for you to find.
</p>

<p>
    The number of the box I'm looking for: _____
</p>

<p>
    <strong>Step 3:</strong>
    Ask your opponent for the number stored in a random box.
    For example: <em>"What is the number in the dotted circle?"</em>.
    Write the number your opponent says in the box you asked about on the right.
    Remember to listen for the number you are looking for.
</p>

<p>
    <strong>Step 4:</strong>
    Each time your opponent guesses a box, cross out that box.
    Keep taking turns until each person's number is found.
</p>

<p>
    <strong>Step 5:</strong>
    Write down the total number of guesses for each person below.
</p>

<p>
    <strong>My total guesses:</strong> _____<br>
    <strong>Opponent's total guesses:</strong> _____
</p>
""")


class NumberHuntResourceGenerator(BaseResourceGenerator):
    """Class for Number Hunt resource generator."""

    copies = True

    @classmethod
    def get_additional_options(cls):
        """Additional options for NumberHuntResourceGenerator."""
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
        }

    def data(self):
        """Create data for a copy of the Number Hunt resource.

        Returns:
            A dictionary of the two pages for the resource.
        """
        pages = []

        prefilled_values = self.options["prefilled_values"].value
        number_order = self.options["number_order"].value

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
                color=label_data["font-colour"],
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
            coord_y_increment = 107.8
            width = 264
            height = 88
            for i, number in enumerate(numbers):
                coord_y = base_coord_y + (coord_y_increment * i)
                vertices = calculate_box_vertices((coord_x, coord_y), width, height)
                box = TextBox(
                    vertices,
                    width,
                    height,
                    font_path=FONT_PATH,
                    font_size=font_size,
                )
                textbox_drawer.write_text_box(
                    box,
                    str(number),
                    horiz_just="center",
                    vert_just="center",
                )
        pages.append({
            "type": "resource-number-hunt",
            "data": [image, INSTRUCTIONS_HTML],
            "thumbnail": True
        })
        return pages

    def subtitle_text(self):
        """Return the subtitle string of the resource as a subtitle.

        Returns:
            text for subtitle (str)
        """
        prefilled_values = self.options["prefilled_values"].value
        number_order = self.options["number_order"].value

        if prefilled_values == "blank":
            range_text = _("Blank")
        else:
            range_min, range_max, font_size = self.get_number_range(prefilled_values)
            range_text = _("{} to {}").format(range_min, range_max - 1)
            number_order_text = NUMBER_ORDER_VALUES[number_order]
            range_text = "{} - {}".format(number_order_text, range_text)
        return range_text

    @property
    def subtitle(self):
        """Return the subtitle string of the resource for a filename.

        Returns:
            text for subtitle (str)
        """
        return "{} - {}".format(self.subtitle_text(), super().subtitle)

    @staticmethod
    def get_number_range(range_descriptor):
        """Return number range tuple for resource.

        Returns:
            Tuple of (range_min, range_max, font_size)
        """
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
