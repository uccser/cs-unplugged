"""Module for the custom Django makeresourcethumbnails command."""

import os
import os.path
from urllib.parse import urlencode
from tqdm import tqdm
from django.core.management.base import BaseCommand
from django.http.request import QueryDict
from resources.models import Resource
from resources.utils.get_resource_generator import get_resource_generator
from resources.utils.resource_valid_test_configurations import resource_valid_test_configurations
from utils.bool_to_yes_no import bool_to_yes_no

BASE_PATH_TEMPLATE = "build/img/resources/{resource}/thumbnails/"


class Command(BaseCommand):
    """Required command class for the custom Django makeresourcethumbnails command."""

    help = "Creates thumbnail images of resource combinations."

    def handle(self, *args, **options):
        """Automatically called when makeresourcethumbnails command is given."""
        resources = Resource.objects.order_by("name")

        for resource in resources:
            base_path = BASE_PATH_TEMPLATE.format(resource=resource.slug)
            if not os.path.exists(base_path):
                os.makedirs(base_path)

            # TODO: Import repeated in next for loop, check alternatives
            empty_generator = get_resource_generator(resource.generator_module)
            combinations = resource_valid_test_configurations(
                empty_generator.valid_options,
                header_text=False
            )

            # Create thumbnail for all possible combinations
            print("Creating thumbnails for {}".format(resource.name))
            progress_bar = tqdm(combinations, ascii=True)

            for combination in progress_bar:
                requested_options = QueryDict(urlencode(combination, doseq=True))
                generator = get_resource_generator(resource.generator_module, requested_options)

                filename = resource.slug + "-"
                for (key, value) in sorted(combination.items()):
                    filename += "{}-{}-".format(key, bool_to_yes_no(value))
                filename = "{}.png".format(filename[:-1])
                thumbnail_file_path = os.path.join(base_path, filename)

                generator.save_thumbnail(resource.name, thumbnail_file_path)
