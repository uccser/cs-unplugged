from tests.BaseTestWithDB import BaseTestWithDB

from topics.models import LearningOutcome
from topics.management.commands._LearningOutcomesLoader import LearningOutcomesLoader


class LearningOutcomesLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.BASE_PATH = "tests/topics/loaders/assets/learning_outcomes/"

    def test_basic_config(self):
        config_file = "basic_config.yaml"

        lo_loader = LearningOutcomesLoader(config_file, self.BASE_PATH)
        lo_loader.load()

        lo_objects = LearningOutcome.objects.all()

        self.assertQuerysetEqual(
            lo_objects,
            ['<LearningOutcome: cats>']
        )
