from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class PeopleViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_people_view(self):
        response = self.client.get(reverse("general:people"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertContains(response, "People")
