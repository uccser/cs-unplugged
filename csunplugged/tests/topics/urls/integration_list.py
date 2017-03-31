from tests.BaseTest import BaseTest
from django.urls import reverse


class IntegrationListURLTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_valid_integration_list(self):
        url = reverse('topics:integration_list', args=['binary-numbers'])
        self.assertEqual(url, '/en/topics/binary-numbers/integrations/')
