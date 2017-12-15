from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class IntegrationURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_integration(self):
        kwargs = {
            "topic_slug": "binary-numbers",
            "integration_slug": "binary-bracelets",
        }
        url = reverse("topics:integration", kwargs=kwargs)
        self.assertEqual(url, "/en/topics/binary-numbers/integrations/binary-bracelets/")
