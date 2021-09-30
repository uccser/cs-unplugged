from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from resources.models import Resource
from resources.management.commands._ResourcesLoader import ResourcesLoader
from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.EmptyYAMLFileError import EmptyYAMLFileError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError
from django.utils import translation


class ResourceLoaderTest(BaseTestWithDB):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.loader_name = "resource"
        self.BASE_PATH = "tests/resources/loaders/assets/resource/"

    def test_basic_resource_loader_config(self):
        config_file = "basic-config.yaml"
        resource_loader = ResourcesLoader(structure_filename=config_file, base_path=self.BASE_PATH)
        resource_loader.load()
        resources = Resource.objects.all()
        self.assertEqual(1, len(resources))
        resource = resources[0]
        self.assertEqual("Resource 1", resource.name)
        self.assertIn("Description of resource 1", resource.content)
        self.assertEqual("resource-untranslated", resource.slug)
        self.assertEqual("BareResourceGenerator", resource.generator_module)
        self.assertEqual(False, resource.copies)

    def test_resource_loader_config_missing_translation_fallback(self):
        config_file = "basic-config.yaml"
        resource_loader = ResourcesLoader(structure_filename=config_file, base_path=self.BASE_PATH)
        resource_loader.load()
        resources = Resource.objects.all()
        self.assertEqual(1, len(resources))
        resource = resources[0]
        with translation.override("de"):
            # Name should fall back to English
            self.assertEqual("Resource 1", resource.name)
            # Content should not fall back to English
            self.assertEqual("", resource.content)

    def test_resource_loader_missing_configuration_file(self):
        config_file = "missing.yaml"
        resource_loader = ResourcesLoader(structure_filename=config_file, base_path=self.BASE_PATH)
        self.assertRaises(
            CouldNotFindYAMLFileError,
            resource_loader.load,
        )

    def test_resource_loader_empty_configuration_file(self):
        config_file = "empty.yaml"
        resource_loader = ResourcesLoader(structure_filename=config_file, base_path=self.BASE_PATH)
        self.assertRaises(
            EmptyYAMLFileError,
            resource_loader.load,
        )

    def test_resource_loader_missing_module_value(self):
        config_file = "missing-module.yaml"
        resource_loader = ResourcesLoader(structure_filename=config_file, base_path=self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            resource_loader.load,
        )

    def test_resource_loader_invalid_module_value(self):
        config_file = "invalid-module.yaml"
        resource_loader = ResourcesLoader(structure_filename=config_file, base_path=self.BASE_PATH)
        self.assertRaises(
            AttributeError,
            resource_loader.load,
        )

    def test_resource_loader_trimmed_module_value(self):
        config_file = "trimmed-module.yaml"
        resource_loader = ResourcesLoader(structure_filename=config_file, base_path=self.BASE_PATH)
        resource_loader.load()
        self.assertEquals(
            Resource.objects.get(slug="resource-untranslated").generator_module,
            "BareResourceGenerator",
        )

    def test_resource_loader_missing_copies_value(self):
        config_file = "missing-copies.yaml"
        resource_loader = ResourcesLoader(structure_filename=config_file, base_path=self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            resource_loader.load,
        )

    def test_resource_loader_invalid_copies_value(self):
        config_file = "invalid-copies.yaml"
        resource_loader = ResourcesLoader(structure_filename=config_file, base_path=self.BASE_PATH)
        self.assertRaises(
            InvalidYAMLValueError,
            resource_loader.load,
        )

    def test_resource_loader_multiple_configuration(self):
        config_file = "multiple.yaml"
        resource_loader = ResourcesLoader(structure_filename=config_file, base_path=self.BASE_PATH)
        resource_loader.load()
        self.assertQuerysetEqual(
            Resource.objects.all(),
            [
                "<Resource: Resource 1>",
                "<Resource: Resource 2>",
            ],
            ordered=False,
        )

    def test_resource_loader_translation(self):
        config_file = "translation.yaml"
        resource_loader = ResourcesLoader(structure_filename=config_file, base_path=self.BASE_PATH)
        resource_loader.load()
        resources = Resource.objects.all()
        self.assertEqual(1, len(resources))
        resource = resources[0]
        self.assertEqual("English Resource Name", resource.name)
        self.assertIn("English resource description", resource.content)
        with translation.override("de"):
            self.assertEqual("German Resource Name", resource.name)
            self.assertIn("German resource description", resource.content)
