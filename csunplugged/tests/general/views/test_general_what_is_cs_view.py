from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class WhatIsCSViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_what_is_cs_view(self):
        response = self.client.get(reverse("general:what_is_cs"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertContains(response, "What is Computer Science?")
