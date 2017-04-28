import os.path
from os import listdir
import django
from tests.BaseTestWithDB import BaseTestWithDB

from topics.models import LearningOutcome
from topics.management.commands._LearningOutcomesLoader import LearningOutcomesLoader


class CurriculumAreaModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.BASE_PATH = "tests/topics/loaders/assets/learning_outcomes/"

    def test_new_learning_outcome(self):
        file = "new.yaml"

        new_loader = LearningOutcomesLoader(file, self.BASE_PATH)
        new_loader.load()

        lo_objects = list(LearningOutcome.objects.values_list('slug', flat=True))
        print(lo_objects)

        self.assertEqual(['cats'], lo_objects)

