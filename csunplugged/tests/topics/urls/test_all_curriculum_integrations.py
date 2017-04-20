from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class AllCurriculumIntegrationsURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = 'en'

    def test_valid_curriculum_integration(self):
        url = reverse('topics:all_curriculum_integrations')
        self.assertEqual(url, '/en/topics/curriculum-integrations/')
