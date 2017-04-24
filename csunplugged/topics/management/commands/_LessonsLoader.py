"""Custom loader for loading lessons."""

from utils.BaseLoader import BaseLoader
from ._LessonLoader import LessonLoader


class LessonsLoader(BaseLoader):
    """Custom loader for loading lessons."""

    def __init__(self, load_log, lessons_structure, topic, unit_plan, BASE_PATH):
        """Create the loader for loading lessons.

        Args:
            load_log: List of log messages (list).
            lessons_structure: List of dictionaries for each lesson (list).
            topic: Object of Topic model.
            unit_plan: Object of UnitPlan model.
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH, load_log)
        self.lessons_structure = lessons_structure
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
        """Run loader for each lesson."""
        for lesson_slug, lesson_structure in self.lessons_structure.items():
            LessonLoader(
                self.load_log,
                lesson_slug,
                lesson_structure,
                self.topic,
                self.unit_plan,
                self.BASE_PATH
            ).load()
