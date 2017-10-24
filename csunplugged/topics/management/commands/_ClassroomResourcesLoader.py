"""Custom loader for loading curriculum areas."""

from django.db import transaction

from utils.BaseLoader import BaseLoader
from utils.errors.InvalidConfigValueError import InvalidConfigValueError

from topics.models import ClassroomResource


class ClassroomResourcesLoader(BaseLoader):
    """Loader for curriculum area content."""

    def __init__(self, **kwargs):
        """Create the loader for loading curriculum areas."""
        super().__init__(**kwargs)

    @transaction.atomic
    def load(self):
        """Load the content for classroom resource.

        Raise:
            InvalidConfigValueError: Description provided is not a string.
        """
        classroom_resources_structure = self.load_yaml_file(self.structure_file_path)

        for (classroom_resource_slug, classroom_resource_description) in classroom_resources_structure.items():

            if not isinstance(classroom_resource_description, str):
                raise InvalidConfigValueError(
                    self.structure_file_path,
                    classroom_resource_slug,
                    "A string describing the classroom resource."
                )
            new_resource = ClassroomResource(
                slug=classroom_resource_slug,
                description=classroom_resource_description,
            )
            new_resource.save()

            self.log("Added classroom resource: {}".format(new_resource.__str__()))

        self.log("All classroom resources loaded!\n")
