"""Custom loader for loading resources."""

from django.db import transaction

from utils.BaseLoader import BaseLoader

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from resources.models import Resource


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
                resource_view = resource_structure["generation-view"]
                resource_thumbnail = resource_structure["thumbnail-static-path"]
                resource_copies = resource_structure["copies"]
            except:
                raise MissingRequiredFieldError()

            resource = Resource(
                slug=resource_slug,
                name=resource_name,
                webpage_template=resource_template,
                generation_view=resource_view,
                thumbnail_static_path=resource_thumbnail,
                copies=resource_copies,
            )
            resource.save()

            self.log("Added Resource: {}".format(resource.name))
        self.log("All resources loaded!\n")
