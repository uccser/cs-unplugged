import os.path
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import ProgrammingChallenge
from topics.management.commands._ProgrammingChallengesLoader import ProgrammingChallengesLoader
from utils.errors.MarkdownStyleError import MarkdownStyleError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError


class ProgrammingChallengesLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "programming_challenges"

    def test_basic_config(self):
        config_file = os.path.join(self.loader_name, "basic-config-1.yaml")
        self.test_data.create_difficulty_level(1)
        self.test_data.create_programming_language(1)
        topic = self.test_data.create_topic(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        pe_loader.load()
        pe_objects = ProgrammingChallenge.objects.all()
        self.assertQuerysetEqual(
            pe_objects,
            ["<ProgrammingChallenge: Programming Challenge 1>"]
        )

    def test_markdown_with_style_error(self):
        config_file = os.path.join(self.loader_name, "basic-config-2.yaml")
        self.test_data.create_difficulty_level(1)
        self.test_data.create_programming_language(1)
        topic = self.test_data.create_topic(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        with self.assertRaises(MarkdownStyleError):
            pe_loader.load()

    def test_empty_data(self):
        config_file = os.path.join(self.loader_name, "empty-data.yaml")
        topic = self.test_data.create_topic(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pe_loader.load
        )

    def test_missing_challenge_number(self):
        config_file = os.path.join(self.loader_name, "missing-challenge-number.yaml")
        topic = self.test_data.create_topic(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pe_loader.load
        )

    def test_missing_challenge_set_number(self):
        config_file = os.path.join(self.loader_name, "missing-challenge-set-number.yaml")
        topic = self.test_data.create_topic(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pe_loader.load
        )

    def test_missing_difficulty_level(self):
        config_file = os.path.join(self.loader_name, "missing-difficulty-level.yaml")
        topic = self.test_data.create_topic(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pe_loader.load
        )

    def test_invalid_difficulty_level(self):
        config_file = os.path.join(self.loader_name, "basic-config-1.yaml")
        self.test_data.create_programming_language(1)
        topic = self.test_data.create_topic(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            KeyNotFoundError,
            pe_loader.load
        )

    def test_missing_programming_languages(self):
        config_file = os.path.join(self.loader_name, "missing-programming-languages.yaml")
        topic = self.test_data.create_topic(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pe_loader.load
        )

    def test_empty_programming_languages(self):
        config_file = os.path.join(self.loader_name, "empty-programming-languages.yaml")
        topic = self.test_data.create_topic(1)
        self.test_data.create_difficulty_level(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            pe_loader.load
        )

    def test_invalid_programming_language(self):
        config_file = os.path.join(self.loader_name, "basic-config-1.yaml")
        self.test_data.create_difficulty_level(1)
        topic = self.test_data.create_topic(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            KeyNotFoundError,
            pe_loader.load
        )

    def test_missing_learning_outcomes(self):
        config_file = os.path.join(self.loader_name, "basic-config-1.yaml")
        topic = self.test_data.create_topic(1)
        self.test_data.create_programming_language(1)
        self.test_data.create_difficulty_level(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        pe_loader.load()
        challenge = ProgrammingChallenge.objects.get(slug="programming-challenge-1")
        self.assertFalse(challenge.learning_outcomes.exists())

    def test_empty_learning_outcomes(self):
        config_file = os.path.join(self.loader_name, "empty-learning-outcomes.yaml")
        topic = self.test_data.create_topic(1)
        self.test_data.create_programming_language(1)
        self.test_data.create_difficulty_level(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        pe_loader.load()
        challenge = ProgrammingChallenge.objects.get(slug="programming-challenge-1")
        self.assertFalse(challenge.learning_outcomes.exists())

    def test_invalid_learning_outcomes(self):
        config_file = os.path.join(self.loader_name, "invalid-learning-outcomes.yaml")
        topic = self.test_data.create_topic(1)
        self.test_data.create_programming_language(1)
        self.test_data.create_difficulty_level(1)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            KeyNotFoundError,
            pe_loader.load
        )

    def test_valid_learning_outcomes(self):
        config_file = os.path.join(self.loader_name, "learning-outcomes.yaml")
        topic = self.test_data.create_topic(1)
        self.test_data.create_difficulty_level(1)
        self.test_data.create_programming_language(1)
        self.test_data.create_learning_outcome(1)
        self.test_data.create_learning_outcome(2)
        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        pe_loader.load()
        challenge = ProgrammingChallenge.objects.get(slug="programming-challenge-1")
        self.assertQuerysetEqual(
            challenge.learning_outcomes.order_by("slug"),
            [
                "<LearningOutcome: Outcome 1>",
                "<LearningOutcome: Outcome 2>",
            ]
        )
