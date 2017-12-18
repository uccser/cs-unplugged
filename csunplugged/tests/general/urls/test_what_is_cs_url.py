from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class WhatIsCSURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_what_is_cs_url(self):
        url = reverse("general:what_is_cs")
        self.assertEqual(url, "/en/what-is-computer-science/")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
