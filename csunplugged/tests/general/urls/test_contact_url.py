from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class ContactURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_contact_url(self):
        url = reverse("general:contact")
        self.assertEqual(url, "/en/contact/")

        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
