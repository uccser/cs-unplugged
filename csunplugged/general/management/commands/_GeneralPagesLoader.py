"""Custom loader for loading general pages."""

from django.db import transaction
from utils.BaseLoader import BaseLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError
from general.models import GeneralPage
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.urls import reverse, NoReverseMatch


class GeneralPagesLoader(BaseLoader):
    """Custom loader for loading general pages."""

    @transaction.atomic
    def load(self):
        """Load general pages.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        general_pages = self.load_yaml_file(self.structure_file_path)

        for (slug, page_data) in general_pages.items():
            try:
                name = page_data["name"]
                template = page_data["template"]
                url_name = page_data["url-name"]
            except (TypeError, KeyError):
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    [
                        "name",
                        "template",
                        "url-name",
                    ],
                    "General page"
                )

            # Check template is valid
            try:
                get_template(template)
            except TemplateDoesNotExist:
                raise InvalidYAMLValueError(
                    self.structure_file_path,
                    "template",
                    "A valid template file path"
                )

            # Check URL name is valid
            try:
                reverse(url_name)
            except NoReverseMatch:
                raise InvalidYAMLValueError(
                    self.structure_file_path,
                    "url-name",
                    "A URL name listed in 'csunplugged/general/urls.py'"
                )

            general_page, created = GeneralPage.objects.update_or_create(
                slug=slug,
                defaults={
                    'name': name,
                    'template': template,
                    'url_name': url_name,
                }
            )
            general_page.save()
            if created:
                term = 'Created'
            else:
                term = 'Updated'
            self.log(f'{term} general page: {name}')
        self.log("All general pages loaded!\n")
