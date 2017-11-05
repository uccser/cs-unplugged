"""Class for Barcode Checksum Poster resource generator."""

from PIL import Image, ImageDraw
from utils.BaseResourceGenerator import BaseResourceGenerator
from utils.TextBoxDrawer import TextBoxDrawer
from django.utils.translation import ugettext as _


class BarcodeChecksumPosterResourceGenerator(BaseResourceGenerator):
    """Class for Grid resource generator."""

    additional_valid_options = {
        "barcode_length": ["12", "13"]
    }

    def data(self):
        """Create data for a copy of the Grid resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        path = "static/img/resources/barcode-checksum-poster/{}-digits"
        path = path.format(self.requested_options["barcode_length"])
        image_path = "{}.png".format(path)
        svg_path = "{}.svg".format(path)
        image = Image.open(image_path)

        draw = ImageDraw.Draw(image)
        textbox_drawer = TextBoxDrawer(image, draw, svg_path)

        textbox_drawer.write_text_box(
            "title",
            _("13 Digit Barcode"),
            horiz_just="center",
            vert_just="center",
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
        barcode_length = self.requested_options["barcode_length"]
        return "{} digits - {}".format(barcode_length, super().subtitle)
