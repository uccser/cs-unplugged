"""Class for Job Badges resource generator."""

from PIL import Image, ImageDraw
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import ugettext as _
from utils.TextBoxDrawer import TextBoxDrawer


class JobBadgesResourceGenerator(BaseResourceGenerator):
    """Class for Job Badges resource generator."""

    def data(self):
        """Create data for a copy of the Job Badges resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        path = "static/img/resources/job-badges/job-badges"
        image_path = "{}.png".format(path)
        svg_path = "{}.svg".format(path)
        image = Image.open(image_path)

        draw = ImageDraw.Draw(image)
        textbox_drawer = TextBoxDrawer(image, draw, svg_path)

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

        return {"type": "image", "data": image}
