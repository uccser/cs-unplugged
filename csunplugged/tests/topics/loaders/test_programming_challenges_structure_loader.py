import os.path
from django.utils import translation
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import ProgrammingChallengeDifficulty
from topics.models import ProgrammingChallengeLanguage
from topics.management.commands._ProgrammingChallengesStructureLoader import ProgrammingChallengesStructureLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError


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
            ["<ProgrammingChallengeDifficulty: Level 1>"],
            transform=repr,
        )
        self.assertQuerysetEqual(
            pel_objects,
            ["<ProgrammingChallengeLanguage: Language 1>"],
            transform=repr,
        )

    def test_missing_languages(self):
        config_file = "missing-languages.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_missing_difficulties(self):
        config_file = "missing-difficulties.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_languages(self):
        config_file = "empty-languages.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_languages_data(self):
        config_file = "empty-languages-data.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_difficulties(self):
        config_file = "empty-difficulties.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_languages_name(self):
        config_file = "empty-languages-name.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_languages_number(self):
        config_file = "empty-languages-number.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pes_loader.load
        )

    def test_empty_difficulties_name(self):
        config_file = "empty-difficulties-name.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            InvalidYAMLValueError,
            pes_loader.load
        )

    def test_translation(self):
        config_file = "translation.yaml"

        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        pes_loader.load()

        translated_lang = ProgrammingChallengeLanguage.objects.get(slug="translated")
        self.assertSetEqual(set(["en", "de"]), set(translated_lang.languages))
        self.assertEqual("English language 1", translated_lang.name)
        with translation.override("de"):
            self.assertEqual("German language 1", translated_lang.name)

        translated_difficulty = ProgrammingChallengeDifficulty.objects.get(level=0)
        self.assertSetEqual(set(["en", "de"]), set(translated_difficulty.languages))
        self.assertEqual("English difficulty 1", translated_difficulty.name)
        with translation.override("de"):
            self.assertEqual("German difficulty 1", translated_difficulty.name)

    def test_translation_missing(self):
        config_file = "translation.yaml"

        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        pes_loader.load()

        untranslated_lang = ProgrammingChallengeLanguage.objects.get(slug="untranslated")
        self.assertSetEqual(set(["en"]), set(untranslated_lang.languages))
        self.assertEqual("English language 2", untranslated_lang.name)
        # Language name SHOULD fall back to english if not given
        with translation.override("de"):
            self.assertEqual("English language 2", untranslated_lang.name)

        untranslated_difficulty = ProgrammingChallengeDifficulty.objects.get(level=1)
        self.assertSetEqual(set(["en"]), set(untranslated_difficulty.languages))
        self.assertEqual("English difficulty 2", untranslated_difficulty.name)
        # Check name does not fall back to english for missing translation
        with translation.override("de"):
            self.assertEqual("", untranslated_difficulty.name)

    def test_insert_start(self):
        config_file = "basic-config.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        pes_loader.load()

        config_file = "insert-start.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        pes_loader.load()

        ped_objects = ProgrammingChallengeDifficulty.objects.all()
        pel_objects = ProgrammingChallengeLanguage.objects.all()
        self.assertQuerysetEqual(
            ped_objects,
            ["<ProgrammingChallengeDifficulty: Level 1>", "<ProgrammingChallengeDifficulty: Level 2>"],
            ordered=False,
            transform=repr,
        )
        self.assertQuerysetEqual(
            pel_objects,
            ["<ProgrammingChallengeLanguage: Language 1>", "<ProgrammingChallengeLanguage: Language 2>"],
            ordered=False,
            transform=repr,
        )

    def test_remove_start(self):
        config_file = "insert-start.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        pes_loader.load()

        config_file = "basic-config.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        pes_loader.load()

        ped_objects = ProgrammingChallengeDifficulty.objects.all()
        pel_objects = ProgrammingChallengeLanguage.objects.all()
        self.assertQuerysetEqual(
            ped_objects,
            ["<ProgrammingChallengeDifficulty: Level 1>"],
            ordered=False,
            transform=repr,
        )
        self.assertQuerysetEqual(
            pel_objects,
            ["<ProgrammingChallengeLanguage: Language 1>"],
            ordered=False,
            transform=repr,
        )

    def test_duplicate_language_numbers(self):
        config_file = "duplicate-language-numbers.yaml"
        pes_loader = ProgrammingChallengesStructureLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            InvalidYAMLValueError,
            pes_loader.load
        )
