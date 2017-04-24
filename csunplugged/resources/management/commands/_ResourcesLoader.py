"""Custom loader for loading resources."""

from django.db import transaction
from utils.BaseLoader import BaseLoader
from resources.models import Resource


class ResourcesLoader(BaseLoader):
    """Custom loader for loading resources."""

    def __init__(self, structure_file, BASE_PATH):
        """Create the loader for loading resources.

        Args:
            structure_file: file path for structure YAML file (string)
            BASE_PATH: base file path (string)
        """
        super().__init__(BASE_PATH)
        self.structure_file = structure_file

    @transaction.atomic
    def load(self):
        """Load the content for resources."""
        resources = self.load_yaml_file(self.BASE_PATH.format(self.structure_file))
        for (resource_slug, resource_data) in resources.items():
            resource = Resource(
                slug=resource_slug,
                name=resource_data['name'],
                webpage_template=resource_data['webpage_template'],
                generation_view=resource_data['generation_view'],
                thumbnail_static_path=resource_data['thumbnail_static_path'],
            )
            resource.save()
            self.log('Added Resource: {}'.format(resource.name))

        self.print_load_log()
