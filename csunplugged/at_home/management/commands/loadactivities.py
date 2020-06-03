"""Module for the custom Django loadactivities command."""

import os.path
from django.core.management.base import BaseCommand
from django.conf import settings
from utils.BaseLoader import BaseLoader
from utils.LoaderFactory import LoaderFactory
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError


class Command(BaseCommand):
    """Required command class for the custom Django loadactivities command."""

    help = "Stores content in database."

    def add_arguments(self, parser):
        """Add optional parameter to updatedata command."""
        parser.add_argument(
            "--lite-load",
            action="store_true",
            dest="lite_load",
            help="Perform lite load (only load key content)",
        )

    def handle(self, *args, **options):
        """Automatically called when the loadactivities command is given.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        lite_load = options.get("lite_load")
        factory = LoaderFactory()

        # Get structure and content files
        base_loader = BaseLoader()
        base_path = settings.ACTIVITIES_CONTENT_BASE_PATH

        structure_file_path = os.path.join(
            base_path,
            base_loader.structure_dir,
            "activities.yaml"
        )

        structure_file = base_loader.load_yaml_file(structure_file_path)

        if structure_file.get("activities", None) is None or not isinstance(structure_file["activities"], dict):
            raise MissingRequiredFieldError(
                structure_file_path,
                ["activities"],
                "At Home"
            )
        else:
            for activity_slug, activity_data in structure_file["activities"].items():
                activity_path = activity_slug
                activity_structure_file = "{}.yaml".format(activity_slug)
                factory.create_activity_loader(
                    base_path=base_path,
                    content_path=activity_path,
                    structure_filename=activity_structure_file,
                    lite_loader=lite_load,
                    activity_data=activity_data,
                ).load()
