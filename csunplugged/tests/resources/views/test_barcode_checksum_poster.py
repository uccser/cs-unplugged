from django.test import tag
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from utils.import_resource_module import import_resource_module
from utils.create_query_string import query_string
from utils.resource_valid_test_configurations import resource_valid_test_configurations


@tag('resource_generation')
class BarcodeChecksumPosterResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_barcode_checksum_poster_resource_form_view(self):
        resource = self.test_data.create_resource(
            "barcode-checksum-poster",
            "Barcode Checksum Poster",
            "resources/barcode-checksum-poster.html",
            "BarcodeChecksumPosterResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_barcode_checksum_poster_resource_generation_valid_configurations(self):
        resource = self.test_data.create_resource(
            "barcode-checksum-poster",
            "Barcode Checksum Poster",
            "resources/barcode-checksum-poster.html",
            "BarcodeChecksumPosterResourceGenerator",
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
            subtitle = "{} digits - {}".format(
                combination["barcode_length"],
                combination["paper_size"],
            )
            self.assertEqual(
                response.get("Content-Disposition"),
                'attachment; filename="Resource Barcode Checksum Poster ({subtitle}).pdf"'.format(subtitle=subtitle)
            )
            print("ok")

    def test_barcode_checksum_poster_resource_generation_missing_barcode_length_parameter(self):
        resource = self.test_data.create_resource(
            "barcode-checksum-poster",
            "Barcode Checksum Poster",
            "resources/barcode-checksum-poster.html",
            "BarcodeChecksumPosterResourceGenerator",
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

    def test_binary_cards_small_resource_generation_missing_paper_size_parameter(self):
        resource = self.test_data.create_resource(
            "barcode-checksum-poster",
            "Barcode Checksum Poster",
            "resources/barcode-checksum-poster.html",
            "BarcodeChecksumPosterResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "barcode_length": "12",
            "header_text": "",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_binary_cards_small_resource_generation_missing_header_text_parameter(self):
        resource = self.test_data.create_resource(
            "barcode-checksum-poster",
            "Barcode Checksum Poster",
            "resources/barcode-checksum-poster.html",
            "BarcodeChecksumPosterResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:generate", kwargs=kwargs)
        get_parameters = {
            "barcode_length": "12",
            "paper_size": "a4",
        }
        url += query_string(get_parameters)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        filename = "Resource Barcode Checksum Poster (12 digits - a4).pdf"
        self.assertEqual(
            response.get("Content-Disposition"),
            'attachment; filename="{}"'.format(filename)
        )
