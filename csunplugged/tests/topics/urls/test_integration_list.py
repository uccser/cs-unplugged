from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class IntegrationListURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_integration_list(self):
        url = reverse("topics:integration_list", args=["binary-numbers"])
        self.assertEqual(url, "/en/topics/binary-numbers/integrations/")
