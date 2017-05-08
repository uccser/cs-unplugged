from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class TopicURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_topic(self):
        url = reverse("topics:topic", args=["binary-numbers"])
        self.assertEqual(url, "/en/topics/binary-numbers/")
