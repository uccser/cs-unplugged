from .BaseLoader import BaseLoader
from .LessonLoader import LessonLoader


class LessonsLoader(BaseLoader):
    """Loader for lessons"""

    def __init__(self, load_log, lessons_structure, topic, unit_plan):
        """Inititiates the loader for lessons

        Args:
            lessons_structure: list of dictionaries for each lesson
            topic: Topic model object
            unit_plan: UnitPlan model object
        """
        super().__init__(load_log)
        self.lessons_structure = lessons_structure
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
        """Call (single) LessonLoader for each lesson to load into db"""
        for structure in self.lessons_structure:
            loader = LessonLoader(self.load_log, structure,
                                  self.topic, self.unit_plan)
            loader.load()
