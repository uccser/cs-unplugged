from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator


class BinaryToAlphabetResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_binary_to_alphabet_resource_form_view(self):
        resource = self.test_data.create_resource(
            "binary-to-alphabet",
            "Binary To Alphabet",
            "resources/binary-to-alphabet.html",
            "binary_to_alphabet.py"
        )
        kwargs = {
            "resource_slug": resource.slug
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
