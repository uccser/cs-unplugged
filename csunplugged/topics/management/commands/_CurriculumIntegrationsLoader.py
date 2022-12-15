"""Custom loader for loading curriculum integrations."""

from django.core.exceptions import ObjectDoesNotExist
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError
from topics.models import CurriculumArea, CurriculumIntegration, Lesson


class CurriculumIntegrationsLoader(TranslatableModelLoader):
    """Custom loader for loading curriculum integrations."""

    def __init__(self, topic, **kwargs):
        """Create the loader for loading curriculum integrations.

        Args:
            topic: Object of related topic model (Topic).
        """
        super().__init__(**kwargs)
        self.topic = topic

    def load(self):
        """Load the content for curriculum integrations.

        Raise:
            KeyNotFoundError: when no object can be found with the matching attribute.
            MissingRequiredFieldError: when a value for a required model field cannot be
                found in the config file.
        """
        structure = self.load_yaml_file(self.structure_file_path)

        current_number = 1
        for (integration_slug, integration_data) in structure.items():
            if integration_data is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["number", "curriculum-areas"],
                    "Curriculum Integration"
                )

            integration_translations = self.get_blank_translation_dictionary()

            content_filename = "{}.md".format(integration_slug)
            content_translations = self.get_markdown_translations(content_filename)
            for language, content in content_translations.items():
                integration_translations[language]["content"] = content.html_string
                integration_translations[language]["name"] = content.title

            integration_number = integration_data.get("number", None)

            integration_curriculum_areas = integration_data.get("curriculum-areas", None)
            if None in [integration_number, integration_curriculum_areas]:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["number", "curriculum-areas"],
                    "Curriculum Integration"
                )

            if integration_number != current_number:
                raise InvalidYAMLValueError(
                    self.structure_file_path,
                    "number",
                    "Curriculum integrations must be numbered sequentially starting from 1"
                )

            integration, created = self.topic.curriculum_integrations.update_or_create(
                number=integration_number,
                defaults={
                    "slug": integration_slug,
                }
            )
            self.populate_translations(integration, integration_translations)
            self.mark_translation_availability(integration, required_fields=["name", "content"])
            integration.save()

            # Add curriculum areas
            for curriculum_area_slug in integration_curriculum_areas:
                try:
                    curriculum_area = CurriculumArea.objects.get(
                        slug=curriculum_area_slug
                    )
                    if curriculum_area.children.exists():
                        raise InvalidYAMLValueError(
                            self.structure_file_path,
                            "curriculum-areas - value '{}' is invalid".format(curriculum_area_slug),
                            "Curriculum area with no children (parent curriculum areas are not allowed)"
                        )
                    else:
                        integration.curriculum_areas.add(curriculum_area)
                except ObjectDoesNotExist:
                    raise KeyNotFoundError(
                        self.structure_file_path,
                        curriculum_area_slug,
                        "Curriculum Areas"
                    )

            # Add prerequisite lessons
            if "prerequisite-lessons" in integration_data:
                prerequisite_lessons = integration_data["prerequisite-lessons"]
                if prerequisite_lessons is not None:
                    for lesson_slug in prerequisite_lessons:
                        try:
                            lesson = Lesson.objects.get(
                                topic__slug=self.topic.slug,
                                slug=lesson_slug,
                            )
                            integration.prerequisite_lessons.add(lesson)
                        except ObjectDoesNotExist:
                            raise KeyNotFoundError(
                                self.structure_file_path,
                                lesson_slug,
                                "Lessons"
                            )

            if created:
                term = 'Created'
            else:
                term = 'Updated'
            self.log(f'{term} curriculum integration: {integration.name}', 1)

            current_number += 1

        CurriculumIntegration.objects.filter(topic=self.topic).exclude(
            number__lt=current_number
        ).delete()
