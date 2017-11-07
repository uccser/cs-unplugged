"""Module for the testing custom Django resource commands."""

from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management
from django.test import tag
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from PyPDF2 import PdfFileReader


@tag("management")
class MakeResourcesCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"
        self.RESOURCE_PATH = "staticfiles/resources/{}"

    def test_makeresources_command_single_resource(self):
        self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        management.call_command("makeresources")
        filepath = self.RESOURCE_PATH.format("Resource Grid (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = self.RESOURCE_PATH.format("Resource Grid (letter).pdf")
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
        filepath = self.RESOURCE_PATH.format("Resource Grid (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = self.RESOURCE_PATH.format("Resource Grid (letter).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = self.RESOURCE_PATH.format("Resource Arrows (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = self.RESOURCE_PATH.format("Resource Arrows (letter).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)

    def test_makeresources_command_single_resource_with_copies(self):
        self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
            copies=True
        )
        management.call_command("makeresources")
        filepath = self.RESOURCE_PATH.format("Resource Grid (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 20)
