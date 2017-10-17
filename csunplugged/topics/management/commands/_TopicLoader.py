"""Custom loader for loading a topic."""

import os.path
from django.db import transaction

from utils.BaseLoader import BaseLoader
from utils.language_utils import get_available_languages, get_default_language
from utils.check_required_files import find_image_files

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError

from topics.models import Topic


class TopicLoader(BaseLoader):
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

        content_translations = {}
        other_resources_translations = {}

        # Convert the content to HTML
        for language in get_available_languages():
            try:
                topic_content = self.convert_md_file(
                    self.get_localised_file(language, "{}.md".format(self.topic_slug)),
                    self.structure_file_path
                )
                content_translations[language] = topic_content
            except CouldNotFindMarkdownFileError:
                if language == get_default_language():
                    raise

            # If other resources are given, convert to HTML
            if "other-resources" in topic_structure:
                topic_other_resources_file = topic_structure["other-resources"]
                if topic_other_resources_file is not None:
                    try:
                        other_resources_content = self.convert_md_file(
                            self.get_localised_file(language, topic_other_resources_file),
                            self.structure_file_path
                        )
                        other_resources_translations[language] = other_resources_content.html_string
                    except CouldNotFindMarkdownFileError:
                        if language == get_default_language():
                            raise

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
            name=topic_content.title,
            icon=topic_icon,
            languages=list(content_translations.keys()),
        )
        for language in content_translations:
            setattr(topic, "content_{}".format(language), content_translations[language].html_string)
            setattr(topic, "name_{}".format(language), content_translations[language].title)
        for language in other_resources_translations:
            setattr(topic, "other_resources_{}".format(language), other_resources_translations[language])
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
