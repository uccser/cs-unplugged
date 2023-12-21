"""Module for the testing custom Django resource commands."""

from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management
from django.test import tag, override_settings
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from pypdf import PdfReader
import os.path
import shutil
from resources.models import Resource

RESOURCE_PATH = "temp/resources/"
LANGUAGE1 = "lang1"
LANGUAGE2 = "lang2"
SINGLE_LANGUAGE = ((LANGUAGE1, LANGUAGE1), )
MULTIPLE_LANGUAGES = ((LANGUAGE1, LANGUAGE1), (LANGUAGE2, LANGUAGE2))


@tag("management")
@override_settings(RESOURCE_GENERATION_LOCATION=RESOURCE_PATH)
@override_settings(RESOURCE_GENERATORS_PACKAGE="tests.resources.management.test_generators")
@override_settings(LANGUAGES=SINGLE_LANGUAGE)
class MakeResourcesCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = LANGUAGE1

    def tearDown(self):
        """Automatically called after each test."""
        if os.path.exists(RESOURCE_PATH):
            shutil.rmtree(RESOURCE_PATH)

    def test_makeresources_command_single_resource(self):
        resource = self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGenerator",
        )
        management.call_command("makeresources")
        filepath = os.path.join(RESOURCE_PATH, self.language, resource.slug, "Resource 1 (a4).pdf")
        pdf = PdfReader(open(filepath, "rb"))
        self.assertEqual(len(pdf.pages), 1)
        filepath = os.path.join(RESOURCE_PATH, self.language, resource.slug, "Resource 1 (letter).pdf")
        pdf = PdfReader(open(filepath, "rb"))
        self.assertEqual(len(pdf.pages), 1)

    def test_makeresources_command_multiple_resources(self):
        resource_1 = self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGenerator",
        )
        resource_2 = self.test_data.create_resource(
            "resource2",
            "Resource 2",
            "Description of resource 2",
            "BareResourceGenerator",
        )
        management.call_command("makeresources")
        filepath = os.path.join(RESOURCE_PATH, self.language, resource_1.slug,  "Resource 1 (a4).pdf")
        pdf = PdfReader(open(filepath, "rb"))
        self.assertEqual(len(pdf.pages), 1)
        filepath = os.path.join(RESOURCE_PATH, self.language, resource_1.slug, "Resource 1 (letter).pdf")
        pdf = PdfReader(open(filepath, "rb"))
        self.assertEqual(len(pdf.pages), 1)
        filepath = os.path.join(RESOURCE_PATH, self.language, resource_2.slug, "Resource 2 (a4).pdf")
        pdf = PdfReader(open(filepath, "rb"))
        self.assertEqual(len(pdf.pages), 1)
        filepath = os.path.join(RESOURCE_PATH, self.language, resource_2.slug, "Resource 2 (letter).pdf")
        pdf = PdfReader(open(filepath, "rb"))
        self.assertEqual(len(pdf.pages), 1)

    def test_makeresources_command_single_resource_with_copies(self):
        resource = self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGeneratorWithCopies",
            copies=True
        )
        management.call_command("makeresources")
        filepath = os.path.join(RESOURCE_PATH, self.language, resource.slug, "Resource 1 (a4).pdf")
        pdf = PdfReader(open(filepath, "rb"))
        self.assertEqual(len(pdf.pages), 20)

    def test_makeresources_command_valid_parameter(self):
        resource = self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGeneratorWithCopies",
            copies=True
        )
        management.call_command("makeresources", "--resource", "resource1")
        filepath = os.path.join(RESOURCE_PATH, self.language, resource.slug, "Resource 1 (a4).pdf")
        pdf = PdfReader(open(filepath, "rb"))
        self.assertEqual(len(pdf.pages), 20)

    def test_makeresources_command_invalid_parameter(self):
        self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGenerator",
            copies=True
        )
        with self.assertRaises(Resource.DoesNotExist):
            management.call_command("makeresources", "--resource", "Invalid Resource")

    def test_makeresources_command_single_resource_existing_folder(self):
        os.makedirs(os.path.dirname(RESOURCE_PATH))
        resource = self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGeneratorWithCopies",
            copies=True
        )
        management.call_command("makeresources", "--resource", "resource1")
        filepath = os.path.join(RESOURCE_PATH, self.language, resource.slug, "Resource 1 (a4).pdf")
        pdf = PdfReader(open(filepath, "rb"))
        self.assertEqual(len(pdf.pages), 20)

    def test_makeresources_command_resource_generator_has_non_enum_options(self):
        self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGeneratorWithNonEnumerableOptions",
        )
        with self.assertRaises(TypeError):
            management.call_command("makeresources")

    @override_settings(LANGUAGES=MULTIPLE_LANGUAGES)
    def test_makeresources_command_all_languages(self):
        resource = self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGenerator",
        )
        management.call_command("makeresources")
        for language_code, _ in MULTIPLE_LANGUAGES:
            filepath = os.path.join(RESOURCE_PATH, language_code, resource.slug, "Resource 1 (a4).pdf")
            pdf = PdfReader(open(filepath, "rb"))
            self.assertEqual(len(pdf.pages), 1)
            filepath = os.path.join(RESOURCE_PATH, language_code, resource.slug, "Resource 1 (letter).pdf")
            pdf = PdfReader(open(filepath, "rb"))
            self.assertEqual(len(pdf.pages), 1)

    @override_settings(LANGUAGES=SINGLE_LANGUAGE)
    def test_makeresources_command_single_language(self):
        resource = self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGenerator",
        )
        management.call_command("makeresources", "--resource", resource.slug, "--language", LANGUAGE1)
        # Check language 1 exists
        filepath = os.path.join(RESOURCE_PATH, LANGUAGE1, resource.slug, "Resource 1 (a4).pdf")
        pdf = PdfReader(open(filepath, "rb"))
        self.assertEqual(len(pdf.pages), 1)
        filepath = os.path.join(RESOURCE_PATH, LANGUAGE1, resource.slug, "Resource 1 (letter).pdf")
        pdf = PdfReader(open(filepath, "rb"))
        self.assertEqual(len(pdf.pages), 1)
        # Check language 2 does not exist
        filepath = os.path.join(RESOURCE_PATH, LANGUAGE2, resource.slug, "Resource 1 (a4).pdf")
        self.assertFalse(os.path.exists(filepath))
        filepath = os.path.join(RESOURCE_PATH, LANGUAGE2, resource.slug, "Resource 1 (letter).pdf")
        self.assertFalse(os.path.exists(filepath))
