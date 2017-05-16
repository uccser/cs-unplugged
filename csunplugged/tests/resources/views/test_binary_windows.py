import itertools
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator


class BinaryWindowsResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_binary_windows_resource_form_view(self):
        resource = self.test_data.create_test_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "binary_windows.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_binary_windows_resource_generation_valid_configurations(self):
        resource = self.test_data.create_test_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "binary_windows.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        base_url = reverse("resources:generate", kwargs=kwargs)

        valid_options = {
            "number_bits": ["4", "8"],
            "value_type": ["binary", "lightbulb"],
            "dot_counts": ["yes", "no"],
            "paper_size": ["a4", "letter"],
            "header_text": ["", "Example header"],
        }
        valid_option_keys = sorted(valid_options)
        combinations = [dict(zip(valid_option_keys, product)) for product in itertools.product(*(valid_options[valid_option_key] for valid_option_key in valid_option_keys))]  # noqa: E501
        print()
        for combination in combinations:
            print("   - Testing combination: {} ... ".format(combination), end="")
            get_parameters = [
                ("dot_counts", combination["dot_counts"]),
                ("number_bits", combination["number_bits"]),
                ("value_type", combination["value_type"]),
                ("paper_size", combination["paper_size"]),
                ("header_text", combination["header_text"]),
            ]
            url = base_url + self.get_query_string(get_parameters)
            response = self.client.get(url)
            self.assertEqual(200, response.status_code)
            if combination["dot_counts"] == "yes":
                count_text = "with dot counts"
            else:
                count_text = "without dot counts"
            FILENAME_TEMPLATE = "{num_bits} bits - {value} - {count_text}"
            subtitle = FILENAME_TEMPLATE.format(
                num_bits=combination["number_bits"],
                value=combination["value_type"],
                count_text=count_text,
            )
            self.assertEqual(
                response.get("Content-Disposition"),
                'attachment; filename="Resource Binary Windows ({subtitle}).pdf"'.format(subtitle=subtitle)
            )
            print("ok")

    def test_binary_windows_resource_generation_missing_dot_count_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "binary_windows.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("number_bits", "8"),
            ("value_type", "binary"),
            ("paper_size", "a4"),
            ("header_text", "Example header text"),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_binary_windows_resource_generation_missing_number_bits_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "binary_windows.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("dot_counts", "yes"),
            ("value_type", "binary"),
            ("paper_size", "a4"),
            ("header_text", "Example header text"),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_binary_windows_resource_generation_missing_value_type_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "binary_windows.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("dot_counts", "yes"),
            ("number_bits", "8"),
            ("paper_size", "a4"),
            ("header_text", "Example header text"),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_binary_windows_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "binary_windows.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("dot_counts", "yes"),
            ("number_bits", "8"),
            ("value_type", "binary"),
            ("header_text", "Example header text"),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_binary_windows_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_test_resource(
            "binary-windows",
            "Binary Windows",
            "resources/binary-windows.html",
            "binary_windows.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = [
            ("dot_counts", "yes"),
            ("number_bits", "8"),
            ("value_type", "lightbulb"),
            ("paper_size", "a4"),
            ("header_text", ""),
        ]
        url += self.get_query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="Resource Binary Windows (8 bits - lightbulb - with dot counts).pdf"'
        )
