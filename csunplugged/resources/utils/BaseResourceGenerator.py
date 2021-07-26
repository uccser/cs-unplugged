"""Class for generator for a resource."""

import os.path
from abc import ABC, abstractmethod
from resources.utils.resize_encode_resource_images import resize_encode_resource_images
from utils.errors.ThumbnailPageNotFoundError import ThumbnailPageNotFoundError
from utils.errors.MoreThanOneThumbnailPageFoundError import MoreThanOneThumbnailPageFoundError
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from resources.utils.resource_parameters import (
    EnumResourceParameter,
    TextResourceParameter,
    IntegerResourceParameter,
)

PAPER_SIZE_VALUES = {
    "a4": _("A4"),
    "letter": _("US Letter"),
}


class BaseResourceGenerator(ABC):
    """Class for generator for a resource."""

    copies = False  # Default

    def __init__(self, requested_options=None):
        """Construct BaseResourceGenerator instance.

        Args:
            requested_options: QueryDict of requested_options (QueryDict).
        """
        self.options = self.get_options()
        self.options.update(self.get_local_options())
        if requested_options:
            self.process_requested_options(requested_options)

    @classmethod
    def get_options(cls):
        """Get options dictionary, including additional subclass options.

        Returns:
            Dictionary, of form {option name: ResourceParameter object, ...}
        """
        options = cls.get_additional_options()
        options.update({
            "paper_size": EnumResourceParameter(
                name="paper_size",
                description=_("Paper Size"),
                values=PAPER_SIZE_VALUES,
                default="a4"
            ),
        })
        return options

    @classmethod
    def get_option_defaults(cls):
        """Get dictionary of default option values.

        Returns:
            Dictionary of option IDs to default values.
        """
        defaults = dict()
        for key, values in cls.get_options().items():
            defaults[key] = values.default
        return defaults

    @classmethod
    def get_local_options(cls):
        """Get local options dictionary, including additional subclass local options.

        These options are only included when running locally.

        Returns:
            Dictionary, of form {option name: ResourceParameter object, ...}
        """
        local_options = cls.get_additional_local_options()
        local_options = {
            "header_text": TextResourceParameter(
                name="header_text",
                description=_("Header Text"),
                placeholder=_("Example School: Room Four"),
                required=False
            ),
        }
        if cls.copies:
            local_options.update({
                "copies":  IntegerResourceParameter(
                    name="copies",
                    description=_("Number of Copies"),
                    min_val=1,
                    max_val=50,
                    default=1,
                    required=False
                ),
            })
        return local_options

    @classmethod
    def get_additional_options(cls):
        """Return additional options, for use on subclass.

        Returns:
            Dictionary, of form {option name: ResourceParameter object, ...}
        """
        return {}

    @classmethod
    def get_additional_local_options(cls):
        """Return additional options, for use on subclass.

        Returns:
            Dictionary, of form {option name: ResourceParameter object, ...}
        """
        return {}

    @abstractmethod
    def data(self):
        """Abstract method to be implemented by subclasses."""
        raise NotImplementedError  # pragma: no cover

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            Text for subtitle (str).
        """
        return str(self.options["paper_size"].value)

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
        # requested_options = requested_options.copy()
        for option_name, option in self.options.items():
            values = requested_options.getlist(option_name)
            option.process_requested_values(values)

    def pdf(self, resource_name):
        """Return PDF for resource request.

        The PDF is returned (compared to the thumbnail which is directly saved)
        as the PDF may be either saved to the disk, or returned in a HTTP
        response.

        Args:
            resource_name: Name of the resource (str).

        Return:
            PDF file of resource.
        """
        # Only import weasyprint when required as production environment
        # does not have it installed.
        from weasyprint import HTML, CSS
        context = dict()
        context["resource"] = resource_name
        context["header_text"] = self.options["header_text"].value
        context["paper_size"] = self.options["paper_size"].value

        if self.copies:
            num_copies = self.options["copies"].value
        else:
            num_copies = 1
        context["all_data"] = []
        for copy in range(num_copies):
            copy_data = self.data()
            if not isinstance(copy_data, list):
                copy_data = [copy_data]
            copy_data = resize_encode_resource_images(
                self.options["paper_size"].value,
                copy_data
            )
            context["all_data"].append(copy_data)

        filename = "{} ({})".format(resource_name, self.subtitle)
        context["filename"] = filename

        pdf_html = render_to_string("resources/base-resource-pdf.html", context)
        html = HTML(string=pdf_html, base_url=settings.BUILD_ROOT)
        css_file = os.path.join(settings.STATIC_ROOT, "css/print-resource-pdf.css")
        css_string = open(css_file, encoding="UTF-8").read()
        base_css = CSS(string=css_string)
        return (html.write_pdf(stylesheets=[base_css]), filename)

    def save_thumbnail(self, resource_name, path):
        """Create thumbnail for resource request.

        Args:
            resource_name: Name of the resource (str).
            path: The path to write the thumbnail to (str).
        """
        thumbnail_data = self.generate_thumbnail()
        self.write_thumbnail(thumbnail_data, resource_name, path)

    def generate_thumbnail(self):
        """Create thumbnail for resource request.

        Raises:
            ThumbnailPageNotFoundError: If resource with more than one page does
                                   not provide a thumbnail page.
            MoreThanOneThumbnailPageFoundError: If resource provides more than
                                           one page as the thumbnail.

        Returns:
            Dictionary of thumbnail data.
        """
        thumbnail_data = self.data()
        if not isinstance(thumbnail_data, list):
            thumbnail_data = [thumbnail_data]

        if len(thumbnail_data) > 1:
            thumbnail_data = list(filter(lambda thumbnail_data: thumbnail_data.get("thumbnail"), thumbnail_data))

            if len(thumbnail_data) == 0:
                raise ThumbnailPageNotFoundError(self)
            elif len(thumbnail_data) > 1:
                raise MoreThanOneThumbnailPageFoundError(self)

        thumbnail_data = resize_encode_resource_images(
            self.options["paper_size"].value,
            thumbnail_data
        )
        return thumbnail_data[0]

    def write_thumbnail(self, thumbnail_data, resource_name, path):
        """Save generatered thumbnail.

        Args:
            thumbnail_data: Data of generated thumbnail.
            resource_name: Name of the resource (str).
            path: The path to write the thumbnail to (str).
        """
        # Only import weasyprint when required as production environment
        # does not have it installed.
        from weasyprint import HTML, CSS
        context = dict()
        context["resource"] = resource_name
        context["paper_size"] = self.options["paper_size"].value
        context["all_data"] = [[thumbnail_data]]
        pdf_html = render_to_string("resources/base-resource-pdf.html", context)
        html = HTML(string=pdf_html, base_url=settings.BUILD_ROOT)
        css_file = os.path.join(settings.STATIC_ROOT, "css/print-resource-pdf.css")
        css_string = open(css_file, encoding="UTF-8").read()
        base_css = CSS(string=css_string)
        thumbnail = html.write_png(stylesheets=[base_css], resolution=72)
        thumbnail_file = open(path, "wb")
        thumbnail_file.write(thumbnail)
        thumbnail_file.close()
