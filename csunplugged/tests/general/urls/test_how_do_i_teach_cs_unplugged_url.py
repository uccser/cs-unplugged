from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse
from http import HTTPStatus


class HowDoITeachCSUnpluggedURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_how_do_i_teach_cs_unplugged_url(self):
        url = reverse("general:how_do_i_teach_cs_unplugged")
        self.assertEqual(url, "/en/how-do-i-teach-cs-unplugged/")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
