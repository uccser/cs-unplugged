import os.path
from unittest.mock import Mock

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import Topic
from topics.management.commands._TopicLoader import TopicLoader

from utils.errors.CouldNotFindConfigFileError import CouldNotFindConfigFileError
from utils.errors.NoHeadingFoundInMarkdownFileError import NoHeadingFoundInMarkdownFileError
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError


class TopicLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "topic"
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_topic_loader_configuration(self):
        config_file = "topic-1/topic-1.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        topic_loader.load()
        self.assertQuerysetEqual(
            Topic.objects.all(),
            ["<Topic: Topic 1>"]
        )

    def test_topic_loader_slug(self):
        config_file = "topic-1/topic-1.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        topic_loader.load()
        self.assertEquals(
            Topic.objects.get(slug="topic-1").slug,
            "topic-1",
        )

    def test_topic_loader_missing_configuration_file(self):
        config_file = "topic-1/topic-missing.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        self.assertRaises(
            CouldNotFindConfigFileError,
            topic_loader.load,
        )

    def test_topic_loader_valid_name_text(self):
        config_file = "topic-1/topic-1.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        topic_loader.load()
        self.assertEquals(
            Topic.objects.get(slug="topic-1").name,
            "Topic 1",
        )

    def test_topic_loader_missing_name_text(self):
        config_file = "topic-missing-name/topic-missing-name.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        self.assertRaises(
            NoHeadingFoundInMarkdownFileError,
            topic_loader.load,
        )

    def test_topic_loader_valid_content_text(self):
        config_file = "topic-1/topic-1.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        topic_loader.load()
        self.assertEquals(
            Topic.objects.get(slug="topic-1").content,
            "<p>Etiam in massa. Nam ut metus. In rhoncus venenatis tellus.</p>",
        )

    def test_topic_loader_missing_content_text(self):
        config_file = "topic-missing-content/topic-missing-content.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        self.assertRaises(
            EmptyMarkdownFileError,
            topic_loader.load,
        )

    def test_topic_loader_missing_unit_plans(self):
        config_file = "topic-missing-unit-plans/topic-missing-unit-plans.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        self.assertRaises(
            MissingRequiredFieldError,
            topic_loader.load,
        )

    def test_topic_loader_valid_icon(self):
        config_file = "topic-valid-icon/topic-valid-icon.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        topic_loader.load()
        self.assertEquals(
            Topic.objects.get(slug="topic-valid-icon").icon,
            "img/logo.png",
        )

    def test_topic_loader_missing_icon(self):
        config_file = "topic-1/topic-1.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        # Passes if loader throws no exception
        topic_loader.load()

    def test_topic_loader_empty_icon(self):
        config_file = "empty-icon/empty-icon.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        topic_loader.load()
        topic = Topic.objects.get(slug="empty-icon")
        self.assertIsNone(topic.icon)

    def test_topic_loader_other_resources_empty(self):
        config_file = "empty-other-resources/empty-other-resources.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        topic_loader.load()
        topic = Topic.objects.get(slug="empty-other-resources")
        self.assertIsNone(topic.other_resources)

    def test_topic_loader_programming_challenges_empty(self):
        config_file = "empty-programming-challenges/empty-programming-challenges.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        # Passes if loader throws no exception
        topic_loader.load()

    def test_topic_loader_curriculum_integrations_empty(self):
        config_file = "empty-curriculum-integrations/empty-curriculum-integrations.yaml"
        factory = Mock()
        topic_loader = TopicLoader(
            factory,
            config_file,
            self.BASE_PATH
        )
        # Passes if loader throws no exception
        topic_loader.load()
