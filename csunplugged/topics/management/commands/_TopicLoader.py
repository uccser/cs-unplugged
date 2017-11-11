"""Custom loader for loading a topic."""

import os.path
from django.db import transaction
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.check_required_files import find_image_files
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import Topic


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

        unit_plans = topic_structure.get("unit-plans", None)
        if unit_plans is None:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ["unit-plans"],
                "Topic"
            )

        topic_translations = self.get_blank_translation_dictionary()

        content_filename = "{}.md".format(self.topic_slug)
        content_translations = self.get_markdown_translations(content_filename)
        for language, content in content_translations.items():
            topic_translations[language]["content"] = content.html_string
            topic_translations[language]["name"] = content.title

        if "other-resources" in topic_structure:
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

        # Create topic objects and save to the db
        topic = Topic(
            slug=self.topic_slug,
            icon=topic_icon,
        )

        self.populate_translations(topic, topic_translations)
        self.mark_translation_availability(topic, required_fields=["name", "content"])
        topic.save()

        self.log("Added Topic: {}".format(topic.name))

        # Load programming challenges
        if "programming-challenges" in topic_structure:
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

        # Load unit plans
        for unit_plan_file_path in unit_plans:
            content_path, structure_filename = os.path.split(unit_plan_file_path)
            self.factory.create_unit_plan_loader(
                topic,
                base_path=self.base_path,
                content_path=os.path.join(self.content_path, content_path),
                structure_filename=structure_filename
            ).load()

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
