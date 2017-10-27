from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from resources.models import Resource
from resources.management.commands._ResourcesLoader import ResourcesLoader
from utils.errors.CouldNotFindConfigFileError import CouldNotFindConfigFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.EmptyConfigFileError import EmptyConfigFileError
from utils.errors.InvalidConfigValueError import InvalidConfigValueError


class ResourceLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.loader_name = "resource"
        self.BASE_PATH = "tests/resources/loaders/assets/resource/"

    def test_basic_resource_loader_config(self):
        config_file = "basic-config.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        resource_loader.load()
        self.assertQuerysetEqual(
            Resource.objects.all(),
            ["<Resource: Grid>"]
        )

    def test_resource_loader_missing_configuration_file(self):
        config_file = "missing.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            CouldNotFindConfigFileError,
            resource_loader.load,
        )

    def test_resource_loader_empty_configuration_file(self):
        config_file = "empty.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            EmptyConfigFileError,
            resource_loader.load,
        )

    def test_resource_loader_correct_slug_value(self):
        config_file = "basic-config.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        resource_loader.load()
        self.assertEquals(
            Resource.objects.get(slug="grid").slug,
            "grid",
        )

    def test_resource_loader_correct_name_value(self):
        config_file = "basic-config.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        resource_loader.load()
        self.assertEquals(
            Resource.objects.get(slug="grid").name,
            "Grid",
        )

    def test_resource_loader_missing_name_value(self):
        config_file = "missing-name.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            resource_loader.load,
        )

    def test_resource_loader_correct_template_value(self):
        config_file = "basic-config.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        resource_loader.load()
        self.assertEquals(
            Resource.objects.get(slug="grid").webpage_template,
            "resources/grid.html",
        )

    def test_resource_loader_missing_template_value(self):
        config_file = "missing-template.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            resource_loader.load,
        )

    def test_resource_loader_invalid_template_value(self):
        config_file = "invalid-template.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            FileNotFoundError,
            resource_loader.load,
        )

    def test_resource_loader_correct_module_value(self):
        config_file = "basic-config.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        resource_loader.load()
        self.assertEquals(
            Resource.objects.get(slug="grid").generator_module,
            "GridResourceGenerator",
        )

    def test_resource_loader_missing_module_value(self):
        config_file = "missing-module.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            resource_loader.load,
        )

    def test_resource_loader_invalid_module_value(self):
        config_file = "invalid-module.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            ModuleNotFoundError,
            resource_loader.load,
        )

    def test_resource_loader_trimmed_module_value(self):
        config_file = "trimmed-module.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        resource_loader.load()
        self.assertEquals(
            Resource.objects.get(slug="grid").generator_module,
            "GridResourceGenerator",
        )

    def test_resource_loader_correct_thumbnail_value(self):
        config_file = "basic-config.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        resource_loader.load()
        self.assertEquals(
            Resource.objects.get(slug="grid").thumbnail_static_path,
            "img/resources/grid/thumbnail.png",
        )

    def test_resource_loader_missing_thumbnail_value(self):
        config_file = "missing-thumbnail.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            resource_loader.load,
        )

    def test_resource_loader_invalid_thumbnail_value(self):
        config_file = "invalid-thumbnail.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            FileNotFoundError,
            resource_loader.load,
        )

    def test_resource_loader_correct_copies_value(self):
        config_file = "basic-config.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        resource_loader.load()
        self.assertEquals(
            Resource.objects.get(slug="grid").copies,
            False,
        )

    def test_resource_loader_missing_copies_value(self):
        config_file = "missing-copies.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            resource_loader.load,
        )

    def test_resource_loader_invalid_copies_value(self):
        config_file = "invalid-copies.yaml"
        resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            InvalidConfigValueError,
            resource_loader.load,
        )
    #
    # def test_resource_loader_multiple_configuration(self):
    #     config_file = "multiple.yaml"
    #     resource_loader = ResourcesLoader(config_file, self.BASE_PATH)
    #     resource_loader.load()
    #     self.assertQuerysetEqual(
    #         Resource.objects.all(),
    #         [
    #             "<Resource: Maths>",
    #             "<Resource: Maths: Algebra>",
    #             "<Resource: Maths: Geometry>",
    #             "<Resource: Science>",
    #             "<Resource: Art>",
    #         ],
    #         ordered=False,
    #     )
