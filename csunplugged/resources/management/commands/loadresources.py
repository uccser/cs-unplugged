from django.core.management.base import BaseCommand, CommandError
from resources.models import Resource
from django.db import transaction
import yaml
import os
import os.path
import sys

class Command(BaseCommand):
    help = 'Reads resource data and adds to database'

    def handle(self, *args, **options):
        """The function called when the loadresources command is given"""
        self.BASE_PATH = 'resources/content/' # TODO: Hardcoded for prototype
        self.load_log = []
        self.resource_list = self.read_yaml('resources.yaml')
        self.load_resources(self.resource_list)
        self.print_load_log()

    def read_yaml(self, filepath):
        path = os.path.join(self.BASE_PATH, filepath)
        structure_file = open(path, encoding='UTF-8').read()
        return yaml.load(structure_file)

    def print_load_log(self):
        for (log, indent) in self.load_log:
            self.stdout.write('{indent}{text}'.format(indent='  '*indent,text=log))
        self.stdout.write('\n')
        self.load_log = []

    @transaction.atomic
    def load_resources(self, resource_list):
        for (resource_slug, resource_data) in resource_list.items():
            resource = Resource(
                slug=resource_slug,
                name=resource_data['name'],
                folder=resource_data['folder'],
            )
            resource.save()
            self.load_log.append(('\nAdded Resource: {}'.format(resource.name), 0))
