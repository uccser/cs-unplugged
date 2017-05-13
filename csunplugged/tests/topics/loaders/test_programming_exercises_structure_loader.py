import os.path
from unittest.mock import Mock

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TestDataGenerator import TestDataGenerator


class ProgrammingExercisesStructureLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_log = Mock()
        self.test_data = TestDataGenerator()
        self.loader_name = "programming_exercises_structure"

    def test_basic_config(self):
        pass
