"""Class for Barcode Checksum Poster resource generator."""

from PIL import Image, ImageDraw
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from utils.TextBoxDrawer import TextBoxDrawer
from django.utils.translation import gettext_lazy as _
from resources.utils.resource_parameters import EnumResourceParameter

BARCODE_LENGTH_VALUES = {
    "12": _("12 digits"),
    "13": _("13 digits"),
}


class BarcodeChecksumPosterResourceGenerator(BaseResourceGenerator):
    """Class for Grid resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for BarcodeChecksumPosterResourceGenerator."""
        return {
            "barcode_length": EnumResourceParameter(
                name="barcode_length",
                description=_("Barcode length"),
                values=BARCODE_LENGTH_VALUES,
                default="12"
            )
        }

    def data(self):
        """Create data for a copy of the Grid resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        path = "static/img/resources/barcode-checksum-poster/{}-digits"
        barcode_length = self.options["barcode_length"].value
        path = path.format(barcode_length)
        image_path = "{}.png".format(path)
        svg_path = "{}.svg".format(path)
        image = Image.open(image_path)

        draw = ImageDraw.Draw(image)
        textbox_drawer = TextBoxDrawer(image, draw, svg_path)

        textbox_drawer.write_text_box(
            "title",
            _("{} Digit Barcode").format(barcode_length),
            horiz_just="center",
        )

        headings = {
            "heading1": _("Separate!"),
            "heading2": _("Operate!"),
            "heading3": _("Calculate!")
        }

        for heading_id, heading in headings.items():
            textbox_drawer.write_text_box(
                heading_id,
                heading,
            )

        textbox_drawer.write_text_box(
            "paragraph",
            _("Remember that this algorithm uses modulo 10, so we are only "
              "interested in the number in the one's column."),
        )

        return {"type": "image", "data": image}

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        barcode_length = self.options["barcode_length"].value
        return "{} - {}".format(BARCODE_LENGTH_VALUES[barcode_length], super().subtitle)
