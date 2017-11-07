from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class AboutURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_about_url(self):
        url = reverse("general:about")
        self.assertEqual(url, "/en/about/")

        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
