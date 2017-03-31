from tests.BaseTest import BaseTest
from django.urls import reverse


class AllCurriculumIntegrationsURLTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_valid_curriculum_integration(self):
        url = reverse('topics:all_curriculum_integrations')
        self.assertEqual(url, '/en/topics/curriculum-integrations/')