from http import HTTPStatus
from django.test import tag
from django.urls import reverse
from resources.utils.resource_test_valid_configurations import resource_test_valid_configurations
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from utils.create_query_string import query_string


@tag("resource")
class SortingNetworkResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_sorting_network_resource_form_view(self):
        resource = self.test_data.create_resource(
            "sorting-network",
            "Sorting Network",
            "resources/sorting-network.html",
            "SortingNetworkResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_sorting_network_resource_generation_valid_configurations(self):
        resource = self.test_data.create_resource(
            "sorting-network",
            "Sorting Network",
            "resources/sorting-network.html",
            "SortingNetworkResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        base_url = reverse("resources:generate", kwargs=kwargs)

        def subtitle(combination):
            if combination["prefilled_values"] == "blank":
                range_text = "blank"
            elif combination["prefilled_values"] == "easy":
                range_text = "1 to 9"
            elif combination["prefilled_values"] == "medium":
                range_text = "10 to 99"
            else:
                range_text = "100 to 999"
            text = "{} - {}".format(
                range_text,
                combination["paper_size"],
            )
            return text

        resource_test_valid_configurations(self, resource, base_url, subtitle)


    def test_sorting_network_resource_generation_missing_prefilled_values_parameter(self):
        resource = self.test_data.create_resource(
            "sorting-network",
            "Sorting Network",
            "resources/sorting-network.html",
            "SortingNetworkResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "paper_size": "a4",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_sorting_network_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_resource(
            "sorting-network",
            "Sorting Network",
            "resources/sorting-network.html",
            "SortingNetworkResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "prefilled_values": "easy",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_sorting_network_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_resource(
            "sorting-network",
            "Sorting Network",
            "resources/sorting-network.html",
            "SortingNetworkResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "prefilled_values": "easy",
            "paper_size": "a4",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        filename = "Resource Sorting Network (1 to 9 - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )
