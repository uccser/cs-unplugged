from http import HTTPStatus
from django.test import tag
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from resources.utils.get_resource_generator import get_resource_generator
from utils.create_query_string import query_string
from resources.utils.resource_valid_test_configurations import resource_valid_test_configurations


@tag('resource_generation')
class BinaryWindowsResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_binary_windows_resource_form_view(self):
        resource = self.test_data.create_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "BinaryWindowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_binary_windows_resource_generation_valid_configurations(self):
        resource = self.test_data.create_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "BinaryWindowsResourceGenerator",
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
            self.assertEqual(HTTPStatus.OK, response.status_code)
            if combination["dot_counts"]:
                count_text = "with dot counts"
            else:
                count_text = "without dot counts"
            TEMPLATE = "{} bits - {} - {} - {}"
            subtitle = TEMPLATE.format(
                combination["number_bits"],
                combination["value_type"],
                count_text,
                combination["paper_size"],
            )
            self.assertEqual(
                response.get("Content-Disposition"),
                'attachment; filename="Resource Binary Windows ({subtitle}).pdf"'.format(subtitle=subtitle)
            )
            print("ok")

    def test_binary_windows_resource_generation_missing_dot_count_parameter(self):
        resource = self.test_data.create_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "BinaryWindowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "number_bits": "8",
            "value_type": "binary",
            "paper_size": "a4",
            "header_text": "Example header text",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_binary_windows_resource_generation_missing_number_bits_parameter(self):
        resource = self.test_data.create_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "BinaryWindowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "dot_counts": "yes",
            "value_type": "binary",
            "paper_size": "a4",
            "header_text": "Example header text",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_binary_windows_resource_generation_missing_value_type_parameter(self):
        resource = self.test_data.create_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "BinaryWindowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "dot_counts": "yes",
            "number_bits": "8",
            "paper_size": "a4",
            "header_text": "Example header text",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_binary_windows_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "BinaryWindowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "dot_counts": "yes",
            "number_bits": "8",
            "value_type": "binary",
            "header_text": "Example header text",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_binary_windows_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "BinaryWindowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "dot_counts": "yes",
            "number_bits": "8",
            "value_type": "lightbulb",
            "paper_size": "a4",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary Windows (8 bits - lightbulb - with dot counts - a4).pdf"'
        )
