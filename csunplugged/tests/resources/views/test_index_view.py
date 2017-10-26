from tests.BaseTestWithDB import BaseTestWithDB
from django.test import tag
from django.urls import reverse
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator


@tag("resource")
class IndexViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_resources_index_with_no_resources(self):
        url = reverse("resources:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["all_resources"].exists())

    def test_resources_index_with_one_resource(self):
        self.test_data.create_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "BinaryCardsResourceGenerator",
        )
        url = reverse("resources:index")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertQuerysetEqual(
            response.context["all_resources"],
            ["<Resource: Resource Binary Cards>"]
        )

    def test_resources_index_with_multiple_resources(self):
        self.test_data.create_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "BinaryCardsResourceGenerator",
        )
        self.test_data.create_resource(
            "sorting-network",
            "Sorting Network",
            "resources/sorting-network.html",
            "SortingNetworkResourceGenerator.py",
        )
        url = reverse("resources:index")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertQuerysetEqual(
            response.context["all_resources"],
            [
                "<Resource: Resource Binary Cards>",
                "<Resource: Resource Sorting Network>",
            ]
        )
