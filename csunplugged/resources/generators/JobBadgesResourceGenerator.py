"""Class for Job Badges resource generator."""

from PIL import Image, ImageDraw
from utils.TextBoxDrawer import TextBox, TextBoxDrawer
from django.utils.translation import ugettext_lazy as _
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from resources.utils.coords import calculate_box_vertices

FONT_PATH = "static/fonts/NotoSans-Regular.ttf"
FONT_SIZE = 90
LABEL_DATA = {
    "programmer": {
        "text": _("Hello, I'm a Programmer"),
        "top-left-coords": (388, 4),
        "width": 1435,
        "height": 156,
        "font-colour": "#000000",
    },
    "tester": {
        "text": _("Hello, I'm a Tester"),
        "top-left-coords": (388, 4),
        "width": 1435,
        "height": 156,
        "horiz-just": "center",
        "vert-just": "center",
    },
    "bot": {
        "text": _("Hello, I'm a Bot"),
        "top-left-coords": (388, 4),
        "width": 1435,
        "height": 156,
    },
}


class JobBadgesResourceGenerator(BaseResourceGenerator):
    """Class for Job Badges resource generator."""

    def data(self):
        """Create data for a copy of the Job Badges resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        image_path = "static/img/resources/job-badges/job-badges.png"
        image = Image.open(image_path)
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
                vertices=vertices,
                width=width,
                height=height,
                font_path=FONT_PATH,
                font_size=FONT_SIZE,
            )
            textbox_drawer.write_text_box(
                box,
                label_text,
                horiz_just="center",
            )
        '''
        image_path = "static/img/resources/job-badges/job-badges.png"
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        textbox_drawer = TextBoxDrawer(image, draw)


        hello_ids = [
            "programmer_hello1",
            "programmer_hello2",
            "tester_hello1",
            "tester_hello2",
            "bot_hello1",
            "bot_hello2",
        ]

        for hello_id in hello_ids:
            textbox_drawer.write_text_box(
                hello_id,
                _("Hello, I'm a"),
                horiz_just="center"
            )

        for i in range(1, 3):
            textbox_drawer.write_text_box(
                "programmer{}".format(i),
                _("Programmer"),
                horiz_just="center"
            )
            textbox_drawer.write_text_box(
                "tester{}".format(i),
                _("Tester"),
                horiz_just="center"
            )
            textbox_drawer.write_text_box(
                "bot{}".format(i),
                _("Bot"),
                horiz_just="center"
            )
        '''

        return {"type": "image", "data": image}
