"""Class for generator for a resource."""

from abc import ABC, abstractmethod
from utils.retrieve_query_parameter import retrieve_query_parameter


class BaseResourceGenerator(ABC):
    """Class for generator for a resource."""

    def __init__(self, resource):
        self.resource = resource

    @abstractmethod
    def setup(self, request):
        """Abstract method to be implemented by subclasses.

        Raise:
            NotImplementedError: When setup() method of the ResourceGenerator
            class is called.
        """
        raise NotImplementedError("Subclass does not implement the setup method.")

    @abstractmethod
    def copy(self, request):
        """Abstract method to be implemented by subclasses.

        Raise:
            NotImplementedError: When copy() method of the ResourceGenerator
            class is called.
        """
        raise NotImplementedError("Subclass does not implement the copy method.")

    def valid_options(self):
        """Provide dictionary of all valid resource parameters.

        This excludes the header text parameter.

        Returns:
            All valid options (dict).
        """
        return {
            "paper_size": ["a4", "letter"]
        }

    def subtitle(self, request):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Args:
            request: HTTP request object (HttpRequest).

        Returns:
            Text for subtitle (str).
        """
        return retrieve_query_parameter(request, "paper_size")
