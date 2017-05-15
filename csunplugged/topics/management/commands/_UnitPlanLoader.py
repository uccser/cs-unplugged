"""Custom loader for loading unit plans."""

import os.path
from utils.BaseLoader import BaseLoader

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError


class UnitPlanLoader(BaseLoader):
    """Custom loader for loading unit plans."""

    def __init__(self, factory, load_log, structure_file_path, topic, BASE_PATH):
        """Create the loader for loading unit plans.

        Args:
            factory: LoaderFactory object for creating loaders (LoaderFactory).
            load_log: List of log messages (list).
            structure_file_path: File path for structure YAML file (string).
            topic: Object of related topic model.
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH, load_log)
        self.factory = factory
        self.unit_plan_slug = os.path.split(structure_file_path)[0]
        self.structure_file_path = os.path.join(self.BASE_PATH, structure_file_path)
        self.BASE_PATH = os.path.join(self.BASE_PATH, self.unit_plan_slug)
        self.topic = topic

    def load(self):
        """Load the content for unit plans.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
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

        unit_plan = self.topic.topic_unit_plans.create(
            slug=self.unit_plan_slug,
            name=unit_plan_content.title,
            content=unit_plan_content.html_string,
        )
        unit_plan.save()

        self.log("Added Unit Plan: {}".format(unit_plan.name), 1)

        # Load the lessons for the unit plan

        # If there is nothing in the structure dictionary there
        # are obviously no lessons! Error!
        if unit_plan_structure is None:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ["(At least one lesson)"],
                "Unit Plan"
            )
        # Call the loader to save the lessons into the db
        lessons_structure = unit_plan_structure
        self.factory.create_lessons_loader(
            self.structure_file_path,
            self.load_log,
            lessons_structure,
            self.topic,
            unit_plan,
            self.BASE_PATH
        ).load()
