from tests.BaseTest import BaseTest
from django.urls import reverse


class IndexURLTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_valid_index(self):
        url = reverse('topics:index')
        self.assertEqual(url, '/en/topics/')
        
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)