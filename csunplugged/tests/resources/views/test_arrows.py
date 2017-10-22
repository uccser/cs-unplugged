from django.test import tag
from django.urls import reverse

from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator

from utils.create_query_string import query_string


@tag('resource_generation')
class ArrowsResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_arrows_resource_form_view(self):
        resource = self.test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_arrows_resource_generation_a4_no_header_text(self):
        resource = self.test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "paper_size": "a4",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Arrows (a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def test_arrows_resource_generation_a4_header_text(self):
        resource = self.test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "paper_size": "a4",
            "header_text": "Arrows"
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Arrows (a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def test_arrows_resource_generation_letter_header_text(self):
        resource = self.test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "paper_size": "letter",
            "header_text": "Arrows"
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Arrows (letter).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def test_arrows_resource_generation_letter_no_header_text(self):
        resource = self.test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "paper_size": "letter",
            "header_text": ""
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Arrows (letter).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )

    def test_arrows_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_arrows_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "paper_size": "a4",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Arrows (a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )
