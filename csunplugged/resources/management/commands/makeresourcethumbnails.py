"""Module for the custom Django makeresourcethumbnails command."""

import os
import os.path
from urllib.parse import urlencode
from tqdm import tqdm
from django.conf import settings
from django.core.management.base import BaseCommand
from django.http.request import QueryDict
from django.utils import translation
from resources.models import Resource
from resources.utils.get_resource_generator import get_resource_generator
from resources.utils.resource_valid_configurations import resource_valid_configurations
from resources.utils.resource_parameters import EnumResourceParameter
from resources.utils.get_thumbnail import get_thumbnail_filename

BASE_PATH_TEMPLATE = "build/img/resources/{resource}/thumbnails/{language}"


class Command(BaseCommand):
    """Required command class for the custom Django makeresourcethumbnails command."""

    help = "Creates thumbnail images of resource combinations."

    def add_arguments(self, parser):
        """Add optional parameter to makeresourcethumbnails command."""
        parser.add_argument(
            "--all-languages",
            action="store_true",
            dest="all_languages",
            help="Generate thumbnails for all languages",
        )

    def handle(self, *args, **options):
        """Automatically called when makeresourcethumbnails command is given."""
        resources = Resource.objects.order_by("name")

        if options.get("all_languages"):
            languages = settings.DEFAULT_LANGUAGES
        else:
            languages = [("en", "")]
        for language_code, _ in languages:
            with translation.override(language_code):
                print("Creating thumbnails for language '{}''".format(language_code))
                for resource in resources:
                    base_path = BASE_PATH_TEMPLATE.format(
                        resource=resource.slug,
                        language=language_code
                    )
                    if not os.path.exists(base_path):
                        os.makedirs(base_path)

                    # TODO: Import repeated in next for loop, check alternatives
                    empty_generator = get_resource_generator(resource.generator_module)

                    if not all([isinstance(option, EnumResourceParameter)
                                for option in empty_generator.get_options().values()]):
                        raise TypeError("Only EnumResourceParameters are supported for pre-generation")
                    valid_options = {option.name: list(option.valid_values.keys())
                                     for option in empty_generator.get_options().values()}
                    combinations = resource_valid_configurations(valid_options)

                    # Create thumbnail for all possible combinations
                    print("Creating thumbnails for {}".format(resource.name))
                    progress_bar = tqdm(combinations, ascii=True)

                    for combination in progress_bar:
                        requested_options = QueryDict(urlencode(combination, doseq=True))
                        generator = get_resource_generator(resource.generator_module, requested_options)
                        filename = get_thumbnail_filename(resource.slug, combination)
                        thumbnail_file_path = os.path.join(base_path, filename)
                        generator.save_thumbnail(resource.name, thumbnail_file_path)
