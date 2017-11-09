import os.path
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import ProgrammingChallengeDifficulty
from topics.models import ProgrammingChallengeLanguage
from topics.management.commands._ProgrammingChallengesStructureLoader import ProgrammingChallengesStructureLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError


class ProgrammingChallengesStructureLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "programming_challenges_structure"
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        config_file = "basic-config.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(config_file, self.BASE_PATH)
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

    def test_missing_languages(self):
        config_file = "missing-languages.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_missing_difficulties(self):
        config_file = "missing-difficulties.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_languages(self):
        config_file = "empty-languages.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_languages_data(self):
        config_file = "empty-languages-data.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_difficulties(self):
        config_file = "empty-difficulties.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_languages_name(self):
        config_file = "empty-languages-name.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_languages_number(self):
        config_file = "empty-languages-number.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_difficulties_data(self):
        config_file = "empty-difficulties-data.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_difficulties_name(self):
        config_file = "empty-difficulties-name.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )
