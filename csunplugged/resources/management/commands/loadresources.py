from django.core.management.base import BaseCommand
from ._ResourcesLoader import ResourcesLoader


class Command(BaseCommand):
    help = 'Reads resource data and adds to database'

    def handle(self, *args, **options):
        """The function called when the loadresources command is given"""

        BASE_PATH = 'resources/content/{}'
        resource_structure_file = 'resources.yaml'

        ResourcesLoader(
            resource_structure_file,
            BASE_PATH
        ).load()
