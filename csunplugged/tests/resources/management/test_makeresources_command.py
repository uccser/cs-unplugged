"""Module for the testing custom Django resource commands."""

from tests.BaseTestWithDB import BaseTestWithDB
from unittest.mock import patch
from django.core import management
from django.test import tag, override_settings
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from PyPDF2 import PdfFileReader
import os.path
import shutil
from resources.models import Resource

RESOURCE_PATH = "temp/resources/"


@tag("management")
@override_settings(RESOURCE_GENERATION_LOCATION=RESOURCE_PATH)
class MakeResourcesCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def tearDown(self):
        """Automatically called after each test."""
        shutil.rmtree(RESOURCE_PATH)

    def test_makeresources_command_single_resource(self):
        self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        management.call_command("makeresources")
        filepath = os.path.join(RESOURCE_PATH, "Resource Grid (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource Grid (letter).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)

    def test_makeresources_command_multiple_resources(self):
        self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        self.test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        management.call_command("makeresources")
        filepath = os.path.join(RESOURCE_PATH, "Resource Grid (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource Grid (letter).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource Arrows (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource Arrows (letter).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)

    def test_makeresources_command_single_resource_with_copies(self):
        self.test_data.create_resource(
            "sortingnetwork",
            "Sorting Network",
            "Sorting network content",
            "SortingNetworkResourceGenerator",
            copies=True
        )
        management.call_command("makeresources")
        filepath = os.path.join(RESOURCE_PATH, "Resource Sorting Network (1 to 9 - a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 20)

    def test_makeresources_command_single_resource_single_parameter(self):
        self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        management.call_command("makeresources", "Resource Grid")
        filepath = os.path.join(RESOURCE_PATH, "Resource Grid (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource Grid (letter).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)

    def test_makeresources_command_multiple_resources_single_parameter(self):
        self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        self.test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        management.call_command("makeresources", "Resource Grid")
        filepath = os.path.join(RESOURCE_PATH, "Resource Grid (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource Grid (letter).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource Arrows (a4).pdf")
        self.assertFalse(os.path.isfile(filepath))
        filepath = os.path.join(RESOURCE_PATH, "Resource Arrows (letter).pdf")
        self.assertFalse(os.path.isfile(filepath))

    def test_makeresources_command_single_resource_with_copies_single_parameter(self):
        self.test_data.create_resource(
            "sortingnetwork",
            "Sorting Network",
            "Sorting network content",
            "SortingNetworkResourceGenerator",
            copies=True
        )
        management.call_command("makeresources", "Resource Sorting Network")
        filepath = os.path.join(RESOURCE_PATH, "Resource Sorting Network (1 to 9 - a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 20)

    def test_makeresources_command_single_resource_existing_folder(self):
        os.makedirs(os.path.dirname(RESOURCE_PATH))
        self.test_data.create_resource(
            "grid",
            "Grid",
            "Grid content",
            "GridResourceGenerator",
        )
        management.call_command("makeresources")
        filepath = os.path.join(RESOURCE_PATH, "Resource Grid (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource Grid (letter).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
