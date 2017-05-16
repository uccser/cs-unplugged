import os.path
from unittest.mock import Mock

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import ProgrammingExercise
from topics.management.commands._ProgrammingExercisesLoader import ProgrammingExercisesLoader


class ProgrammingExercisesLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_log = Mock()
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "programming_exercises"

    def test_basic_config(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")

        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")

        pe_loader = ProgrammingExercisesLoader(self.load_log, config_file, topic, self.test_data.LOADER_ASSET_PATH)
        pe_loader.load()

        pe_objects = ProgrammingExercise.objects.all()

        self.assertQuerysetEqual(
            pe_objects,
            ["<ProgrammingExercise: Programming Challenge 1>"]
        )
