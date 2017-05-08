from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class PeopleViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = 'en'

    def test_people_view(self):
        response = self.client.get(reverse('general:people'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "People")
