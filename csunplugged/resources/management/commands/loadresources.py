from django.core.management.base import BaseCommand
from .ResourcesLoader import ResourcesLoader


class Command(BaseCommand):
    help = 'Reads resource data and adds to database'

    def handle(self, *args, **options):
        """The function called when the loadresources command is given"""
        
        self.BASE_PATH = 'resources/content/{}'  # TODO: Hardcoded for prototype
        resource_structure_file = self.BASE_PATH.format('resources.yaml')
        ResourcesLoader(resource_structure_file).load()