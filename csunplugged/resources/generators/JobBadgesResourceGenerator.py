"""Class for Job Badges resource generator."""

from PIL import Image, ImageDraw
from utils.TextBoxDrawer import TextBox, TextBoxDrawer
from django.utils.translation import ugettext_lazy as _
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from resources.utils.coords import calculate_box_vertices

FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
FONT_SIZE = 200
TEXTBOX_WIDTH = 1000
TEXTBOX_HEIGHT = 275
LABEL_DATA = {
    "programmer": _("Hello, I'm a Programmer"),
    "tester": _("Hello, I'm a Tester"),
    "bot": _("Hello, I'm a Bot"),
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
        
        # coordinates of top left point of text box
        top_left_x_coord, top_left_y_coord = 50, 100
        
        # Add text labels
        for label, label_text in LABEL_DATA.items():
            # left box
            vertices = calculate_box_vertices(
                (top_left_x_coord, top_left_y_coord),
                TEXTBOX_WIDTH,
                TEXTBOX_HEIGHT
            )
            box = TextBox(
                vertices=vertices,
                width=TEXTBOX_WIDTH,
                height=TEXTBOX_HEIGHT,
                font_path=FONT_PATH,
                font_size=FONT_SIZE,
            )
            textbox_drawer.write_text_box(
                box,
                label_text,
                horiz_just="center",
            )
            # right box
            right_box_coords = (top_left_x_coord+1150, top_left_y_coord)
            vertices = calculate_box_vertices(
                right_box_coords,
                TEXTBOX_WIDTH,
                TEXTBOX_HEIGHT
            )
            box = TextBox(
                vertices=vertices,
                width=TEXTBOX_WIDTH,
                height=TEXTBOX_HEIGHT,
                font_path=FONT_PATH,
                font_size=FONT_SIZE,
            )
            textbox_drawer.write_text_box(
                box,
                label_text,
                horiz_just="center",
            )

            # increase y coord for next name tag down
            top_left_y_coord += 700

        return {"type": "image", "data": image}
