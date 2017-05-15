import os.path

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TestDataGenerator import TestDataGenerator

from topics.models import ProgrammingExerciseDifficulty
from topics.models import ProgrammingExerciseLanguage
from topics.management.commands._ProgrammingExercisesStructureLoader import ProgrammingExercisesStructureLoader


class ProgrammingExercisesStructureLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TestDataGenerator()
        self.loader_name = "programming_exercises_structure"
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        config_file = "basic-config.yaml"

        pes_loader = ProgrammingExercisesStructureLoader(config_file, self.BASE_PATH)
        pes_loader.load()

        ped_objects = ProgrammingExerciseDifficulty.objects.all()
        pel_objects = ProgrammingExerciseLanguage.objects.all()

        self.assertQuerysetEqual(
            ped_objects,
            ["<ProgrammingExerciseDifficulty: Level 1>"]
        )

        self.assertQuerysetEqual(
            pel_objects,
            ["<ProgrammingExerciseLanguage: Language 1>"]
        )
