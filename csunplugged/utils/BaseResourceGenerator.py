"""Class for generator for a resource."""

from django.http import Http404
from abc import ABC, abstractmethod
from utils.str_to_bool import str_to_bool
from copy import deepcopy


class BaseResourceGenerator(ABC):
    """Class for generator for a resource."""

    default_valid_options = {
        "paper_size": ["a4", "letter"]
    }
    additional_valid_options = dict()

    def __init__(self, requested_options=None):
        """Construct BaseResourceGenerator instance.

        Args:
            requested_options: QueryDict of requested_options (QueryDict).
        """
        # Use deepcopy to avoid successive generators from sharing the same
        # valid_options dictionary.
        self.valid_options = deepcopy(BaseResourceGenerator.default_valid_options)
        self.valid_options.update(self.additional_valid_options)
        if requested_options:
            self.requested_options = self.process_requested_options(requested_options)

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

    def process_requested_options(self, requested_options):
        """Convert requested options to usable types.

        Method does the following:
        - Update all values through str_to_bool utility function.
        - Raises 404 error is requested option cannot be found.
        - Raises 404 is option given with invalid value.

        Returns:
            QueryDict of converted requested options (QueryDict).
        """
        requested_options = requested_options.copy()
        for option in self.valid_options.keys():
            values = requested_options.getlist(option)
            if not values:
                raise Http404("{} parameter not specified.".format(option))
            for (i, value) in enumerate(values):
                update_value = str_to_bool(value)
                if update_value not in self.valid_options[option]:
                    raise Http404("{} for parameter {} is not valid.".format(update_value, option))
                values[i] = update_value
            requested_options.setlist(option, values)
        return requested_options
