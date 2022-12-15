"""Custom loader for loading resources."""

from django.db import transaction
from django.http.request import QueryDict
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError
from resources.utils.get_resource_generator import get_resource_generator
from resources.models import Resource


class ResourcesLoader(TranslatableModelLoader):
    """Custom loader for loading resources."""

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
                generator_module = resource_structure["generator-module"]
                resource_copies = resource_structure["copies"]
            except KeyError:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    [
                        "generator-module",
                        "copies"
                    ],
                    "Resource"
                )
            resource_translations = self.get_blank_translation_dictionary()
            content_filename = "{}.md".format(resource_slug)
            content_translations = self.get_markdown_translations(content_filename)
            for language, content in content_translations.items():
                resource_translations[language]["content"] = content.html_string
                resource_translations[language]["name"] = content.title

            # Remove .py extension if given
            if generator_module.endswith(".py"):
                generator_module = generator_module[:-3]

            # Check module can be imported
            get_resource_generator(generator_module, QueryDict())

            # Check copies value is boolean
            if not isinstance(resource_copies, bool):
                raise InvalidYAMLValueError(
                    self.structure_file_path,
                    "copies",
                    "'true' or 'false'"
                )

            # Create or update lesson objects and save to the database
            resource, created = Resource.objects.update_or_create(
                slug=resource_slug,
                defaults={
                    'generator_module': generator_module,
                    'copies': resource_copies,
                },
            )
            self.populate_translations(resource, resource_translations)
            self.mark_translation_availability(resource, required_fields=["name", "content"])
            resource.save()

            if created:
                term = 'Created'
            else:
                term = 'Updated'
            self.log(f'{term} Resource: {resource.name}')

        Resource.objects.exclude(slug__in=resources_structure.keys()).delete()

        self.log("All resources loaded!\n")
