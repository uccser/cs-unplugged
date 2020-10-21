from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class JobeProxyURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_jobe_proxy(self):
        url = reverse("plugging_it_in:jobe_proxy")
        self.assertEqual(url, "/en/plugging-it-in/jobe_proxy")
