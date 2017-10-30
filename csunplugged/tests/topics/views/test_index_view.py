from http import HTTPStatus
from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from topics.models import Topic


class IndexViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_index_with_no_topics(self):
        url = reverse("topics:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_index_with_one_topic(self):
        new_topic = Topic(
            slug="binary-numbers",
            name="Binary Numbers",
            content="content",
            other_resources="content",
            icon="icon"
        )
        new_topic.save()

        url = reverse("topics:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertQuerysetEqual(
            response.context["all_topics"],
            ["<Topic: Binary Numbers>"]
        )
