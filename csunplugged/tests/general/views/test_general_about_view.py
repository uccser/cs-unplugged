from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class AboutViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = 'en'

    def test_about_view(self):
        response = self.client.get(reverse('general:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About")
