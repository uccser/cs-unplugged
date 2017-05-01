from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class HomeURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = 'en'

    def test_valid_home_request(self):
        url = reverse('general:home')
        self.assertEqual(url, '/en/')

        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
