"""Custom loader for loading unit plans."""

import os.path
from utils.BaseLoader import BaseLoader
from ._LessonsLoader import LessonsLoader


class UnitPlanLoader(BaseLoader):
    """Custom loader for loading unit plans."""

    def __init__(self, load_log, structure_file, topic, BASE_PATH):
        """Create the loader for loading unit plans.

        Args:
            load_log: List of log messages (list).
            structure_file: File path for structure YAML file (string).
            topic: Object of related topic model.
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH, load_log)
        self.structure_file = os.path.join(self.BASE_PATH, structure_file)
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file)[0])
        self.topic = topic

    def load(self):
        """Load the content for unit plans."""
        unit_plan_structure = self.load_yaml_file(self.structure_file)
        md_file = unit_plan_structure['md-file']
        unit_plan_content = self.convert_md_file(os.path.join(self.BASE_PATH, md_file))

        unit_plan = self.topic.topic_unit_plans.create(
            slug=unit_plan_structure['slug'],
            name=unit_plan_content.title,
            content=unit_plan_content.html_string,
        )
        unit_plan.save()

        self.log('Added Unit Plan: {}'.format(unit_plan.name), 1)

        lessons_structure = unit_plan_structure['lessons']
        LessonsLoader(
            self.load_log,
            lessons_structure,
            self.topic,
            unit_plan,
            self.BASE_PATH
        ).load()
