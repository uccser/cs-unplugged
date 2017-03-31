from tests.BaseTest import BaseTest
from django.urls import reverse


class IntegrationURLTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)
    
    def test_valid_integration(self):
        url = reverse('topics:integration', args=['binary-numbers', 'binary-bracelets'])
        self.assertEqual(url, '/en/topics/binary-numbers/integrations/binary-bracelets/')