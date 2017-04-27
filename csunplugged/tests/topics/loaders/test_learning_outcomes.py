from tests.BaseTestWithDB import BaseTestWithDB
from topics.management.commands._LearningOutcomesLoader import LearningOutcomesLoader


class CurriculumAreaModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_new_learning_outcome(self):
        new_loader = LearningOutcomesLoader("new.yaml", "csunplugged/tests/topics/loaders/assets/")
        new_loader.load()
