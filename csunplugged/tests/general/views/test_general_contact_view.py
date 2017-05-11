from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class ContactViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_contact_view(self):
        response = self.client.get(reverse("general:contact"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact Us")
