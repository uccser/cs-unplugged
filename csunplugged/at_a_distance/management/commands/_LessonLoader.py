"""Custom loader for loading an at a distance lesson."""

from django.db import transaction
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from at_a_distance.models import Lesson
from at_a_distance.settings import AT_A_DISTANCE_INTRODUCTION_FILENAME


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
                "Activity"
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
            },
        )

        self.populate_translations(lesson, lesson_translations)
        self.mark_translation_availability(lesson, required_fields=['name', 'introduction'])
        lesson.save()

        if created:
            term = 'Created'
        else:
            term = 'Updated'
        self.log(f'{term} At A Distance Lesson: {lesson}')
