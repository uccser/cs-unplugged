"""Module for creating bare resource generator."""

from django.http import QueryDict
from resources.utils.BaseResourceGenerator import BaseResourceGenerator


class BareResourceGenerator(BaseResourceGenerator):
    """Class for bare resource generator."""

    def __init__(self, requested_options=QueryDict("paper_size=a4")):
        """Construct BareResourceGenerator instance.

        Args:
            requested_options: QueryDict of requested_options (QueryDict).
        """
        super().__init__(requested_options)

    def data(self):
        """Create data for a copy of the resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        return {"type": "html", "data": "Page 1"}


class BareResourceGeneratorWithCopies(BareResourceGenerator):
    """Class for bare resource generator with copies."""

    copies = True


class BareResourceGeneratorMultiPage(BareResourceGenerator):
    """Class for bare resource generator with two pages."""

    def data(self):
        """Create data for a copy of the resource.

        Returns:
            A list of two dictionaries, one for each page of the resource.
        """
        return [
            {"type": "html", "data": "Page 1"},
            {"type": "html", "data": "Page 2"}
        ]
