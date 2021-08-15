from http import HTTPStatus
from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class IndexURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_index(self):
        url = reverse("plugging_it_in:index")
        self.assertEqual(url, "/en/plugging-it-in/")

        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
