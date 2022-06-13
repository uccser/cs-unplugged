"""Custom loader for loading a topic."""

import os.path
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.check_required_files import find_image_files
from utils.convert_heading_tree_to_dict import convert_heading_tree_to_dict
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from topics.models import (
    Topic,
    Lesson,
    LessonNumber,
    AgeGroup,
)


class TopicLoader(TranslatableModelLoader):
    """Custom loader for loading a topic."""

    def __init__(self, factory, **kwargs):
        """Create the loader for loading a topic.

        Args:
            factory: LoaderFactory object for creating loaders (LoaderFactory).
        """
        super().__init__(**kwargs)
        self.factory = factory
        self.topic_slug = self.content_path

    @transaction.atomic
    def load(self):
        """Load the content for a topic.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        topic_structure = self.load_yaml_file(self.structure_file_path)

        topic_translations = self.get_blank_translation_dictionary()

        content_filename = "{}.md".format(self.topic_slug)
        content_translations = self.get_markdown_translations(content_filename)
        for language, content in content_translations.items():
            topic_translations[language]["name"] = content.title
            topic_translations[language]["content"] = content.html_string

        whats_it_all_about_translations = self.get_markdown_translations(
            'whats-it-all-about.md',
            heading_required=False,
            remove_title=True,
        )
        for language, content in whats_it_all_about_translations.items():
            topic_translations[language]["whats_it_all_about"] = content.html_string
            if content.heading_tree:
                heading_tree = convert_heading_tree_to_dict(content.heading_tree)
                topic_translations[language]["whats_it_all_about_heading_tree"] = heading_tree

        if "computational-thinking-links" in topic_structure:
            ct_links_filename = topic_structure["computational-thinking-links"]
            ct_links_translations = self.get_markdown_translations(
                ct_links_filename,
                heading_required=False,
                remove_title=False,
            )
            for language, content in ct_links_translations.items():
                topic_translations[language]["computational_thinking_links"] = content.html_string

        if "other-resources" in topic_structure and topic_structure["other-resources"] is not None:
            other_resources_filename = topic_structure["other-resources"]
            other_resources_translations = self.get_markdown_translations(other_resources_filename)
            for language, content in other_resources_translations.items():
                topic_translations[language]["other_resources"] = content.html_string

        # Check if icon is given
        if "icon" in topic_structure:
            topic_icon = topic_structure["icon"]
            if topic_icon is not None:
                find_image_files([topic_icon], self.structure_file_path)
            else:
                topic_icon = None
        else:
            topic_icon = None

        # Create Topic object and save to the database
        topic = Topic(
            slug=self.topic_slug,
            icon=topic_icon,
        )

        self.populate_translations(topic, topic_translations)
        self.mark_translation_availability(
            topic,
            required_fields=[
                "name",
                "content",
            ]
        )
        topic.save()

        self.log("Added Topic: {}".format(topic.name))

        # Load programming challenges
        if "programming-challenges" in topic_structure and not self.lite_loader:
            programming_challenges_structure_file_path = topic_structure["programming-challenges"]
            if programming_challenges_structure_file_path is not None:
                programming_challenges_path, structure_filename = os.path.split(
                    programming_challenges_structure_file_path
                )
                self.factory.create_programming_challenges_loader(
                    topic,
                    base_path=self.base_path,
                    content_path=os.path.join(self.content_path, programming_challenges_path),
                    structure_filename=structure_filename
                ).load()

        # Get path to lesson yaml
        lessons_yaml = topic_structure.get("lessons", None)
        if lessons_yaml is None:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ["lessons", "age-groups"],
                "Topic"
            )

        lesson_path, lesson_structure_file = os.path.split(lessons_yaml)

        # Call the loader to save the lessons into the db
        self.factory.create_lessons_loader(
            topic,
            content_path=os.path.join(self.content_path, lesson_path),
            structure_filename=lesson_structure_file,
            base_path=self.base_path,
            lite_loader=self.lite_loader,
        ).load()

        # Create AgeGroup and assign to lessons
        age_groups = topic_structure.get("age-groups", None)
        if age_groups is None:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ["lessons", "age-groups"],
                "Unit Plan"
            )

        for (age_group_slug, age_group_data) in age_groups.items():

            try:
                age_group = AgeGroup.objects.get(
                    slug=age_group_slug
                )
            except ObjectDoesNotExist:
                raise KeyNotFoundError(
                    self.structure_file_path,
                    age_group_slug,
                    "Age Range"
                )

            if age_group_data is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["lesson keys"],
                    "Unit Plan"
                )

            for (lesson_slug, lesson_data) in age_group_data.items():
                try:
                    lesson = Lesson.objects.get(
                        slug=lesson_slug
                    )
                except ObjectDoesNotExist:
                    raise KeyNotFoundError(
                        self.structure_file_path,
                        lesson_slug,
                        "Lesson"
                    )

                if lesson_data is None or lesson_data.get("number", None) is None:
                    raise MissingRequiredFieldError(
                        self.structure_file_path,
                        ["number"],
                        "Unit Plan"
                    )
                else:
                    lesson_number = lesson_data.get("number", None)

                relationship = LessonNumber(
                    age_group=age_group,
                    lesson=lesson,
                    number=lesson_number,
                )
                relationship.save()

        if "curriculum-integrations" in topic_structure:
            curriculum_integrations_structure_file_path = topic_structure["curriculum-integrations"]
            if curriculum_integrations_structure_file_path is not None:
                curriculum_integrations_path, structure_filename = os.path.split(
                    curriculum_integrations_structure_file_path
                )
                self.factory.create_curriculum_integrations_loader(
                    topic,
                    base_path=self.base_path,
                    content_path=os.path.join(self.content_path, curriculum_integrations_path),
                    structure_filename=structure_filename
                ).load()

        self.log("")
