"""Class for generator for a resource."""

from abc import ABC, abstractmethod
from resources.utils.resize_encode_resource_images import resize_encode_resource_images
from utils.str_to_bool import str_to_bool
from utils.errors.QueryParameterMissingError import QueryParameterMissingError
from utils.errors.QueryParameterInvalidError import QueryParameterInvalidError
from utils.errors.ThumbnailPageNotFound import ThumbnailPageNotFound
from utils.errors.MoreThanOneThumbnailPageFound import MoreThanOneThumbnailPageFound
from copy import deepcopy
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.staticfiles import finders


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

        Args:
            requested_options: QueryDict of requested_options (QueryDict).

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
                raise QueryParameterMissingError(option)
            for (i, value) in enumerate(values):
                update_value = str_to_bool(value)
                if update_value not in self.valid_options[option]:
                    raise QueryParameterInvalidError(option, value)
                values[i] = update_value
            requested_options.setlist(option, values)
        return requested_options

    def generate_thumbnail(self, resource_name, path):
        """Return thumbnail for resource request.

        Args:
            resource_name: Name of the resource (str).
            path: The path to write the thumbnail to (str).

        Raises:
            ThumbnailPageNotFound: If resource with more than one page does
                                   not provide a thumbnail page.
            MoreThanOneThumbnailPageFound: If resource provides more than
                                           one page as the thumbnail.
        """
        from weasyprint import HTML, CSS

        thumbnail_data = self.data()
        if not isinstance(thumbnail_data, list):
            thumbnail_data = [thumbnail_data]

        if len(thumbnail_data) > 1:
            thumbnail_data = list(filter(lambda thumbnail_data: thumbnail_data.get("thumbnail"), thumbnail_data))

            if len(thumbnail_data) == 0:
                raise ThumbnailPageNotFound(self)
            elif len(thumbnail_data) > 1:
                raise MoreThanOneThumbnailPageFound(self)

        thumbnail_data = resize_encode_resource_images(self, thumbnail_data)
        context = dict()
        context["resource"] = resource_name
        context["paper_size"] = self.requested_options["paper_size"]
        context["all_data"] = [thumbnail_data]
        pdf_html = render_to_string("resources/base-resource-pdf.html", context)
        html = HTML(string=pdf_html, base_url=settings.BUILD_ROOT)
        css_file = finders.find("css/print-resource-pdf.css")
        css_string = open(css_file, encoding="UTF-8").read()
        base_css = CSS(string=css_string)
        thumbnail = html.write_png(stylesheets=[base_css], resolution=72)
        thumbnail_file = open(path, "wb")
        thumbnail_file.write(thumbnail)
        thumbnail_file.close()
