import os.path
from unittest.mock import Mock

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TestDataGenerator import TestDataGenerator

from topics.models import Topic
from topics.management.commands._TopicLoader import TopicLoader


class TopicLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TestDataGenerator()
        self.loader_name = "topic"
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        config_file = "topic-1/topic-1.yaml"
        factory = Mock()

        topic_loader = TopicLoader(factory, config_file, self.BASE_PATH)
        topic_loader.load()

        topic_objects = Topic.objects.all()

        self.assertQuerysetEqual(
            topic_objects,
            ["<Topic: Topic 1>"]
        )
