from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class IntegrationURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = 'en'

    def test_valid_integration(self):
        url = reverse('topics:integration', args=['binary-numbers', 'binary-bracelets'])
        self.assertEqual(url, '/en/topics/binary-numbers/integrations/binary-bracelets/')
