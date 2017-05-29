from django.urls import reverse
from django.conf import settings
from django.test import override_settings, modify_settings
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


@override_settings(DEBUG=True)
class IndexViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.topics_test_data = TopicsTestDataGenerator()
    #
    # def test_index_with_no_content(self):
    #     url = reverse("dev:index")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_index_topics_context(self):
    #     topic = self.topics_test_data.create_topic(3)
    #     topic = self.topics_test_data.create_topic(2)
    #     topic = self.topics_test_data.create_topic(4)
    #     topic = self.topics_test_data.create_topic(1)
    #     url = reverse("dev:index")
    #     self.assertEqual(200, response.status_code)
    #     self.assertQuerysetEqual(
    #         response.context["topics"],
    #         [
    #             "<Topic: Topic 1>",
    #             "<Topic: Topic 2>",
    #             "<Topic: Topic 3>",
    #             "<Topic: Topic 4>",
    #         ]
    #     )
