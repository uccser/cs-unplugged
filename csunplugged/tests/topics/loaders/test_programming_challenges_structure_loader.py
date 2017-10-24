import os.path

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import ProgrammingChallengeDifficulty
from topics.models import ProgrammingChallengeLanguage
from topics.management.commands._ProgrammingChallengesStructureLoader import ProgrammingChallengesStructureLoader


class ProgrammingChallengesStructureLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "programming_challenges_structure"
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        config_file = "basic-config.yaml"

        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        pes_loader.load()

        ped_objects = ProgrammingChallengeDifficulty.objects.all()
        pel_objects = ProgrammingChallengeLanguage.objects.all()

        self.assertQuerysetEqual(
            ped_objects,
            ["<ProgrammingChallengeDifficulty: Level 1>"]
        )

        self.assertQuerysetEqual(
            pel_objects,
            ["<ProgrammingChallengeLanguage: Language 1>"]
        )
