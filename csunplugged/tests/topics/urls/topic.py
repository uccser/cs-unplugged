from tests.BaseTest import BaseTest
from django.urls import reverse


class TopicURLTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_valid_topic(self):
        url = reverse('topics:topic', args=['binary-numbers'])
        self.assertEqual(url, '/en/topics/binary-numbers/')
