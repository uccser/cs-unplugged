from django.db import transaction
from topics.management.commands.BaseLoader import BaseLoader
from topics.management.commands.LessonLoader import LessonLoader
from topics.models import CurriculumLink

class LessonsLoader(BaseLoader):
    """Loader for lessons"""

    def __init__(self, lessons_structure, topic, unit_plan):
        """Inititiates the loader for lessons

        Args:
            lessons_structure: list of dictionaries for each lesson
            topic: Topic model object
            unit_plan: UnitPlan model object
        """
        super().__init__()
        self.lessons_structure = lessons_structure
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
        """Call (single) LessonLoader for each lesson to load into db"""
        for lesson_structure in self.lessons_structure:
            LessonLoader(lesson_structure, self.topic, self.unit_plan).load()
