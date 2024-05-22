"""Class for Modulo Clock resource generator."""

from PIL import Image, ImageDraw, ImageFont
from math import pi, sin, cos
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.utils.translation import gettext_lazy as _
from resources.utils.resource_parameters import EnumResourceParameter

MODULO_NUMBER_VALUES = {
    "1": _("Blank"),
    "2": "2",
    "10": "10",
}


class ModuloClockResourceGenerator(BaseResourceGenerator):
    """Class for Modulo Clock resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for ModuloClockResourceGenerator."""
        return {
            "modulo_number": EnumResourceParameter(
                name="modulo_number",
                description=_("Modulo"),
                values=MODULO_NUMBER_VALUES,
                default="10",
            )
        }

    def data(self):
        """Create a image for Modulo Clock resource.

        Returns:
            A dictionary for the resource page.
        """
        image_path = "static/img/resources/modulo-clock/modulo-clock-{}.png"

        modulo_number = int(self.options["modulo_number"].value)
        image = Image.open(image_path.format(modulo_number))
        draw = ImageDraw.Draw(image)

        font_size = 150
        font_path = "static/fonts/PatrickHand-Regular.ttf"
        font = ImageFont.truetype(font_path, font_size)

        radius = 750
        x_center = image.width / 2
        y_center = image.height / 2
        # Count from the '12 oclock position'
        start_angle = pi * 1.5
        angle_between_numbers = (2 * pi) / modulo_number

        for number in range(0, modulo_number):
            text = str(number)
            angle = start_angle + (angle_between_numbers * number)
            x_coord = radius * cos(angle) + x_center
            y_coord = radius * sin(angle) + y_center
            left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
            text_width, text_height = right - left, bottom - top
            text_coord_x = x_coord - (text_width / 2)
            text_coord_y = y_coord - (text_height / 2) - 40
            draw.text(
                (text_coord_x, text_coord_y),
                text,
                font=font,
                fill="#000"
            )

        return {"type": "image", "data": image}

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            Text for subtitle (str).
        """
        modulo_number = self.options["modulo_number"].value
        if modulo_number == "1":
            modulo_text = _("Blank")
        else:
            modulo_text = modulo_number
        return "{} - {}".format(
            modulo_text,
            super().subtitle
        )
