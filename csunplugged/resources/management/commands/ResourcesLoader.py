from django.db import transaction
from utils.BaseLoader import BaseLoader
from resources.models import Resource


class ResourcesLoader(BaseLoader):
    """Loader for resources"""

    def __init__(self, structure_file):
        """Initiates the loader for resources

        Args:
            structure_file: file path (string)
        """
        super().__init__()
        self.structure_file = structure_file

    @transaction.atomic
    def load(self):
        """load the content for resources"""
        resources = self.load_yaml_file(self.structure_file)
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
