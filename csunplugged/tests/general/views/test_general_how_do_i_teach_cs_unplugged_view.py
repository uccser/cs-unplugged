from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class HowDoITeachCSUnpluggedViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_how_do_i_teach_cs_unplugged_view(self):
        response = self.client.get(reverse("general:how_do_i_teach_cs_unplugged"))
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertContains(response, "How do I teach CS Unplugged?")
