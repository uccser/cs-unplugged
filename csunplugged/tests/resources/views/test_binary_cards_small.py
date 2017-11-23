from http import HTTPStatus
from django.test import tag
from django.urls import reverse
from tests.resources.views.ResourceViewBaseTest import ResourceViewBaseTest
from tests.create_query_string import query_string


@tag("resource")
class BinaryCardsSmallResourceViewTest(ResourceViewBaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_binary_cards_small_resource_form_view(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "BinaryCardsSmallResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_binary_cards_small_resource_generation_valid_configurations(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "BinaryCardsSmallResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        base_url = reverse("resources:generate", kwargs=kwargs)
        self.run_valid_configuration_tests(resource, base_url)

    def test_binary_cards_small_resource_generation_missing_dot_count_parameter(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "BinaryCardsSmallResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "number_bits": "4",
            "black_back": "yes",
            "paper_size": "a4",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_binary_cards_small_resource_generation_missing_number_bits_parameter(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "BinaryCardsSmallResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "dot_counts": "yes",
            "black_back": "yes",
            "paper_size": "a4",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_binary_cards_small_resource_generation_missing_black_back_parameter(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "BinaryCardsSmallResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "number_bits": "4",
            "dot_counts": "yes",
            "paper_size": "a4",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_binary_cards_small_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "BinaryCardsSmallResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "number_bits": "4",
            "dot_counts": "yes",
            "black_back": "yes",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_binary_cards_small_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "BinaryCardsSmallResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "dot_counts": "yes",
            "number_bits": "4",
            "black_back": "yes",
            "paper_size": "a4",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        filename = "Resource Binary Cards (small) (4 bits - with dot counts - with black back - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )
