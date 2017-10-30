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
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        self.test_data.create_curriculum_area(1)

        config_file = "basic-config.yaml"

        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        lo_loader.load()

        lo_objects = LearningOutcome.objects.all()

        self.assertQuerysetEqual(
            lo_objects,
            ["<LearningOutcome: Justify why there aren’t actual 0’s and 1’s zooming around inside a computer.>"]
        )
