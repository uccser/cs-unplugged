import os.path

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import CurriculumArea
from topics.management.commands._CurriculumAreasLoader import CurriculumAreasLoader

from utils.errors.CouldNotFindConfigFileError import CouldNotFindConfigFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.EmptyConfigFileError import EmptyConfigFileError


class CurriculumAreasLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "curriculum_areas"
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_curriculum_areas_loader_config(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertQuerysetEqual(
            CurriculumArea.objects.all(),
            ["<CurriculumArea: Maths>"]
        )

    def test_curriculum_areas_loader_missing_configuration_file(self):
        config_file = "missing.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            CouldNotFindConfigFileError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_empty_configuration_file(self):
        config_file = "empty.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            EmptyConfigFileError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_slug_value(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="maths").slug,
            "maths",
        )

    def test_curriculum_areas_loader_correct_name_value(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="maths").name,
            "Maths",
        )

    def test_curriculum_areas_loader_missing_data(self):
        config_file = "missing-data.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_missing_name_value(self):
        config_file = "missing-name.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_number_value(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="maths").number,
            1,
        )

    def test_curriculum_areas_loader_missing_number_value(self):
        config_file = "missing-number.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_colour_value(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="maths").colour,
            "blue",
        )

    def test_curriculum_areas_loader_missing_colour_value(self):
        config_file = "missing-colour.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_children_value(self):
        config_file = "children.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertQuerysetEqual(
            CurriculumArea.objects.all(),
            [
                "<CurriculumArea: Maths>",
                "<CurriculumArea: Maths: Algebra>",
                "<CurriculumArea: Maths: Geometry>",
            ],
            ordered=False,
        )
        parent = CurriculumArea.objects.get(slug="maths")
        self.assertQuerysetEqual(
            CurriculumArea.objects.filter(parent=parent),
            [
                "<CurriculumArea: Maths: Algebra>",
                "<CurriculumArea: Maths: Geometry>",
            ],
            ordered=False,
        )

    def test_curriculum_areas_loader_missing_children_value(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertQuerysetEqual(
            CurriculumArea.objects.all(),
            ["<CurriculumArea: Maths>"],
        )

    def test_curriculum_areas_loader_empty_children_value(self):
        config_file = "empty-children.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_children_slug_value(self):
        config_file = "children.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertEqual(
            CurriculumArea.objects.get(slug="algebra").slug,
            "algebra",
        )

    def test_curriculum_areas_loader_children_name_empty(self):
        config_file = "children-name-empty.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_children_name_value(self):
        config_file = "children.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="algebra").name,
            "Algebra",
        )

    def test_curriculum_areas_loader_missing_children_name_value(self):
        config_file = "missing-children-name.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_children_number_value(self):
        config_file = "children.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="algebra").number,
            1,
        )

    def test_curriculum_areas_loader_correct_children_colour_value(self):
        config_file = "children.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="algebra").colour,
            "blue",
        )

    def test_curriculum_areas_loader_multiple_configuration(self):
        config_file = "multiple.yaml"
        area_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        area_loader.load()
        self.assertQuerysetEqual(
            CurriculumArea.objects.all(),
            [
                "<CurriculumArea: Maths>",
                "<CurriculumArea: Maths: Algebra>",
                "<CurriculumArea: Maths: Geometry>",
                "<CurriculumArea: Science>",
                "<CurriculumArea: Art>",
            ],
            ordered=False,
        )
