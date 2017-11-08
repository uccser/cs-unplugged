from http import HTTPStatus
from django.test import tag
from django.urls import reverse
from tests.resources.views.ResourceViewBaseTest import ResourceViewBaseTest
from tests.create_query_string import query_string


@tag("resource")
class BinaryWindowsResourceViewTest(ResourceViewBaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        self.run_valid_configuration_tests(resource, base_url)

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

    def subtitle(self, combination):
        """Return text of subtitle for given combination.

        Args:
            combination (dict): Dictionary of a valid combination

        Returns:
            String of subtitle.
        """
        if combination["dot_counts"]:
            count_text = "with dot counts"
        else:
            count_text = "without dot counts"
        text = "{} bits - {} - {} - {}".format(
            combination["number_bits"],
            combination["value_type"],
            count_text,
            combination["paper_size"],
        )
        return text
