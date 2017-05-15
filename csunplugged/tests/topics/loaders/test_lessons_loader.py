import os.path
from unittest.mock import Mock

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TestDataGenerator import TestDataGenerator

from topics.models import Lesson
from topics.management.commands._LessonsLoader import LessonsLoader


class LessonsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_log = Mock()
        self.test_data = TestDataGenerator()
        self.loader_name = "lessons"

    def test_basic_config(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")

        unit_plan = self.test_data.create_test_unit_plan("1")
        topic = self.test_data.create_test_topic("1")

        lesson_loader = LessonsLoader(config_file, self.load_log, lessons_structure, topic, unit_plan, self.test_data.LOADER_ASSET_PATH)
        lesson_loader.load()

        lessons_objects = Lessons.objects.all()

        self.assertQuerysetEqual(
            ci_objects,
            ["<Lesson: Lesson 1>"]
        )
