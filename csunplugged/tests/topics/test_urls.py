from tests.BaseTest import BaseTest
from topics import urls
from django.urls import reverse


class UrlsTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_topics(self):
        url = reverse('topics:index')
        self.assertEqual(url, '/en/topics/')