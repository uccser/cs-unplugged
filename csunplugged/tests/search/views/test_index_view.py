from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from django.core import management


class IndexViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_search_view_with_no_query_with_index(self):
        self.test_data.create_topic(1)
        self.test_data.create_topic(2)
        self.test_data.create_topic(3)
        management.call_command("rebuild_index", "--noinput")
        url = reverse("search:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertFalse(response.context["object_list"])
        self.assertIsNone(response.context.get("query"))

    def test_search_view_with_no_query_with_no_index(self):
        url = reverse("search:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertFalse(response.context["object_list"])
        self.assertIsNone(response.context.get("query"))
