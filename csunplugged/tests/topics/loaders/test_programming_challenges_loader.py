import os.path
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from django.utils import translation
from topics.models import ProgrammingChallenge
from topics.management.commands._ProgrammingChallengesLoader import ProgrammingChallengesLoader
from utils.errors.VertoConversionError import VertoConversionError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError


class ProgrammingChallengesLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "programming_challenges"
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        config_file = "basic-config-1.yaml"
        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()
        pc_objects = ProgrammingChallenge.objects.all()
        self.assertQuerysetEqual(
            pc_objects,
            ["<ProgrammingChallenge: Programming Challenge 1>"]
        )

    def test_missing_translation_is_listed_unavailable(self):
        config_file = "basic-config-1.yaml"
        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()
        pc = ProgrammingChallenge.objects.get(slug="programming-challenge-1")
        self.assertSetEqual(set(["en"]), set(pc.languages))

    def test_missing_hints_optional(self):
        config_file = "missing-hints.yaml"

        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")

        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()  # Should not throw error, as hints are optional
        pc = ProgrammingChallenge.objects.get(slug="missing-hints")
        implementation = pc.implementations.all()[0]
        self.assertEquals("", implementation.hints)

    def test_missing_solution(self):
        config_file = "missing-solution.yaml"

        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")

        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        with self.assertRaises(CouldNotFindMarkdownFileError):
            pc_loader.load()

    def test_missing_testing_examples(self):
        config_file = "missing-testing-examples.yaml"

        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")

        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        with self.assertRaises(CouldNotFindMarkdownFileError):
            pc_loader.load()

    def test_missing_expected_result(self):
        config_file = "missing-expected-result.yaml"

        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")

        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        with self.assertRaises(CouldNotFindMarkdownFileError):
            pc_loader.load()

    def test_full_translation(self):
        config_file = "translation.yaml"

        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")

        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()

        pc = ProgrammingChallenge.objects.get(slug="translation")
        implementation = pc.implementations.all()[0]

        self.assertSetEqual(set(["en", "de"]), set(pc.languages))
        self.assertSetEqual(set(["en", "de"]), set(implementation.languages))

        self.assertEqual("Translation English", pc.name)
        self.assertIn("English programming challenge content", pc.content)
        self.assertIn("English expected result content.", implementation.expected_result)
        self.assertIn("English solution content.", implementation.solution)
        self.assertIn("English hints content.", implementation.hints)

        with translation.override("de"):
            self.assertEqual("Translation German", pc.name)
            self.assertIn("German programming challenge content", pc.content)
            self.assertIn("German expected result content.", implementation.expected_result)
            self.assertIn("German solution content.", implementation.solution)
            self.assertIn("German hints content.", implementation.hints)

    def test_translation_missing_solution(self):
        config_file = "translation-missing-solution.yaml"

        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")

        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()

        pc = ProgrammingChallenge.objects.get(slug="translation-missing-solution")

        # All required parts of the programming challenge are available in german
        self.assertSetEqual(set(["en", "de"]), set(pc.languages))

        implementation = pc.implementations.all()[0]

        # German solution is missing from the implementation, so the
        # implementation is not available in german.
        self.assertSetEqual(set(["en"]), set(implementation.languages))

    def test_translation_missing_expected_result(self):
        config_file = "translation-missing-expected-result.yaml"

        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")

        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()

        pc = ProgrammingChallenge.objects.get(slug="translation-missing-expected-result")

        # All required parts of the programming challenge are available in german
        self.assertSetEqual(set(["en", "de"]), set(pc.languages))

        implementation = pc.implementations.all()[0]

        # German expected result is missing from the implementation, so the
        # implementation is not available in german.
        self.assertSetEqual(set(["en"]), set(implementation.languages))

    def test_translation_missing_hints(self):
        config_file = "translation-missing-hints.yaml"

        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")

        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()  # Should not throw error, as hints are optional
        pc = ProgrammingChallenge.objects.get(slug="translation-missing-hints")
        implementation = pc.implementations.all()[0]

        # Hints are optional, so challenge and implementation both available in de
        self.assertSetEqual(set(["en", "de"]), set(implementation.languages))
        self.assertSetEqual(set(["en", "de"]), set(pc.languages))

        self.assertIn("English hints content.", implementation.hints)
        with translation.override("de"):
            # accessing the untranslated field should not default back to english
            self.assertEquals("", implementation.hints)

    def test_markdown_with_style_error(self):
        config_file = "basic-config-2.yaml"
        self.test_data.create_difficulty_level(1)
        self.test_data.create_programming_language(1)
        topic = self.test_data.create_topic(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        with self.assertRaises(VertoConversionError):
            pc_loader.load()

    def test_empty_data(self):
        config_file = "empty-data.yaml"
        topic = self.test_data.create_topic(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pc_loader.load
        )

    def test_missing_challenge_number(self):
        config_file = "missing-challenge-number.yaml"
        topic = self.test_data.create_topic(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pc_loader.load
        )

    def test_missing_challenge_set_number(self):
        config_file = "missing-challenge-set-number.yaml"
        topic = self.test_data.create_topic(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pc_loader.load
        )

    def test_missing_difficulty_level(self):
        config_file = "missing-difficulty-level.yaml"
        topic = self.test_data.create_topic(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pc_loader.load
        )

    def test_invalid_difficulty_level(self):
        config_file = "basic-config-1.yaml"
        self.test_data.create_programming_language(1)
        topic = self.test_data.create_topic(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            KeyNotFoundError,
            pc_loader.load
        )

    def test_missing_programming_languages(self):
        config_file = "missing-programming-languages.yaml"
        topic = self.test_data.create_topic(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pc_loader.load
        )

    def test_empty_programming_languages(self):
        config_file = "empty-programming-languages.yaml"
        topic = self.test_data.create_topic(1)
        self.test_data.create_difficulty_level(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            pc_loader.load
        )

    def test_invalid_programming_language(self):
        config_file = "basic-config-1.yaml"
        self.test_data.create_difficulty_level(1)
        topic = self.test_data.create_topic(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            KeyNotFoundError,
            pc_loader.load
        )

    def test_missing_learning_outcomes(self):
        config_file = "basic-config-1.yaml"
        topic = self.test_data.create_topic(1)
        self.test_data.create_programming_language(1)
        self.test_data.create_difficulty_level(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()
        challenge = ProgrammingChallenge.objects.get(slug="programming-challenge-1")
        self.assertFalse(challenge.learning_outcomes.exists())

    def test_empty_learning_outcomes(self):
        config_file = "empty-learning-outcomes.yaml"
        topic = self.test_data.create_topic(1)
        self.test_data.create_programming_language(1)
        self.test_data.create_difficulty_level(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()
        challenge = ProgrammingChallenge.objects.get(slug="programming-challenge-1")
        self.assertFalse(challenge.learning_outcomes.exists())

    def test_invalid_learning_outcomes(self):
        config_file = "invalid-learning-outcomes.yaml"
        topic = self.test_data.create_topic(1)
        self.test_data.create_programming_language(1)
        self.test_data.create_difficulty_level(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            KeyNotFoundError,
            pc_loader.load
        )

    def test_valid_learning_outcomes(self):
        config_file = "learning-outcomes.yaml"
        topic = self.test_data.create_topic(1)
        self.test_data.create_difficulty_level(1)
        self.test_data.create_programming_language(1)
        self.test_data.create_learning_outcome(1)
        self.test_data.create_learning_outcome(2)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()
        challenge = ProgrammingChallenge.objects.get(slug="programming-challenge-1")
        self.assertQuerysetEqual(
            challenge.learning_outcomes.order_by("slug"),
            [
                "<LearningOutcome: Outcome 1>",
                "<LearningOutcome: Outcome 2>",
            ]
        )

    def test_insert_start(self):
        config_file = "basic-config-1.yaml"
        topic = self.test_data.create_topic(1)
        self.test_data.create_difficulty_level(1)
        self.test_data.create_programming_language(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()

        pc_objects = ProgrammingChallenge.objects.all()

        self.assertQuerysetEqual(
            list(pc_objects),
            [
                "<ProgrammingChallenge: Programming Challenge 1>",
            ]
        )

        config_file = "multiple-challenges.yaml"
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()

        pc_objects = ProgrammingChallenge.objects.all()

        self.assertQuerysetEqual(
            pc_objects,
            [
                "<ProgrammingChallenge: Translation English>",
                "<ProgrammingChallenge: Programming Challenge 1>",
            ],
            ordered=False
        )

    def test_remove_start(self):
        config_file = "multiple-challenges.yaml"
        topic = self.test_data.create_topic(1)
        self.test_data.create_difficulty_level(1)
        self.test_data.create_programming_language(1)
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()

        pc_objects = ProgrammingChallenge.objects.all()

        self.assertQuerysetEqual(
            pc_objects,
            [
                "<ProgrammingChallenge: Translation English>",
                "<ProgrammingChallenge: Programming Challenge 1>",
            ],
            ordered=False
        )

        config_file = "basic-config-1.yaml"
        pc_loader = ProgrammingChallengesLoader(topic, structure_filename=config_file, base_path=self.base_path)
        pc_loader.load()

        pc_objects = ProgrammingChallenge.objects.all()

        self.assertQuerysetEqual(
            list(pc_objects),
            [
                "<ProgrammingChallenge: Programming Challenge 1>",
            ]
        )
