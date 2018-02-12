"""Custom loader for loading Classic CS Unplugged pages."""

from urllib.parse import urljoin
from django.db import transaction
from django.urls import reverse
from utils.BaseLoader import BaseLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError
from classic.models import ClassicPage


class ClassicPagesLoader(BaseLoader):
    """Custom loader for loading Classic CS Unplugged pages."""

    @transaction.atomic
    def load(self):
        """Load Classic CS Unplugged pages.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        classic_pages = self.load_yaml_file(self.structure_file_path)

        for (slug, page_data) in classic_pages.items():
            try:
                name = page_data["name"]
                indexed = page_data["indexed"]
            except KeyError:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    [
                        "name",
                        "indexed",
                    ],
                    "Classic CS Unplugged page"
                )

            # Check indexed value is boolean
            if not isinstance(indexed, bool):
                raise InvalidYAMLValueError(
                    self.structure_file_path,
                    "indexed",
                    "'true' or 'false'"
                )

            redirect = page_data.get("redirect", None)
            if redirect and redirect.startswith("http"):
                redirect_url = redirect
            elif redirect:
                redirect_url = reverse(redirect)
            else:
                redirect_url = urljoin("https://classic.csunplugged.org/", slug)

            classic_page = ClassicPage(
                slug=slug,
                name=name,
                indexed=indexed,
                redirect=redirect_url,
            )

            self.log("Added Classic CS Unplugged page: {}".format(name))
        self.log("All Classic CS Unplugged pages loaded!\n")
