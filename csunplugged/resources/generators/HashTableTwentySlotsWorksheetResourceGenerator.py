"""Class for Hash Table Worksheet resource generator."""

from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.template.loader import render_to_string


class HashTableTwentySlotsWorksheetResourceGenerator(BaseResourceGenerator):
    """Class for Hash Table Worksheet resource generator."""

    copies = True

    def data(self):
        """Create data for a copy of the Hash Table Worksheet resource.

        Returns:
            A dictionary of HTML for the resource.
        """
        pages = []

        mod_20_buckets = [{"number": i} for i in range(20)]
        html = render_to_string(
            "resources/hash-table-20-slots-worksheet.html",
            {
                "mod_20_buckets": mod_20_buckets,
            }
        )
        pages.append({"type": "html", "data": html, "thumbnail": True})

        return pages
