"""Class for Piano Keys resource generator."""

from PIL import Image, ImageDraw
from utils.str_to_bool import str_to_bool
from utils.TextBoxDrawer import TextBoxDrawer, TextBox
from django.utils.translation import gettext_lazy as _
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from resources.utils.resource_parameters import EnumResourceParameter


KEY_LABELS = {
    "no": _("Blank"),
    "type-1": ["C",  "D",  "E",  "F",  "G",   "A",   "B"],
    "type-2": ["C",  "D",  "E",  "F",  "G",   "A",   "H"],
    "type-3": ["Do", "Re", "Mi", "Fa", "So",  "La",  "Ti"],
    "type-4": ["Do", "Re", "Mi", "Fa", "Sol", "La",  "Si"],
}
KEY_AREAS = [
    ([(65, 493), (220, 493), (65, 632), (220, 632)], 157, 140),
    ([(255, 493), (390, 493), (255, 632), (390, 632)], 125, 140),
    ([(424, 493), (582, 493), (424, 632), (582, 632)], 159, 140),
    ([(617, 493), (792, 493), (617, 632), (792, 632)], 180, 140),
    ([(836, 493), (985, 493), (836, 632), (985, 632)], 155, 140),
    ([(1024, 493), (1175, 493), (1024, 632), (1175, 632)], 159, 140),
    ([(1213, 493), (1355, 493), (1213, 632), (1355, 632)], 145, 140),
    ([(1392, 493), (1557, 493), (1392, 632), (1557, 632)], 167, 140),
    ([(1591, 493), (1744, 493), (1591, 632), (1744, 632)], 157, 140),
    ([(1784, 493), (1966, 493), (1784, 632), (1966, 632)], 184, 140),
    ([(1998, 493), (2154, 493), (1998, 632), (2154, 632)], 157, 140),
    ([(2185, 493), (2351, 493), (2185, 632), (2351, 632)], 169, 140),
    ([(2378, 493), (2526, 493), (2378, 632), (2526, 632)], 150, 140),
    ([(2556, 493), (2709, 493), (2556, 632), (2709, 632)], 154, 140),
]
LABEL_COLOURS = [
    "#ffdd0e",
    "#0b983a",
    "#0f70b7",
    "#82358c",
    "#2b2e83",
    "#e30613",
    "#ea5b0c",
]


class PianoKeysResourceGenerator(BaseResourceGenerator):
    """Class for Piano Keys resource generator."""

    @classmethod
    def get_additional_options(cls):
        """Additional options for PianoKeysResourceGenerator."""
        return {
            "label": EnumResourceParameter(
                name="label",
                description=_("Piano key labels"),
                values=create_key_labels(),
                default="type-1"
            )
        }

    def data(self):
        """Create a image for Piano Keys resource.

        Returns:
            A list of dictionaries for each resource page.
        """
        label_type = self.options["label"].value
        image_path = "static/img/resources/piano-keys/keyboard.png"
        image = Image.open(image_path)
        if str_to_bool(label_type):
            self.label_keys(image, label_type)
        image = image.rotate(90, expand=True)
        return {"type": "image", "data": image}

    def label_keys(self, image, label_type):
        """Label keys on image.

        Args:
            image (Image): PillowImage of image.
            label_type (str): Key of label type.
        """
        draw = ImageDraw.Draw(image)
        textbox_drawer = TextBoxDrawer(image, draw)
        labels = KEY_LABELS[label_type]
        for index, (vertices, width, height) in enumerate(KEY_AREAS):
            position = index % 7
            box = TextBox(
                vertices,
                width,
                height,
                color=LABEL_COLOURS[position],
                font_path="static/fonts/PatrickHand-Regular.ttf",
                font_size=120,
            )
            textbox_drawer.write_text_box(
                box,
                labels[position],
                horiz_just="center",
            )

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        label = KEY_LABELS[self.options["label"].value]
        if isinstance(label, list):
            label = ", ".join(label)
        return "{} - {}".format(
            label,
            super().subtitle
        )


def create_key_labels():
    """Return dictionary of option labels.

    Returns:
        Dictionary of values used for options.
    """
    labels = dict()
    for key, data in KEY_LABELS.items():
        if type(data) is list:
            labels[key] = ", ".join(data)
        else:
            labels[key] = data
    return labels
