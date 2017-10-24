"""Custom loader for loading resources."""

from django.db import transaction
from django.http.request import QueryDict
from utils.BaseLoader import BaseLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.get_resource_generator import get_resource_generator
from resources.models import Resource


class ResourcesLoader(BaseLoader):
    """Custom loader for loading resources."""

    def __init__(self, structure_file, BASE_PATH):
        """Create the loader for loading resources.

        Args:
            structure_file: file path for structure YAML file (str).
            BASE_PATH: base file path (str).
        """
        super().__init__(BASE_PATH)
        self.structure_file = structure_file

    @transaction.atomic
    def load(self):
        """Load the content for resources.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        resources_structure = self.load_yaml_file(
            self.BASE_PATH.format(
                self.structure_file
            )
        )

        for (resource_slug, resource_structure) in resources_structure.items():
            try:
                resource_name = resource_structure["name"]
                resource_template = resource_structure["webpage-template"]
                generator_module = resource_structure["generator-module"]
                resource_thumbnail = resource_structure["thumbnail-static-path"]
                resource_copies = resource_structure["copies"]
            except KeyError:
                raise MissingRequiredFieldError()

            # Remove .py extension if given
            if generator_module.endswith(".py"):
                generator_module = generator_module[:-3]

            # Check module can be imported
            get_resource_generator(generator_module, QueryDict())

            resource = Resource(
                slug=resource_slug,
                name=resource_name,
                webpage_template=resource_template,
                generator_module=generator_module,
                thumbnail_static_path=resource_thumbnail,
                copies=resource_copies,
            )
            resource.save()

            self.log("Added Resource: {}".format(resource.name))
        self.log("All resources loaded!\n")
