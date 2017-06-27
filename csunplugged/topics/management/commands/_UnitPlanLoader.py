"""Custom loader for loading unit plans."""

import os.path
from utils.BaseLoader import BaseLoader
from utils.convert_heading_tree_to_dict import convert_heading_tree_to_dict
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError

from topics.models import (
    Lesson,
    LessonNumber,
    AgeGroup,
)


class UnitPlanLoader(BaseLoader):
    """Custom loader for loading unit plans."""

    def __init__(self, factory, structure_file_path, topic, BASE_PATH):
        """Create the loader for loading unit plans.

        Args:
            factory: LoaderFactory object for creating loaders (LoaderFactory).
            structure_file_path: File path for structure YAML file (str).
            topic: Object of related topic model (Topic).
            BASE_PATH: Base file path (str).
        """
        super().__init__(BASE_PATH)
        self.factory = factory
        self.unit_plan_slug = os.path.split(structure_file_path)[0]
        self.structure_file_path = os.path.join(self.BASE_PATH, structure_file_path)
        self.BASE_PATH = os.path.join(self.BASE_PATH, self.unit_plan_slug)
        self.topic = topic

    def load(self):
        """Load the content for unit plans.

        Raise:
            KeyNotFoundError: when no object can be found with the matching attribute.
            MissingRequiredFieldError: when a value for a required model field cannot
                be found in the config file.
        """
        unit_plan_structure = self.load_yaml_file(self.structure_file_path)

        # Convert the content to HTML
        unit_plan_content = self.convert_md_file(
            os.path.join(
                self.BASE_PATH,
                "{}.md".format(self.unit_plan_slug)
            ),
            self.structure_file_path
        )

        heading_tree = None
        if unit_plan_content.heading_tree:
            heading_tree = convert_heading_tree_to_dict(unit_plan_content.heading_tree)

        if "computational-thinking-links" in unit_plan_structure:
            file_name = unit_plan_structure["computational-thinking-links"]
            file_path = os.path.join(
                self.BASE_PATH,
                file_name
            )
            ct_links_content = self.convert_md_file(
                file_path,
                self.structure_file_path,
                heading_required=False,
                remove_title=False,
            )
            ct_links = ct_links_content.html_string
        else:
            ct_links = None

        unit_plan = self.topic.unit_plans.create(
            slug=self.unit_plan_slug,
            name=unit_plan_content.title,
            content=unit_plan_content.html_string,
            heading_tree=heading_tree,
            computational_thinking_links=ct_links,
        )
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
        lessons_structure_file_path = os.path.join(self.BASE_PATH, lessons_yaml)

        # Call the loader to save the lessons into the db
        self.factory.create_lessons_loader(
            lessons_structure_file_path,
            self.topic,
            unit_plan,
            self.BASE_PATH
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
            except:
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
                except:
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
