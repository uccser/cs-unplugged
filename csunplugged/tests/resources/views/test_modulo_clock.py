from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator


class ModuloClockResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_modulo_clock_resource_form_view(self):
        resource = self.test_data.create_resource(
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

    def test_modulo_clock_resource_generation_blank_a4_no_header_text(self):
        resource = self.test_data.create_resource(
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
            "modulo_number": "1",
            "paper_size": "a4",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Modulo Clock (blank - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def test_modulo_clock_resource_generation_blank_letter_no_header_text(self):
        resource = self.test_data.create_resource(
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
            "modulo_number": "1",
            "paper_size": "letter",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Modulo Clock (blank - letter).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def test_modulo_clock_resource_generation_blank_a4_header_text(self):
        resource = self.test_data.create_resource(
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
            "modulo_number": "1",
            "paper_size": "a4",
            "header_text": "Modulo Clock"
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Modulo Clock (blank - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def test_modulo_clock_resource_generation_blank_letter_header_text(self):
        resource = self.test_data.create_resource(
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
            "modulo_number": "1",
            "paper_size": "letter",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Modulo Clock (blank - letter).pdf"