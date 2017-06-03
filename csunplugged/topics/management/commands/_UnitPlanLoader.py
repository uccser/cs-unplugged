"""Custom loader for loading unit plans."""

import os.path
from utils.BaseLoader import BaseLoader
from utils.convert_heading_tree_to_dict import convert_heading_tree_to_dict
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError

from topics.models import (
    Lesson,
    AgeRange
)


class UnitPlanLoader(BaseLoader):
    """Custom loader for loading unit plans."""

    def __init__(self, factory, structure_file_path, topic, BASE_PATH):
        """Create the loader for loading unit plans.

        Args:
            factory: LoaderFactory object for creating loaders (LoaderFactory).
            structure_file_path: File path for structure YAML file (string).
            topic: Object of related topic model.
            BASE_PATH: Base file path (string).
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

        unit_plan = self.topic.topic_unit_plans.create(
            slug=self.unit_plan_slug,
            name=unit_plan_content.title,
            content=unit_plan_content.html_string,
            heading_tree=heading_tree,
        )
        unit_plan.save()

        self.log("Added unit plan: {}".format(unit_plan.name), 1)

        # Load the lessons for the unit plan

        # If there is nothing in the structure dictionary there
        # are obviously no lessons! Error!
        if unit_plan_structure is None:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ["(At least one lesson)"],
                "Unit Plan"
            )
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

        # Create AgeRange and assign to lessons
        age_groups = unit_plan_structure.get("age-groups", None)
        if age_groups is None:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ["lessons", "age-groups"],
                "Unit Plan"
            )

        for age_group in age_groups:

            for age_range in age_group:  # single entry in the dictionary, so first (and only) key is age group
                min_age, max_age = age_range.split('-')

            new_age_range = AgeRange(
                age_range=(int(min_age), int(max_age))
            )
            new_age_range.save()

            for lesson_slug in age_group[age_range]:
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
                lesson.age_range.add(new_age_range)
