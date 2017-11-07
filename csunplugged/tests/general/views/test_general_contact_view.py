from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class ContactViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_contact_view(self):
        response = self.client.get(reverse("general:contact"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertContains(response, "Contact Us")
