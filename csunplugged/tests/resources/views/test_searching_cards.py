from http import HTTPStatus
from django.test import tag
from django.urls import reverse
from tests.resources.views.ResourceViewBaseTest import ResourceViewBaseTest
from tests.create_query_string import query_string


@tag("resource")
class SearchingCardsResourceViewTest(ResourceViewBaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_searching_cards_resource_form_view(self):
        resource = self.test_data.create_resource(
            "searching-cards",
            "Searching Cards",
            "resources/searching-cards.html",
            "SearchingCardsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_searching_cards_resource_generation_valid_configurations(self):
        resource = self.test_data.create_resource(
            "searching-cards",
            "Searching Cards",
            "resources/searching-cards.html",
            "SearchingCardsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        base_url = reverse("resources:generate", kwargs=kwargs)
        self.run_valid_configuration_tests(resource, base_url)

    def test_searching_cards_resource_generation_missing_number_cards_parameter(self):
        resource = self.test_data.create_resource(
            "searching-cards",
            "Searching Cards",
            "resources/searching-cards.html",
            "SearchingCardsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "max_number": "99",
            "help_sheet": True,
            "paper_size": "a4",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_searching_cards_resource_generation_missing_max_number_parameter(self):
        resource = self.test_data.create_resource(
            "searching-cards",
            "Searching Cards",
            "resources/searching-cards.html",
            "SearchingCardsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "number_cards": "15",
            "help_sheet": True,
            "paper_size": "a4",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_searching_cards_resource_generation_missing_help_sheet_parameter(self):
        resource = self.test_data.create_resource(
            "searching-cards",
            "Searching Cards",
            "resources/searching-cards.html",
            "SearchingCardsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "number_cards": "15",
            "max_number": "99",
            "paper_size": "a4",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_searching_cards_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_resource(
            "searching-cards",
            "Searching Cards",
            "resources/searching-cards.html",
            "SearchingCardsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "number_cards": "15",
            "max_number": "99",
            "help_sheet": True,
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_searching_cards_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_resource(
            "searching-cards",
            "Searching Cards",
            "resources/searching-cards.html",
            "SearchingCardsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "number_cards": "15",
            "max_number": "99",
            "help_sheet": True,
            "paper_size": "a4",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        filename = "Resource Searching Cards (15 cards - 0 to 99 - with helper sheet - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def subtitle(self, combination):
        """Return text of subtitle for given combination.

        Args:
            combination (dict): Dictionary of a valid combination

        Returns:
            String of subtitle.
        """
        if combination["max_number"] == "blank":
            range_text = "blank"
        elif combination["max_number"] == "cards":
            range_text = "0 to {}".format(combination["number_cards"])
        else:
            range_text = "0 to {}".format(combination["max_number"])

        if combination["help_sheet"]:
            help_text = "with helper sheet"
        else:
            help_text = "without helper sheet"

        text = "{} cards - {} - {} - {}".format(
            combination["number_cards"],
            range_text,
            help_text,
            combination["paper_size"],
        )
        return text
