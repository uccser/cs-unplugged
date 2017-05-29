from django.urls import reverse
from django.test import override_settings
from django.conf import settings
from tests.BaseTestWithDB import BaseTestWithDB


@override_settings(DEBUG=True)
class IndexURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
    # 
    # def test_valid_index(self):
    #     url = reverse("dev:index")
    #     self.assertEqual(url, "/en/__dev__/")
    #
    #     response = self.client.get(url)
    #     self.assertEqual(200, response.status_code)
