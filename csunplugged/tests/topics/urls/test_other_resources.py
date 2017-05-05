from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class OtherResourcesURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_other_resources(self):
        url = reverse("topics:other_resources", args=["binary-numbers"])
        self.assertEqual(url, "/en/topics/binary-numbers/other-resources/")
