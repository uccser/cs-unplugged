from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class TopicModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()

    def test_topic_str(self):
        topic = self.test_data.create_topic(1)
        self.assertEqual(topic.__str__(), "Topic 1")

    def test_topic_model_type(self):
        topic = self.test_data.create_topic(1)
        self.assertEqual(topic.model_type(), "Topic")

    def test_topic_model_get_absolute_url(self):
        topic = self.test_data.create_topic(1)
        self.assertEqual(
            topic.get_absolute_url(),
            "/en/topics/topic-1/"
        )
