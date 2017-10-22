from django.test import tag
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from utils.import_resource_module import import_resource_module
from utils.create_query_string import query_string
from utils.resource_valid_test_configurations import resource_valid_test_configurations


@tag('resource_generation')
class SearchingCardsResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
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
        self.assertEqual(200, response.status_code)

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
        resource_module = import_resource_module(resource)
        valid_options = resource_module.valid_options()
        combinations = resource_valid_test_configurations(valid_options)
        print()
        for combination in combinations:
            print("   - Testing combination: {} ... ".format(combination), end="")
            url = base_url + query_string(combination)
            response = self.client.get(url)
            self.assertEqual(200, response.status_code)
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
            subtitle = "{} cards - {} - {} - {}".format(
                combination["number_cards"],
                range_text,
                help_text,
                combination["paper_size"],
            )
            self.assertEqual(
                response.get("Content-Disposition"),
                'attachment; filename="Resource Searching Cards ({subtitle}).pdf"'.format(subtitle=subtitle)
            )
            print("ok")

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
        self.assertEqual(404, response.status_code)

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
        self.assertEqual(404, response.status_code)

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
        self.assertEqual(404, response.status_code)

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
        self.assertEqual(404, response.status_code)

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
        self.assertEqual(200, response.status_code)
        filename = "Resource Searching Cards (15 cards - 0 to 99 - with helper sheet - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )
