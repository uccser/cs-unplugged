from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class PeopleURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_people_url(self):
        url = reverse("general:people")
        self.assertEqual(url, "/en/people/")

        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
