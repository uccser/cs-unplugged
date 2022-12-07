"""Custom loader for loading Classic CS Unplugged pages."""

from urllib.parse import urljoin
from django.db import transaction
from utils.BaseLoader import BaseLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
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
            except (TypeError, KeyError):
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    [
                        "name",
                    ],
                    "Classic CS Unplugged page"
                )

            redirect_url = urljoin("https://classic.csunplugged.org/", slug)

            classic_page, created = ClassicPage.objects.update_or_create(
                slug=slug,
                name=name,
                redirect=redirect_url,
            )
            classic_page.save()

            if created:
                term = 'Created'
            else:
                term = 'Updated'
            self.log(f'{term} Classic CS Unplugged page: {name}')

        ClassicPage.objects.exclude(slug__in=classic_pages.keys()).delete();

        self.log("All Classic CS Unplugged pages loaded!\n")
