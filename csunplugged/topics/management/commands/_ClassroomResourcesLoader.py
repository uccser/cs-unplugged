"""Custom loader for loading curriculum areas."""

from django.db import transaction

from utils.TranslatableModelLoader import TranslatableModelLoader

from topics.models import ClassroomResource


class ClassroomResourcesLoader(TranslatableModelLoader):
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
        classroom_resources = self.load_yaml_file(self.structure_file_path)['classroom-resources']
        classroom_resources_translations = self.get_yaml_translations(
            self.structure_filename,
            required_slugs=classroom_resources,
            required_fields=["description"]

        )

        for classroom_resource_slug in classroom_resources:
            translations = classroom_resources_translations.get(classroom_resource_slug, dict())
            new_resource = ClassroomResource(
                slug=classroom_resource_slug,
            )
            self.populate_translations(new_resource, translations)
            self.mark_translation_availability(new_resource, required_fields=['description'])
            new_resource.save()

            self.log("Added classroom resource: {}".format(new_resource.__str__()))

        self.log("All classroom resources loaded!\n")
