"""Class for Treasure Island resource generator."""

from yattag import Doc
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from resources.utils.resource_parameters import EnumResourceParameter

TYPE_VALUES = {
    "map": _("Student map"),
    "islands": _("Islands"),
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
