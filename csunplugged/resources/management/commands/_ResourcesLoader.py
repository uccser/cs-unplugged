"""Custom loader for loading resources."""

import os.path
from django.db import transaction
from django.http.request import QueryDict
from utils.BaseLoader import BaseLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.InvalidConfigValueError import InvalidConfigValueError
from resources.utils.get_resource_generator import get_resource_generator
from resources.models import Resource
from django.contrib.staticfiles import finders


class ResourcesLoader(BaseLoader):
    """Custom loader for loading resources."""

    def __init__(self, **kwargs):
        """Create the loader for loading resources."""
        super().__init__(**kwargs)

    @transaction.atomic
    def load(self):
        """Load the content for resources.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        resources_structure = self.load_yaml_file(self.structure_file_path)

        for (resource_slug, resource_structure) in resources_structure.items():
            try:
                resource_name = resource_structure["name"]
                resource_template = resource_structure["webpage-template"]
                generator_module = resource_structure["generator-module"]
                resource_thumbnail = resource_structure["thumbnail-static-path"]
                resource_copies = resource_structure["copies"]
            except KeyError:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    [
                        "name",
                        "webpage-template",
                        "generator-module",
                        "thumbnail-static-path",
                        "copies"
                    ],
                    "Resource"
                )

            # Check resource template file exists
            open(os.path.join("templates", resource_template), encoding="UTF-8")

            # Remove .py extension if given
            if generator_module.endswith(".py"):
                generator_module = generator_module[:-3]

            # Check module can be imported
            get_resource_generator(generator_module, QueryDict())

            # Check thumbnail exists
            if not finders.find(resource_thumbnail):
                error_text = "Thumbnail image {} for resource {} could not be found."
                raise FileNotFoundError(error_text.format(resource_thumbnail, resource_name))

            # Check copies value is boolean
            if not isinstance(resource_copies, bool):
                raise InvalidConfigValueError(
                    self.structure_file_path,
                    "copies",
                    "'true' or 'false'"
                )

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
