"""Module for the custom Django makeresources command."""

import os
import os.path
from urllib.parse import urlencode
from django.core.management.base import BaseCommand
from django.http.request import QueryDict
from django.conf import settings
from django.utils import translation
from resources.models import Resource
from resources.utils.get_resource_generator import get_resource_generator
from resources.utils.resource_valid_configurations import resource_valid_configurations
from resources.utils.resource_parameters import EnumResourceParameter


class Command(BaseCommand):
    """Required command class for the custom Django makestaticresources command."""

    help = "Creates static PDF files of resource combinations."

    def add_arguments(self, parser):
        """Add optional parameter to makeresources command."""
        parser.add_argument(
            "resource_slug",
            nargs="?",
            default=None,
            help="The resource slug to generate",
        )
        parser.add_argument(
            "resource_language",
            nargs="?",
            default=None,
            help="The language to generate the resource in",
        )

    def handle(self, *args, **options):
        """Automatically called when the makeresources command is given."""
        base_path = settings.RESOURCE_GENERATION_LOCATION

        if options["resource_slug"]:
            resources = [Resource.objects.get(slug=options["resource_slug"])]
        else:
            resources = Resource.objects.order_by("name")

        if options["resource_language"]:
            generation_languages = [options["resource_language"]]
        else:
            generation_languages = []
            for language_code, _ in settings.LANGUAGES:
                if language_code not in settings.INCONTEXT_L10N_PSEUDOLANGUAGES:
                    generation_languages.append(language_code)

        for resource in resources:
            print("Creating {}".format(resource.name))

            # TODO: Import repeated in next for loop, check alternatives
            empty_generator = get_resource_generator(resource.generator_module)
            if not all([isinstance(option, EnumResourceParameter)
                        for option in empty_generator.get_options().values()]):
                raise TypeError("Only EnumResourceParameters are supported for pre-generation")
            valid_options = {option.name: list(option.valid_values.keys())
                             for option in empty_generator.get_options().values()}
            combinations = resource_valid_configurations(valid_options)

            # TODO: Create PDFs in parallel

            # Create PDF for all possible combinations
            for combination in combinations:
                for language_code in generation_languages:
                    self.create_resource_pdf(resource, combination, language_code, base_path)

    def create_resource_pdf(self, resource, combination, language_code, base_path):
        """Create a given resource PDF.

        Args:
            resource (Resource): Resource to create.
            combination (dict): Specific option attributes for this resource.
            language_code (str): Code for language.
            base_path (str): Base path for outputting P
        """
        print("  - Creating {} PDF in '{}' with parameters '{}".format(resource.name, language_code, combination))
        with translation.override(language_code):
            if resource.copies:
                combination["copies"] = settings.RESOURCE_COPY_AMOUNT
            requested_options = QueryDict(urlencode(combination, doseq=True))
            generator = get_resource_generator(resource.generator_module, requested_options)
            (pdf_file, filename) = generator.pdf(resource.name)

            pdf_directory = os.path.join(base_path, resource.slug, language_code)
            if not os.path.exists(pdf_directory):
                os.makedirs(pdf_directory)

            filename = "{}.pdf".format(filename)
            pdf_file_output = open(os.path.join(pdf_directory, filename), "wb")
            pdf_file_output.write(pdf_file)
            pdf_file_output.close()
