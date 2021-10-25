from http import HTTPStatus
from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class AboutURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_about(self):
        url = reverse("plugging_it_in:block_based_vs_scratch")
        self.assertEqual(url, "/en/plugging-it-in/block-based-vs-scratch/")

        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
