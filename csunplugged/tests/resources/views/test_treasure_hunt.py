from http import HTTPStatus
from django.test import tag
from django.urls import reverse
from tests.resources.views.ResourceViewBaseTest import ResourceViewBaseTest
from tests.create_query_string import query_string


@tag("resource")
class TreasureHuntResourceViewTest(ResourceViewBaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_treasure_hunt_resource_form_view(self):
        resource = self.test_data.create_resource(
            "treasure-hunt",
            "Treasure Hunt",
            "resources/treasure-hunt.html",
            "TreasureHuntResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_treasure_hunt_resource_generation_valid_configurations(self):
        resource = self.test_data.create_resource(
            "treasure-hunt",
            "Treasure Hunt",
            "resources/treasure-hunt.html",
            "TreasureHuntResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        base_url = reverse("resources:generate", kwargs=kwargs)
        self.run_valid_configuration_tests(resource, base_url)

    def test_treasure_hunt_resource_generation_missing_prefilled_values_parameter(self):
        resource = self.test_data.create_resource(
            "treasure-hunt",
            "Treasure Hunt",
            "resources/treasure-hunt.html",
            "TreasureHuntResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "number_order": "sorted",
            "instructions": True,
            "art": "colour",
            "paper_size": "letter",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_treasure_hunt_resource_generation_missing_number_order_parameter(self):
        resource = self.test_data.create_resource(
            "treasure-hunt",
            "Treasure Hunt",
            "resources/treasure-hunt.html",
            "TreasureHuntResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "prefilled_values": "hard",
            "instructions": True,
            "art": "colour",
            "paper_size": "letter",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_treasure_hunt_resource_generation_missing_instructions_parameter(self):
        resource = self.test_data.create_resource(
            "treasure-hunt",
            "Treasure Hunt",
            "resources/treasure-hunt.html",
            "TreasureHuntResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "prefilled_values": "hard",
            "number_order": "sorted",
            "art": "colour",
            "paper_size": "letter",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_treasure_hunt_resource_generation_missing_art_parameter(self):
        resource = self.test_data.create_resource(
            "treasure-hunt",
            "Treasure Hunt",
            "resources/treasure-hunt.html",
            "TreasureHuntResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "prefilled_values": "hard",
            "number_order": "sorted",
            "instructions": True,
            "paper_size": "letter",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_treasure_hunt_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_resource(
            "treasure-hunt",
            "Treasure Hunt",
            "resources/treasure-hunt.html",
            "TreasureHuntResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "prefilled_values": "hard",
            "number_order": "sorted",
            "instructions": True,
            "art": "colour",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_treasure_hunt_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_resource(
            "treasure-hunt",
            "Treasure Hunt",
            "resources/treasure-hunt.html",
            "TreasureHuntResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "prefilled_values": "hard",
            "number_order": "sorted",
            "instructions": True,
            "art": "colour",
            "paper_size": "letter",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        filename = "Resource Treasure Hunt (Sorted - 0 to 9999 - full colour - with instructions - letter).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )
