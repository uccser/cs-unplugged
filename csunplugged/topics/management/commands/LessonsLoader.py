import yaml
import os
from django.db import transaction
from topics.management.commands.BaseLoader import BaseLoader
from topics.management.commands.LessonLoader import LessonLoader
from topics.models import CurriculumLink

class LessonsLoader(BaseLoader):

    def __init__(self, lessons_structure, topic, unit_plan):
        super().__init__()
        self.lessons_structure = lessons_structure
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
        for lesson_structure in self.lessons_structure:
            LessonLoader(lesson_structure, self.topic, self.unit_plan).load()
