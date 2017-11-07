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
        # Use deepcopy to avoid successive generators from sharing the same
        # valid_options dictionary.
        super().__init__(requested_options)

    def data(self):
        """Create data for a copy of the resource.

        Returns:
            A dictionary of the one page for the resource.
        """
        return {"type": "html", "data": "Page 1"}
