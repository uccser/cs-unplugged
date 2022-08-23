from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class TopicWhatsItAllAboutURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_topic_whats_it_all_about(self):
        kwargs = {
            "topic_slug": "binary-numbers",
        }
        url = reverse("topics:topic_whats_it_all_about", kwargs=kwargs)
        self.assertEqual(url, "/en/topics/binary-numbers/whats-it-all-about/")
