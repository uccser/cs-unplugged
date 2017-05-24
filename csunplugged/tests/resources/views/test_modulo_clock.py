from django.urls import reverse

from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator

from utils.create_query_string import query_string


class ModuloClockResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_modulo_clock_resource_form_view(self):
        resource = self.test_data.create_test_resource(
            "modulo-clock",
            "Modulo Clock",
            "resources/modulo-clock.html",
            "modulo_clock.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_modulo_clock_resource_generation_2_a4(self):
        resource = self.test_data.create_test_resource(
            "modulo-clock",
            "Modulo Clock",
            "resources/modulo-clock.html",
            "modulo_clock.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "modulo_number": "2",
            "paper_size": "a4",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Modulo Clock (2 - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def test_modulo_clock_resource_generation_2_letter(self):
        resource = self.test_data.create_test_resource(
            "modulo-clock",
            "Modulo Clock",
            "resources/modulo-clock.html",
            "modulo_clock.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "modulo_number": "2",
            "paper_size": "letter",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Modulo Clock (2 - letter).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def test_modulo_clock_resource_generation_10_a4(self):
        resource = self.test_data.create_test_resource(
            "modulo-clock",
            "Modulo Clock",
            "resources/modulo-clock.html",
            "modulo_clock.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "modulo_number": "10",
            "paper_size": "a4",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Modulo Clock (10 - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def test_modulo_clock_resource_generation_10_letter(self):
        resource = self.test_data.create_test_resource(
            "modulo-clock",
            "Modulo Clock",
            "resources/modulo-clock.html",
            "modulo_clock.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "modulo_number": "10",
            "paper_size": "letter",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Modulo Clock (10 - letter).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def test_modulo_clock_resource_generation_missing_modulo_number_parameter(self):
        resource = self.test_data.create_test_resource(
            "modulo-clock",
            "Modulo Clock",
            "resources/modulo-clock.html",
            "modulo_clock.py",
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

    def test_modulo_clock_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_test_resource(
            "modulo-clock",
            "Modulo Clock",
            "resources/modulo-clock.html",
            "modulo_clock.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "modulo_number": "2",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_modulo_clock_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_test_resource(
            "modulo-clock",
            "Modulo Clock",
            "resources/modulo-clock.html",
            "modulo_clock.py",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "modulo_number": "2",
            "paper_size": "a4",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Modulo Clock (2 - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )
