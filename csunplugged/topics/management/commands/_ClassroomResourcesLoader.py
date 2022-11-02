"""Custom loader for loading curriculum areas."""

from django.db import transaction

from utils.TranslatableModelLoader import TranslatableModelLoader

from topics.models import ClassroomResource


class ClassroomResourcesLoader(TranslatableModelLoader):
    """Loader for curriculum area content."""

    @transaction.atomic
    def load(self):
        """Load the content for classroom resource.

        Raise:
            InvalidYAMLValueError: Description provided is not a string.
        """
        classroom_resources = self.load_yaml_file(self.structure_file_path)["classroom-resources"]
        classroom_resources_translations = self.get_yaml_translations(
            self.structure_filename,
            required_slugs=classroom_resources,
            required_fields=["description"]

        )

        for classroom_resource_slug in classroom_resources:
            translations = classroom_resources_translations.get(classroom_resource_slug, dict())
            new_resource, created = ClassroomResource.objects.update_or_create(
                slug=classroom_resource_slug,
            )
            self.populate_translations(new_resource, translations)
            self.mark_translation_availability(new_resource, required_fields=["description"])
            new_resource.save()

            if created:
                term = 'Created'
            else:
                term = 'Updated'
            self.log(f'{term} classroom resource: {new_resource.__str__()}')

        self.log("All classroom resources loaded!\n")
