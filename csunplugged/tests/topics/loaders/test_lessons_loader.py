import os.path
from unittest.mock import Mock

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import Lesson
from topics.management.commands._LessonsLoader import LessonsLoader


class LessonsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_log = Mock()
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "lessons"

    def test_basic_config(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        complete_config_file_path = os.path.join(self.test_data.LOADER_ASSET_PATH, config_file)
        lessons_structure = self.test_data.load_yaml_file(complete_config_file_path)

        topic = self.test_data.create_test_topic("1")
        unit_plan = self.test_data.create_test_unit_plan(topic, "1")

        lesson_loader = LessonsLoader(
            config_file,
            self.load_log,
            lessons_structure,
            topic,
            unit_plan,
            self.test_data.LOADER_ASSET_PATH
        )
        lesson_loader.load()

        lesson_objects = Lesson.objects.all()

        self.assertQuerysetEqual(
            lesson_objects,
            ["<Lesson: Lesson 1>"]
        )
