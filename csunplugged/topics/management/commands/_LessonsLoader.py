"""Custom loader for loading lessons."""

from django.core.exceptions import ObjectDoesNotExist
from utils.BaseLoader import BaseLoader
from utils.language_utils import get_default_language, get_available_languages
from utils.model_translation_utils import populate_translations, mark_translation_availability
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.convert_heading_tree_to_dict import convert_heading_tree_to_dict
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from django.utils import translation


from topics.models import (
    ProgrammingChallenge,
    ProgrammingChallengeNumber,
    LearningOutcome,
    Resource,
    ResourceDescription,
    ClassroomResource
)

class LessonsLoader(TranslatableModelLoader):
    """Custom loader for loading lessons."""

    def __init__(self, topic, unit_plan, **kwargs):
        """Create the loader for loading lessons.

        Args:
            topic: Object of Topic model (Topic).
            unit_plan: Object of UnitPlan model (UnitPlan).
        """
        super().__init__(**kwargs)
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
        """Load the content for a single lesson.

        Raises:
            KeyNotFoundError: when no object can be found with the matching attribute.
            InvalidConfigValueError: when provided value is not valid.
            MissingRequiredFieldError: when a value for a required model field cannot be
                found in the config file.
        """
        lessons_structure = self.load_yaml_file(self.structure_file_path)

        for (lesson_slug, lesson_structure) in lessons_structure.items():


            if lesson_structure is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["number"],
                    "Lesson"
                )

            lesson_translations = {} # Language, then fields, then values

            content_filename = "{}.md".format(lesson_slug)
            content_translations = self.get_markdown_translations(content_filename)
            for language, content in content_translations.items():
                lesson_translations[language] = dict()
                lesson_translations[language]['content'] = content.html_string
                lesson_translations[language]['name'] = content.title
                if content.heading_tree:
                    heading_tree = convert_heading_tree_to_dict(content.heading_tree)
                    lesson_translations[language]['heading_tree'] = heading_tree

            if "computational-thinking-links" in lesson_structure:
                filename = lesson_structure["computational-thinking-links"]
                ct_links_translations = self.get_markdown_translations(
                    filename,
                    heading_required=False,
                    remove_title=False,
                )
                for language, content in ct_links_translations.items():
                    lesson_translations[language]['computational_thinking_links'] = content.html_string

            if "programming-challenges-description" in lesson_structure:
                filename = lesson_structure["programming-challenges-description"]
                pcd_translations = self.get_markdown_translations(
                    filename,
                    heading_required=False,
                    remove_title=False,
                )
                for language, content in pcd_translations.items():
                    lesson_translations[language]['programming_challenges_description'] = content.html_string

            if "duration" in lesson_structure:
                lesson_duration = lesson_structure["duration"]
            else:
                lesson_duration = None

            lesson = self.topic.lessons.create(
                unit_plan=self.unit_plan,
                slug=lesson_slug,
                duration=lesson_duration,
            )
            # raise Exception(lesson_translations)
            self.populate_translations(lesson, lesson_translations)
            self.mark_translation_availability(lesson, required_fields=['name', 'content'])
            # raise Exception(lesson.name)

            lesson.save()

            # Add programming challenges
            if "programming-challenges" in lesson_structure:
                programming_challenge_slugs = lesson_structure["programming-challenges"]
                if programming_challenge_slugs is not None:
                    # Check all slugs are valid
                    for programming_challenge_slug in programming_challenge_slugs:
                        try:
                            ProgrammingChallenge.objects.get(
                                slug=programming_challenge_slug,
                                topic=self.topic
                            )

                        except ObjectDoesNotExist:
                            raise KeyNotFoundError(
                                self.structure_file_path,
                                programming_challenge_slug,
                                "Programming Challenges"
                            )

                    # Store number of challenge in relationship with lesson.
                    # If three linked challenges have numbers 1.1, 4.2, and 4.5
                    # They will be stored as 1.1, 2.1, and 2.2 respectively.

                    # Order challenges for numbering.
                    programming_challenges = ProgrammingChallenge.objects.filter(
                        slug__in=programming_challenge_slugs,
                        topic=self.topic
                    ).order_by("challenge_set_number", "challenge_number")

                    # Setup variables for numbering.
                    display_set_number = 0
                    last_set_number = -1
                    display_number = 0
                    last_number = -1

                    # For each challenge, increment number variables if original
                    # numbers are different.
                    for programming_challenge in programming_challenges:
                        if programming_challenge.challenge_set_number > last_set_number:
                            display_set_number += 1
                            display_number = 0
                            last_number = -1
                        if programming_challenge.challenge_number > last_number:
                            display_number += 1
                        last_set_number = programming_challenge.challenge_set_number
                        last_number = programming_challenge.challenge_number

                        # Create and save relationship between lesson and
                        # challenge that contains challenge number.
                        relationship = ProgrammingChallengeNumber(
                            programming_challenge=programming_challenge,
                            lesson=lesson,
                            challenge_set_number=display_set_number,
                            challenge_number=display_number,
                        )
                        relationship.save()

            # Add learning outcomes
            if "learning-outcomes" in lesson_structure:
                learning_outcome_slugs = lesson_structure["learning-outcomes"]
                if learning_outcome_slugs is not None:
                    for learning_outcome_slug in learning_outcome_slugs:
                        try:
                            learning_outcome = LearningOutcome.objects.get(
                                slug=learning_outcome_slug
                            )
                            lesson.learning_outcomes.add(learning_outcome)
                        except ObjectDoesNotExist:
                            raise KeyNotFoundError(
                                self.structure_file_path,
                                learning_outcome_slug,
                                "Learning Outcomes"
                            )

            # Add classroom resources
            if "classroom-resources" in lesson_structure:
                classroom_resources_slugs = lesson_structure["classroom-resources"]
                if classroom_resources_slugs is not None:
                    for classroom_resources_slug in classroom_resources_slugs:
                        try:
                            classroom_resource = ClassroomResource.objects.get(
                                slug=classroom_resources_slug
                            )
                            lesson.classroom_resources.add(classroom_resource)
                        except:
                            raise KeyNotFoundError(
                                self.structure_file_path,
                                classroom_resources_slug,
                                "Classroom Resources"
                            )

            # Add generated resources
            if "generated-resources" in lesson_structure:
                resources = lesson_structure["generated-resources"]
                if resources is not None:
                    for (resource_slug, resource_data) in resources.items():
                        if resource_data is None:
                            raise MissingRequiredFieldError(
                                self.structure_file_path,
                                ["description"],
                                "Generated Resource"
                            )
                        try:
                            resource = Resource.objects.get(
                                slug=resource_slug
                            )
                        except ObjectDoesNotExist:
                            raise KeyNotFoundError(
                                self.structure_file_path,
                                resource_slug,
                                "Resources"
                            )
                        resource_description = resource_data.get("description", None)
                        if resource_description is None:
                            raise MissingRequiredFieldError(
                                self.structure_file_path,
                                ["description"],
                                "Generated Resource"
                            )

                        relationship = ResourceDescription(
                            resource=resource,
                            lesson=lesson,
                            description=resource_description
                        )
                        relationship.save()

            self.log("Added lesson: {}".format(lesson.__str__()), 2)
