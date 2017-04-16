import os.path
from django.db import transaction

from utils.BaseLoader import BaseLoader

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from resources.models import Resource


class ResourcesLoader(BaseLoader):
    """Loader for resources"""

    def __init__(self, structure_file, BASE_PATH):
        """Initiates the loader for resources

        Args:
            structure_file: file path (string)

        Raises:
            MissingRequiredFieldError:
        """
        super().__init__(BASE_PATH)
        self.structure_file = structure_file

    @transaction.atomic
    def load(self):
        """Call (single) ResourceLoader for each resource to load into the database
        """
        resources_structure = self.load_yaml_file(
            self.BASE_PATH.format(
                self.structure_file
            )
        )

        for (resource_slug, resource_structure) in resources_structure.items():
            try:
                resource_name = resource_structure['name']
                resource_template = resource_structure['webpage-template']
                resource_view = resource_structure['generation-view']
                resource_thumbnail = resource_structure['thumbnail-static-path']
            except:
                raise MissingRequiredFieldError()

            resource = Resource(
                slug=resource_slug,
                name=resource_name,
                webpage_template=resource_template,
                generation_view=resource_view,
                thumbnail_static_path=resource_thumbnail
            )
            resource.save()

            self.log('Added Resource: {}'.format(resource.name))

        self.print_load_log()
