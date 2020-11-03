from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class SaveAttamptURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_jobe_proxy(self):
        url = reverse("plugging_it_in:save_attempt")
        self.assertEqual(url, "/en/plugging-it-in/save_attempt")
