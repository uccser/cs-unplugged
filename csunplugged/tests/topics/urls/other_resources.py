from tests.BaseTest import BaseTest
from django.urls import reverse


class OtherResourcesURLTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_valid_other_resources(self):
        url = reverse('topics:other_resources', args=['binary-numbers'])
        self.assertEqual(url, '/en/topics/binary-numbers/other-resources/')
