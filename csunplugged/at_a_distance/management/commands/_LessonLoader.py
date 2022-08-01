"""Custom loader for loading an at a distance lesson."""

from django.db import transaction
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError
from utils.language_utils import (
    get_available_languages,
    get_default_language,
)
from at_a_distance.models import Lesson, SupportingResource
from at_a_distance.settings import (
    AT_A_DISTANCE_INTRODUCTION_FILENAME,
    AT_A_DISTANCE_SUPPORTING_RESOURCES_FILENAME,
)


class AtADistanceLessonLoader(TranslatableModelLoader):
    """Custom loader for loading an lesson."""

    def __init__(self, factory, lesson_data, **kwargs):
        """Create the loader for loading an activity.

        Args:
            factory: LoaderFactory object for creating loaders (LoaderFactory).
        """
        super().__init__(**kwargs)
        self.factory = factory
        self.lesson_slug = self.content_path
        self.lesson_data = lesson_data

    @transaction.atomic
    def load(self):
        """Load the content for an at a distance lesson.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching attribute.
        """
        lesson_translations = self.get_blank_translation_dictionary()

        try:
            order_number = self.lesson_data['order-number']
        except KeyError:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                [
                    "order-number",
                ],
                "Lesson"
            )

        # Suitability values
        suitability_options = [i[0] for i in Lesson.SUITABILITY_CHOICES]

        try:
            suitable_teaching_students = self.lesson_data['suitable-for-teaching-students']
        except KeyError:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                [
                    "suitable-for-teaching-students",
                ],
                "Lesson"
            )
        else:
            if suitable_teaching_students not in suitability_options:
                raise InvalidYAMLValueError(
                    self.structure_file_path,
                    "suitable-for-teaching-students",
                    suitability_options,
                )

        try:
            suitable_teaching_educators = self.lesson_data['suitable-for-teaching-educators']
        except KeyError:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                [
                    "suitable-for-teaching-educators",
                ],
                "Lesson"
            )
        else:
            if suitable_teaching_educators not in suitability_options:
                raise InvalidYAMLValueError(
                    self.structure_file_path,
                    "suitable-for-teaching-educators",
                    suitability_options,
                )

        # Introduction content
        content_translations = self.get_markdown_translations(AT_A_DISTANCE_INTRODUCTION_FILENAME)
        for language, content in content_translations.items():
            lesson_translations[language]['name'] = content.title
            lesson_translations[language]['introduction'] = content.html_string

        # Create or update lesson objects and save to the database
        lesson, created = Lesson.objects.update_or_create(
            slug=self.lesson_slug,
            defaults={
                'order_number': order_number,
                'suitable_for_teaching_students': suitable_teaching_students,
                'suitable_for_teaching_educators': suitable_teaching_educators,
            },
        )

        self.populate_translations(lesson, lesson_translations)
        self.mark_translation_availability(lesson, required_fields=['name', 'introduction'])
        lesson.save()

        # Supporting resources
        lesson.supporting_resources.all().delete()
        supporting_resources = self.lesson_data.get('supporting-resources')
        if supporting_resources:
            self.add_supporting_resource_translations(lesson)

        if created:
            term = 'Created'
        else:
            term = 'Updated'
        self.log(f'{term} At A Distance Lesson: {lesson}')

    def add_supporting_resource_translations(self, lesson):
        """Get dictionary of translations of supporting resources.

        Returns:
            Dictionary mapping language codes to HTML.

        Raises:
            CouldNotFindYAMLFileError: If the requested file could not be found
                in the /en directory tree
        """
        for language in get_available_languages():
            yaml_file_path = self.get_localised_file(
                language,
                AT_A_DISTANCE_SUPPORTING_RESOURCES_FILENAME,
            )
            try:
                supporting_resources = self.load_yaml_file(yaml_file_path)
            except CouldNotFindYAMLFileError:
                if language == get_default_language():
                    raise
            else:
                for (index, supporting_resource) in enumerate(supporting_resources):
                    SupportingResource.objects.create(
                        order_number=index,
                        text=supporting_resource['text'],
                        url=supporting_resource['url'],
                        language=language,
                        lesson=lesson,
                    )