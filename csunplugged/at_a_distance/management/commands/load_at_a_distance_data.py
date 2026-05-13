"""Module for the custom Django load_at_a_distance_data command."""

import os.path
from django.core.management.base import BaseCommand
from django.conf import settings
from utils.BaseLoader import BaseLoader
from utils.LoaderFactory import LoaderFactory
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError
from at_a_distance.models import Lesson


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
            "structure.yaml"
        )

        structure_file = base_loader.load_yaml_file(structure_file_path)

        if structure_file.get("lessons", None) is None:
            raise MissingRequiredFieldError(
                structure_file_path,
                ["lessons"],
                "Application Structure"
            )
        elif not isinstance(structure_file["lessons"], list):
            raise InvalidYAMLValueError(
                structure_file_path,
                ["lessons"],
                "list"
            )
        else:
            for lesson_number, lesson_slug in enumerate(structure_file["lessons"]):
                lesson_structure_file = f"{lesson_slug}.yaml"
                factory.create_at_a_distance_lesson_loader(
                    lesson_number,
                    base_path=base_path,
                    content_path=lesson_slug,
                    structure_filename=lesson_structure_file,
                ).load()

            _, results = Lesson.objects.exclude(slug__in=structure_file["lessons"]).delete()
            if results.get("at_a_distance", 0) > 0:
                print(f"Deleted {results['at_a_distance.Lesson']} lessons")
