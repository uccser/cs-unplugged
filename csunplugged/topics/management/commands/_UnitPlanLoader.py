"""Custom loader for loading unit plans."""

import os.path
from django.core.exceptions import ObjectDoesNotExist
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.convert_heading_tree_to_dict import convert_heading_tree_to_dict
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError


from topics.models import (
    Lesson,
    LessonNumber,
    AgeGroup,
)


class UnitPlanLoader(TranslatableModelLoader):
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

        unit_plan_translations = self.get_blank_translation_dictionary()

        content_filename = "{}.md".format(self.unit_plan_slug)
        content_translations = self.get_markdown_translations(content_filename)
        for language, content in content_translations.items():
            unit_plan_translations[language]["content"] = content.html_string
            unit_plan_translations[language]["name"] = content.title
            if content.heading_tree:
                heading_tree = convert_heading_tree_to_dict(content.heading_tree)
                unit_plan_translations[language]["heading_tree"] = heading_tree

        if "computational-thinking-links" in unit_plan_structure:
            ct_links_filename = unit_plan_structure["computational-thinking-links"]
            ct_links_translations = self.get_markdown_translations(
                ct_links_filename,
                heading_required=False,
                remove_title=False,
            )
            for language, content in ct_links_translations.items():
                unit_plan_translations[language]["computational_thinking_links"] = content.html_string

        unit_plan = self.topic.unit_plans.create(
            slug=self.unit_plan_slug,
            languages=list(content_translations.keys()),
        )

        self.populate_translations(unit_plan, unit_plan_translations)
        self.mark_translation_availability(unit_plan, required_fields=["name", "content"])

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
