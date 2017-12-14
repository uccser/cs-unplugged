from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class OtherResourcesURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_other_resources(self):
        kwargs = {
            "topic_slug": "binary-numbers",
        }
        url = reverse("topics:other_resources", kwargs=kwargs)
        self.assertEqual(url, "/en/topics/binary-numbers/other-resources/")
