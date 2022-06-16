"""Module for the custom Django load_at_a_distance_data command."""

import os.path
from django.core.management.base import BaseCommand
from django.conf import settings
from utils.BaseLoader import BaseLoader
from utils.LoaderFactory import LoaderFactory
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError


class Command(BaseCommand):
    """Required command class for the custom Django load_at_a_distance_data command."""

    help = "Loads load_at_a_distance_data content in database."

    def handle(self, *args, **options):
        """Automatically called when the load_at_a_distance_data command is given.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        factory = LoaderFactory()

        # Get structure and content files
        base_loader = BaseLoader()
        base_path = settings.AT_A_DISTANCE_CONTENT_BASE_PATH

        structure_file_path = os.path.join(
            base_path,
            base_loader.structure_dir,
            "lessons.yaml"
        )

        structure_data = base_loader.load_yaml_file(structure_file_path)

        for lesson_slug, lesson_data in structure_data.items():
            activity_structure_file = "{}.yaml".format(lesson_slug)
            factory.create_at_a_distance_lesson_loader(
                base_path=base_path,
                content_path=lesson_slug,
                structure_filename=activity_structure_file,
                lesson_data=lesson_data,
            ).load()
