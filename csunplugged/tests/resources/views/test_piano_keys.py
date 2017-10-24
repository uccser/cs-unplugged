from django.test import tag
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from utils.get_resource_generator import get_resource_generator
from utils.create_query_string import query_string
from utils.resource_valid_test_configurations import resource_valid_test_configurations
from utils.bool_to_yes_no import bool_to_yes_no


@tag('resource_generation')
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
            "PianoKeysResourceGenerator",
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
            "PianoKeysResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        base_url = reverse("resources:generate", kwargs=kwargs)
        empty_generator = get_resource_generator(resource.generator_module)
        combinations = resource_valid_test_configurations(
            empty_generator.valid_options
        )
        print()
        for combination in combinations:
            print("   - Testing combination: {} ... ".format(combination), end="")
            url = base_url + query_string(combination)
            response = self.client.get(url)
            self.assertEqual(200, response.status_code)
            subtitle = "{} highlight - {}".format(
                bool_to_yes_no(combination["highlight"]),
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
            "PianoKeysResourceGenerator",
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
            "PianoKeysResourceGenerator",
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
            "PianoKeysResourceGenerator",
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
