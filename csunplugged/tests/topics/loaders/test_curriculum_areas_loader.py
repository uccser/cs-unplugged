import os.path
from django.utils import translation
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import CurriculumArea
from topics.management.commands._CurriculumAreasLoader import CurriculumAreasLoader
from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.EmptyYAMLFileError import EmptyYAMLFileError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError


class CurriculumAreasLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "curriculum_areas"
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_curriculum_areas_loader_config(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()
        self.assertQuerysetEqual(
            CurriculumArea.objects.all(),
            ["<CurriculumArea: Maths>"],
            transform=repr,
        )

    def test_curriculum_areas_loader_missing_configuration_file(self):
        config_file = "missing.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            CouldNotFindYAMLFileError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_empty_configuration_file(self):
        config_file = "empty.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            EmptyYAMLFileError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_slug_value(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="maths").slug,
            "maths",
        )

    def test_curriculum_areas_loader_correct_name_value(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="maths").name,
            "Maths",
        )

    def test_curriculum_areas_loader_missing_data(self):
        config_file = "missing-data.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_missing_name_value(self):
        config_file = "missing-name.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_number_value(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="maths").number,
            1,
        )

    def test_curriculum_areas_loader_missing_number_value(self):
        config_file = "missing-number.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_colour_value(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="maths").colour,
            "blue",
        )

    def test_curriculum_areas_loader_missing_colour_value(self):
        config_file = "missing-colour.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_children_value(self):
        config_file = "children.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()
        self.assertQuerysetEqual(
            CurriculumArea.objects.all(),
            [
                "<CurriculumArea: Maths>",
                "<CurriculumArea: Maths: Algebra>",
                "<CurriculumArea: Maths: Geometry>",
            ],
            ordered=False,
            transform=repr,
        )
        parent = CurriculumArea.objects.get(slug="maths")
        self.assertQuerysetEqual(
            CurriculumArea.objects.filter(parent=parent),
            [
                "<CurriculumArea: Maths: Algebra>",
                "<CurriculumArea: Maths: Geometry>",
            ],
            ordered=False,
            transform=repr,
        )

    def test_curriculum_areas_loader_missing_children_value(self):
        config_file = "basic-config.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()
        self.assertQuerysetEqual(
            CurriculumArea.objects.all(),
            ["<CurriculumArea: Maths>"],
            transform=repr,
        )

    def test_curriculum_areas_loader_empty_children_value(self):
        config_file = "empty-children.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_children_slug_value(self):
        config_file = "children.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()
        self.assertEqual(
            CurriculumArea.objects.get(slug="algebra").slug,
            "algebra",
        )

    def test_curriculum_areas_loader_children_name_empty(self):
        config_file = "children-name-empty.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            InvalidYAMLValueError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_children_name_value(self):
        config_file = "children.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="algebra").name,
            "Algebra",
        )

    def test_curriculum_areas_loader_missing_children_name_value(self):
        config_file = "missing-children-name.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            area_loader.load,
        )

    def test_curriculum_areas_loader_correct_children_number_value(self):
        config_file = "children.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="algebra").number,
            1,
        )

    def test_curriculum_areas_loader_correct_children_colour_value(self):
        config_file = "children.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()
        self.assertEquals(
            CurriculumArea.objects.get(slug="algebra").colour,
            "blue",
        )

    def test_curriculum_areas_loader_multiple_configuration(self):
        config_file = "multiple.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
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
            transform=repr,
        )

    def test_curriculum_areas_loader_translation(self):
        config_file = "translation.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()

        translated = CurriculumArea.objects.get(slug="translated")
        self.assertSetEqual(set(["en", "de"]), set(translated.languages))
        self.assertEqual("English Name", translated.name)
        with translation.override("de"):
            self.assertEqual("German Name", translated.name)

    def test_curriculum_areas_loader_missing_translation(self):
        config_file = "translation.yaml"
        area_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        area_loader.load()

        translated = CurriculumArea.objects.get(slug="untranslated")
        self.assertSetEqual(set(["en"]), set(translated.languages))
        self.assertEqual("English Name", translated.name)
        # Check name does not fall back to english for missing translation
        with translation.override("de"):
            self.assertEqual("", translated.name)

    def test_insert_middle(self):
        config_file = "multiple.yaml"

        ca_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        ca_loader.load()

        ca_objects = CurriculumArea.objects.all()
        self.assertQuerysetEqual(
            ca_objects,
            [
                "<CurriculumArea: Maths: Algebra>",
                "<CurriculumArea: Maths: Geometry>",
                "<CurriculumArea: Maths>",
                "<CurriculumArea: Science>",
                "<CurriculumArea: Art>",
            ],
            ordered=False,
            transform=repr,
        )

        config_file = "insert-middle.yaml"

        ca_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        ca_loader.load()

        ca_objects = CurriculumArea.objects.all()

        self.assertQuerysetEqual(
            ca_objects,
            [
                "<CurriculumArea: Maths>",
                "<CurriculumArea: Maths: Algebra>",
                "<CurriculumArea: Maths: Geometry>",
                "<CurriculumArea: Literacy>",
                "<CurriculumArea: Science>",
                "<CurriculumArea: Art>",
            ],
            ordered=False,
            transform=repr,
        )

    def test_delete_end(self):
        config_file = "multiple.yaml"

        ca_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        ca_loader.load()

        ca_objects = CurriculumArea.objects.all()
        self.assertQuerysetEqual(
            ca_objects,
            [
                "<CurriculumArea: Maths>",
                "<CurriculumArea: Maths: Algebra>",
                "<CurriculumArea: Maths: Geometry>",
                "<CurriculumArea: Science>",
                "<CurriculumArea: Art>",
            ],
            ordered=False,
            transform=repr,
        )

        config_file = "delete-end.yaml"

        ca_loader = CurriculumAreasLoader(structure_filename=config_file, base_path=self.base_path)
        ca_loader.load()

        ca_objects = CurriculumArea.objects.all()
        print("ca_objects", ca_objects)
        self.assertQuerysetEqual(
            ca_objects,
            [
                "<CurriculumArea: Maths>",
                "<CurriculumArea: Maths: Algebra>",
                "<CurriculumArea: Maths: Geometry>",
                "<CurriculumArea: Science>",
            ],
            ordered=False,
            transform=repr,
        )
