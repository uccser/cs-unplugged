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
from multiprocessing.dummy import Pool, Lock
from sqlite3 import ProgrammingError as sqlite3_ProgrammingError

THREADS = 6
LOCK = Lock()


class Command(BaseCommand):
    """Required command class for the custom Django makestaticresources command."""

    help = "Creates static PDF files of resource combinations."

    def add_arguments(self, parser):
        """Add optional parameter to makeresources command."""
        parser.add_argument(
            "resource_name",
            nargs="?",
            default=None,
            help="The resource name to generate",
        )
        parser.add_argument(
            "resource_language",
            nargs="?",
            default=None,
            help="The language to generate the resource in",
        )

    def handle(self, *args, **options):
        """Automatically called when the makeresources command is given."""
        if options["resource_name"]:
            resources = [Resource.objects.get(name=options["resource_name"])]
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
            self.create_pdfs_for_resource(resource, generation_languages)

    def create_pdfs_for_resource(self, resource, generation_languages):
        """Create all PDFs for a given resource.

        Args:
            resource (Resource): The resource PDFs will be generated for
            generation_languages (list): All languages to generate PDFs in
        """
        base_path = settings.RESOURCE_GENERATION_LOCATION
        pool = Pool(THREADS)

        # TODO: Import repeated in next for loop, check alternatives
        empty_generator = get_resource_generator(resource.generator_module)
        if not all([isinstance(option, EnumResourceParameter)
                    for option in empty_generator.get_options().values()]):
            raise TypeError("Only EnumResourceParameters are supported for pre-generation")
        valid_options = {option.name: list(option.valid_values.keys())
                         for option in empty_generator.get_options().values()}
        combinations = resource_valid_configurations(valid_options)

        # Create parameter sets for all possible combinations of resource
        parameter_sets = []
        for combination in combinations:
            for language_code in generation_languages:
                parameter_sets.append([resource, combination, language_code, base_path])

        # Generate resources
        print("Creating {} PDFs with {} processes for '{}'...".format(
            len(parameter_sets), THREADS, resource.name)
            )
        try:
            pool.map(self.create_resource_pdf, parameter_sets)
        except sqlite3_ProgrammingError:
            print("Error using parallel processing, creating {} PDFs in series for '{}'...".format(
                len(parameter_sets), resource.name)
                )
            for parameter_set in parameter_sets:
                self.create_resource_pdf(parameter_set)

    def create_resource_pdf(self, parameter_set):
        """Create a given resource PDF.

        Args:
            parameter_set (list): A list of...
                resource (Resource): Resource to create.
                combination (dict): Specific option attributes for this resource.
                language_code (str): Code for language.
                base_path (str): Base path for outputting the resource
        """
        resource = parameter_set[0]
        combination = parameter_set[1]
        language_code = parameter_set[2]
        base_path = parameter_set[3]
        LOCK.acquire()
        print("  - Creating PDF in '{}':".format(language_code))
        for key in combination.keys():
            print("    - {}: {}".format(key, combination[key]))
        LOCK.release()
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
