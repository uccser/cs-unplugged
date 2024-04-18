from http import HTTPStatus
from django.test import tag
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
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
        self.assertEqual(len(response.context["all_resources"]), 0)

    def test_resources_index_with_one_resource(self):
        self.test_data.create_resource(
            "resource",
            "Resource",
            "Description",
            "GridResourceGenerator",
        )
        url = reverse("resources:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertQuerysetEqual(
            response.context["all_resources"],
            ["<Resource: Resource>"],
            transform=repr,
        )
        self.assertEqual(
            response.context["all_resources"][0].thumbnail,
            "/static/img/resources/resource/thumbnails/en/resource-paper_size-a4.png"
        )

    def test_resources_index_with_multiple_resources(self):
        self.test_data.create_resource(
            "binary-cards",
            "Binary Cards",
            "Description of binary cards",
            "BinaryCardsResourceGenerator",
        )
        self.test_data.create_resource(
            "sorting-network",
            "Sorting Network",
            "Description of sorting network",
            "SortingNetworkResourceGenerator",
        )
        url = reverse("resources:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertQuerysetEqual(
            response.context["all_resources"],
            [
                "<Resource: Binary Cards>",
                "<Resource: Sorting Network>",
            ],
            transform=repr,
        )
