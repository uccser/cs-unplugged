import itertools
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from utils.import_resource_module import import_resource_module
from utils.create_query_string import query_string


class PianoKeysResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_piano_keys_resource_form_view(self):
        resource = self.test_data.create_resource(
            "piano-keys",
            "Piano Keys",
            "resources/piano-keys.html",
            "piano_keys.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_piano_keys_resource_generation_valid_configurations(self):
        resource = self.test_data.create_resource(
            "piano-keys",
            "Piano Keys",
            "resources/piano-keys.html",
            "piano_keys.py",
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
            print("   - Testing combination: {} ... ".format(combination), end="")
            url = base_url + query_string(combination)
            response = self.client.get(url)
            self.assertEqual(200, response.status_code)
            subtitle = "{} highlight - {}".format(
                combination["highlight"],
                combination["paper_size"],
            )
            self.assertEqual(
                response.get("Content-Disposition"),
                'attachment; filename="Resource Piano Keys ({subtitle}).pdf"'.format(subtitle=subtitle)
            )
            print("ok")

    def test_piano_keys_resource_generation_missing_highlight_parameter(self):
        resource = self.test_data.create_resource(
            "piano-keys",
            "Piano Keys",
            "resources/piano-keys.html",
            "piano_keys.py",
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
        self.assertEqual(404, response.status_code)

    def test_piano_keys_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_resource(
            "piano-keys",
            "Piano Keys",
            "resources/piano-keys.html",
            "piano_keys.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "highlight": "no",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_piano_keys_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_resource(
            "piano-keys",
            "Piano Keys",
            "resources/piano-keys.html",
            "piano_keys.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "highlight": "no",
            "paper_size": "a4",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Piano Keys (no highlight - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )
