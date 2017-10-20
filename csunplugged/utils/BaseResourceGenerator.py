"""Class for generator for a resource."""

from django.http import Http404
from abc import ABC, abstractmethod


class BaseResourceGenerator(ABC):
    """Class for generator for a resource."""

    default_valid_options = {
        "paper_size": ["a4", "letter"]
    }
    additional_valid_options = dict()

    def __init__(self, requested_options):
        """Constructor for BaseResourceGenerator.

        Args:
            request: HTTP request object (HttpRequest).
        """
        self.valid_options = BaseResourceGenerator.default_valid_options
        self.valid_options.update(self.additional_valid_options)
        self.requested_options = requested_options
        self.check_requested_options()

    @abstractmethod
    def data(self):
        """Abstract method to be implemented by subclasses.

        Raise:
            NotImplementedError: When data() method of the ResourceGenerator
            class is called.
        """
        raise NotImplementedError("Subclass does not implement the data method.")

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            Text for subtitle (str).
        """
        return self.requested_options["paper_size"]

    def check_requested_options(self):
        """Check all requested options.

        If an option cannot be found, or an option is given with an invalid
        value, then a 404 error is raised.
        """
        for option in self.valid_options.keys():
            if option not in self.requested_options:
                raise Http404("{} parameter not specified.".format(option))
            for value in self.requested_options.getlist(option):
                if value not in self.valid_options[option]:
                    raise Http404("{} for parameter {} is not valid.".format(value, option))
