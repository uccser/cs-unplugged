import os.path

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import LearningOutcome
from topics.management.commands._LearningOutcomesLoader import LearningOutcomesLoader


class LearningOutcomesLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "learning_outcomes"
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        config_file = "basic-config.yaml"

        lo_loader = LearningOutcomesLoader(config_file, self.BASE_PATH)
        lo_loader.load()

        lo_objects = LearningOutcome.objects.all()

        self.assertQuerysetEqual(
            lo_objects,
            ["<LearningOutcome: Justify why there aren’t actual 0’s and 1’s zooming around inside a computer.>"]
        )
