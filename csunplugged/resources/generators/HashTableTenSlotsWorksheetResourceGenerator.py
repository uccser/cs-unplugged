"""Class for Hash Table Worksheet resource generator."""

from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from django.template.loader import render_to_string


class HashTableTenSlotsWorksheetResourceGenerator(BaseResourceGenerator):
    """Class for Hash Table Worksheet resource generator."""

    copies = True

    def data(self):
        """Create data for a copy of the Hash Table Worksheet resource.

        Returns:
            A dictionary of HTML for the resource.
        """
        pages = []

        mod_10_buckets = [{"number": i} for i in range(10)]
        html = render_to_string(
            "resources/hash-table-10-slots-worksheet.html",
            {
                "mod_10_buckets": mod_10_buckets,
            }
        )
        pages.append({"type": "html", "data": html, "thumbnail": True})

        return pages
