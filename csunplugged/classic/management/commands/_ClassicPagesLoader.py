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
            except KeyError:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    [
                        "name",
                    ],
                    "Classic CS Unplugged page"
                )

            redirect_url = urljoin("https://classic.csunplugged.org/", slug)

            classic_page = ClassicPage(
                slug=slug,
                name=name,
                redirect=redirect_url,
            )
            classic_page.save()
            self.log("Added Classic CS Unplugged page: {}".format(name))
        self.log("All Classic CS Unplugged pages loaded!\n")
