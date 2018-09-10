"""Module for the custom Django loadgeneralpages command."""

from django.core.management.base import BaseCommand
from django.conf import settings
from utils.LoaderFactory import LoaderFactory


class Command(BaseCommand):
    """Required command class for the custom loadgeneralpages command."""

    help = "Reads general pages and adds these to database"

    def handle(self, *args, **options):
        """Automatically called when the loadgeneralpages command is given."""
        base_path = settings.GENERAL_PAGES_CONTENT_BASE_PATH
        general_pages_structure_file = "general-pages.yaml"
        factory = LoaderFactory()
        factory.create_general_pages_loader(
            structure_filename=general_pages_structure_file,
            base_path=base_path
        ).load()
