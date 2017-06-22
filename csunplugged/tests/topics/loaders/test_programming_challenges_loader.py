import os.path

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import ProgrammingChallenge
from topics.management.commands._ProgrammingChallengesLoader import ProgrammingChallengesLoader

from utils.errors.MarkdownStyleError import MarkdownStyleError


class ProgrammingChallengesLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "programming_challenges"

    def test_basic_config(self):
        config_file = os.path.join(self.loader_name, "basic-config-1.yaml")

        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")

        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        pe_loader.load()

        pe_objects = ProgrammingChallenge.objects.all()

        self.assertQuerysetEqual(
            pe_objects,
            ["<ProgrammingChallenge: Programming Challenge 1>"]
        )

    def test_markdown_with_style_error(self):
        config_file = os.path.join(self.loader_name, "basic-config-2.yaml")

        self.test_data.create_difficulty_level("1")
        self.test_data.create_programming_language("1")
        topic = self.test_data.create_topic("1")

        pe_loader = ProgrammingChallengesLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)

        with self.assertRaises(MarkdownStyleError):
            pe_loader.load()
