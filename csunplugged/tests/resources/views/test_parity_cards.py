from http import HTTPStatus
from django.test import tag
from django.urls import reverse
from tests.resources.views.ResourceViewBaseTest import ResourceViewBaseTest
from tests.create_query_string import query_string


@tag("resource")
class ParityCardsResourceViewTest(ResourceViewBaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_parity_cards_resource_form_view(self):
        resource = self.test_data.create_resource(
            "parity-cards",
            "Parity Cards",
            "resources/parity-cards.html",
            "ParityCardsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_parity_cards_resource_generation_valid_configurations(self):
        resource = self.test_data.create_resource(
            "parity-cards",
            "Parity Cards",
            "resources/parity-cards.html",
            "ParityCardsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        base_url = reverse("resources:generate", kwargs=kwargs)
        self.run_valid_configuration_tests(resource, base_url)

    def test_parity_cards_resource_generation_missing_back_colour_parameter(self):
        resource = self.test_data.create_resource(
            "parity-cards",
            "Parity Cards",
            "resources/parity-cards.html",
            "ParityCardsResourceGenerator",
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

    def test_parity_cards_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_resource(
            "parity-cards",
            "Parity Cards",
            "resources/parity-cards.html",
            "ParityCardsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "back_colour": "black",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_parity_cards_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_resource(
            "parity-cards",
            "Parity Cards",
            "resources/parity-cards.html",
            "ParityCardsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "back_colour": "black",
            "paper_size": "a4",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        filename = "Resource Parity Cards (black back - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )
