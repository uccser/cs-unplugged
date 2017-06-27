from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class LeftRightCardsResourceURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.RESOURCE_SLUG = "left-right-cards"
        self.RESOURCE_URL_KWARGS = {"resource_slug": self.RESOURCE_SLUG}

    def test_valid_left_right_cards_resource_url(self):
        url = reverse("resources:resource", kwargs=self.RESOURCE_URL_KWARGS)
        self.assertEqual(url, "/en/resources/left-right-cards/")

    def test_valid_left_right_cards_resource_generate_url(self):
        url = reverse("resources:generate", kwargs=self.RESOURCE_URL_KWARGS)
        self.assertEqual(url, "/en/resources/left-right-cards/generate")
