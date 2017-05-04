from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class GlossaryURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = 'en'

    def test_valid_glossary_url(self):
        url = reverse('topics:glossary')
        self.assertEqual(url, '/en/topics/glossary/')

    def test_valid_glossary_json_url(self):
        url = reverse('topics:glossary_json')
        self.assertEqual(url, '/en/topics/glossary/json/')
