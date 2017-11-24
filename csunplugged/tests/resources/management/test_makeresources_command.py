"""Module for the testing custom Django resource commands."""

from tests.BaseTestWithDB import BaseTestWithDB
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
@override_settings(RESOURCE_GENERATORS_PACKAGE="tests.resources.management.test_generators")
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
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGenerator",
        )
        management.call_command("makeresources")
        filepath = os.path.join(RESOURCE_PATH, "Resource 1 (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource 1 (letter).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)

    def test_makeresources_command_multiple_resources(self):
        self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGenerator",
        )
        self.test_data.create_resource(
            "resource2",
            "Resource 2",
            "Description of resource 2",
            "BareResourceGenerator",
        )
        management.call_command("makeresources")
        filepath = os.path.join(RESOURCE_PATH, "Resource 1 (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource 1 (letter).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource 2 (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)
        filepath = os.path.join(RESOURCE_PATH, "Resource 2 (letter).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 1)

    def test_makeresources_command_single_resource_with_copies(self):
        self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGeneratorWithCopies",
            copies=True
        )
        management.call_command("makeresources")
        filepath = os.path.join(RESOURCE_PATH, "Resource 1 (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 20)

    def test_makeresources_command_valid_parameter(self):
        self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGeneratorWithCopies",
            copies=True
        )
        management.call_command("makeresources", "Resource 1")
        filepath = os.path.join(RESOURCE_PATH, "Resource 1 (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 20)

    def test_makeresources_command_invalid_parameter(self):
        self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGenerator",
            copies=True
        )
        with self.assertRaises(Resource.DoesNotExist):
            management.call_command("makeresources", "Invalid Resource")

    def test_makeresources_command_single_resource_existing_folder(self):
        os.makedirs(os.path.dirname(RESOURCE_PATH))
        self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGeneratorWithCopies",
            copies=True
        )
        management.call_command("makeresources", "Resource 1")
        filepath = os.path.join(RESOURCE_PATH, "Resource 1 (a4).pdf")
        pdf = PdfFileReader(open(filepath, "rb"))
        self.assertEqual(pdf.getNumPages(), 20)

    def test_makeresources_command_resource_generator_has_non_enum_options(self):
        self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGeneratorWithNonEnumerableOptions",
        )
        with self.assertRaises(TypeError):
            management.call_command("makeresources")
