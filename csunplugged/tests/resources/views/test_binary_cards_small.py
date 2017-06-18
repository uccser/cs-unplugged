import itertools
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from utils.import_resource_module import import_resource_module
from utils.create_query_string import query_string


class BinaryCardsSmallResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_binary_cards_small_resource_form_view(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "binary_cards_small.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_binary_cards_small_resource_generation_valid_configurations(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "binary_cards_small.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        base_url = reverse("resources:generate", kwargs=kwargs)
        resource_module = import_resource_module(resource)
        valid_options = resource_module.valid_options()
        valid_options["header_text"] = ["", "Example header"]
        valid_option_keys = sorted(valid_options)
        combinations = [dict(zip(valid_option_keys, product)) for product in itertools.product(*(valid_options[valid_option_key] for valid_option_key in valid_option_keys))]  # noqa: E501
        print()
        for combination in combinations:
            print(combination)
            print("   - Testing combination: {} ... ".format(combination), end="")
            url_combination = {}
            for parameter in combination:
                if combination[parameter] is True:
                    url_combination[parameter] = "yes"
                elif combination[parameter] is False:
                    url_combination[parameter] = "no"
                else:
                    url_combination[parameter] = combination[parameter]
            url = base_url + query_string(url_combination)
            response = self.client.get(url)
            self.assertEqual(200, response.status_code)
            if combination["dot_counts"] is True:
                display_numbers_text = "with dot counts"
            else:
                display_numbers_text = "without dot counts"
            if combination["black_back"] is True:
                black_back_text = "with black back"
            else:
                black_back_text = "without black back"
            subtitle = "{} bits - {} - {} - {}".format(
                combination["number_bits"],
                display_numbers_text,
                black_back_text,
                combination["paper_size"],
            )
            self.assertEqual(
                response.get("Content-Disposition"),
                'attachment; filename="Resource Binary Cards (small) ({subtitle}).pdf"'.format(subtitle=subtitle)
            )
            print("ok")

    def test_binary_cards_small_resource_generation_missing_dot_count_parameter(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "binary_cards_small.py",
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
        self.assertEqual(404, response.status_code)

    def test_binary_cards_small_resource_generation_missing_number_bits_parameter(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "binary_cards_small.py",
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
        self.assertEqual(404, response.status_code)

    def test_binary_cards_small_resource_generation_missing_black_back_parameter(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "binary_cards_small.py",
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
        self.assertEqual(404, response.status_code)

    def test_binary_cards_small_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "binary_cards_small.py",
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
        self.assertEqual(404, response.status_code)

    def test_binary_cards_small_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_resource(
            "binary-cards",
            "Binary Cards (small)",
            "resources/binary-cards-small.html",
            "binary_cards_small.py",
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
        self.assertEqual(200, response.status_code)
        filename = "Resource Binary Cards (small) (4 bits - with dot counts - with black back - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )
