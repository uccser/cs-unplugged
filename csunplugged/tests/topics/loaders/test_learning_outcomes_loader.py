from tests.BaseTestWithDB import BaseTestWithDB

from topics.models import LearningOutcome
from topics.management.commands._LearningOutcomesLoader import LearningOutcomesLoader


class LearningOutcomesLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.BASE_PATH = "tests/topics/loaders/assets/learning_outcomes/"

    def test_new_learning_outcome(self):
        config_file = "one_learning_outcome.yaml"

        new_loader = LearningOutcomesLoader(config_file, self.BASE_PATH)
        new_loader.load()

        lo_objects = LearningOutcome.objects.all()

        self.assertQuerysetEqual(
            lo_objects,
            ['<LearningOutcome: cats>']
        )
