"""Custom loader for loading unit plans."""

import os.path
from django.core.exceptions import ObjectDoesNotExist
from utils.BaseLoader import BaseLoader
from utils.language_utils import get_available_languages, get_default_language
from utils.convert_heading_tree_to_dict import convert_heading_tree_to_dict
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError


from topics.models import (
    Lesson,
    LessonNumber,
    AgeGroup,
)


class UnitPlanLoader(BaseLoader):
    """Custom loader for loading unit plans."""

    def __init__(self, factory, topic, **kwargs):
        """Create the loader for loading unit plans.

        Args:
            factory: LoaderFactory object for creating loaders (LoaderFactory).
            topic: Object of related topic model (Topic).
        """
        super().__init__(**kwargs)
        self.factory = factory
        self.unit_plan_slug = os.path.splitext(self.structure_filename)[0]
        self.topic = topic

    def load(self):
        """Load the content for unit plans.

        Raise:
            KeyNotFoundError: when no object can be found with the matching attribute.
            MissingRequiredFieldError: when a value for a required model field cannot
                be found in the config file.
        """
        unit_plan_structure = self.load_yaml_file(self.structure_file_path)
        content_translations = {}
        ct_links_translations = {}
        heading_tree_translations = {}

        for language in get_available_languages():
            try:
                # Convert the content to HTML
                unit_plan_content = self.convert_md_file(
                    self.get_localised_file(language, "{}.md".format(self.unit_plan_slug)),
                    self.structure_file_path
                )
                content_translations[language] = unit_plan_content
            except CouldNotFindMarkdownFileError:
                if language == get_default_language():
                    raise

            if unit_plan_content.heading_tree:
                heading_tree = convert_heading_tree_to_dict(unit_plan_content.heading_tree)
                heading_tree_translations[language] = heading_tree

            if "computational-thinking-links" in unit_plan_structure:
                filename = unit_plan_structure["computational-thinking-links"]
                file_path = self.get_localised_file(language, filename)
                try:
                    ct_links_content = self.convert_md_file(
                        file_path,
                        self.structure_file_path,
                        heading_required=False,
                        remove_title=False,
                    )
                    ct_links_translations[language] = ct_links_content.html_string
                except CouldNotFindMarkdownFileError:
                    if language == get_default_language():
                        raise

        unit_plan = self.topic.unit_plans.create(
            slug=self.unit_plan_slug,
            languages=list(content_translations.keys()),
        )
        for language in content_translations:
            setattr(unit_plan, "content_{}".format(language), content_translations[language].html_string)
            setattr(unit_plan, "name_{}".format(language), content_translations[language].title)
            if unit_plan_content.heading_tree:
                heading_tree = convert_heading_tree_to_dict(content_translations[language].heading_tree)
                setattr(unit_plan, "heading_tree_{}".format(language), heading_tree)
        for language in ct_links_translations:
            setattr(unit_plan, "computational_thinking_links_{}".format(language), ct_links_translations[language])
        for language in heading_tree_translations:
            setattr(unit_plan, "heading_tree_{}".format(language), heading_tree_translations[language])

        unit_plan.save()

        self.log("Added unit plan: {}".format(unit_plan.name), 1)

        # Load the lessons for the unit plan
        # Get path to lesson yaml
        lessons_yaml = unit_plan_structure.get("lessons", None)
        if lessons_yaml is None:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ["lessons", "age-groups"],
                "Unit Plan"
            )

        lesson_path, lesson_structure_file = os.path.split(lessons_yaml)

        # Call the loader to save the lessons into the db
        self.factory.create_lessons_loader(
            self.topic,
            unit_plan,
            content_path=os.path.join(self.content_path, lesson_path),
            structure_filename=lesson_structure_file,
            base_path=self.base_path,

        ).load()

        # Create AgeGroup and assign to lessons
        age_groups = unit_plan_structure.get("age-groups", None)
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
