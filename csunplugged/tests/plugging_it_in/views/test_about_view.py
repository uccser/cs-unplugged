from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class AboutViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_about_view(self):
        response = self.client.get(reverse("plugging_it_in:about"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertContains(response, "About")
