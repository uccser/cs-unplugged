import os.path
from django.utils import translation
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from utils.errors.MissingRequiredModelsError import MissingRequiredModelsError
from utils.errors.EmptyYAMLFileError import EmptyYAMLFileError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError
from topics.models import LearningOutcome
from topics.management.commands._LearningOutcomesLoader import LearningOutcomesLoader


class LearningOutcomesLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "learning_outcomes"
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        self.test_data.create_curriculum_area(1)
        config_file = "basic-config.yaml"
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        lo_loader.load()
        lo_objects = LearningOutcome.objects.all()
        self.assertQuerysetEqual(
            lo_objects,
            ["<LearningOutcome: Justify why there aren’t actual 0’s and 1’s zooming around inside a computer.>"]
        )

    def test_missing_configuration_file(self):
        config_file = "missing.yaml"
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            CouldNotFindYAMLFileError,
            lo_loader.load,
        )

    def test_empty_configuration_file(self):
        config_file = "empty.yaml"
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            EmptyYAMLFileError,
            lo_loader.load,
        )

    def test_missing_text(self):
        config_file = "missing-text.yaml"
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredModelsError,
            lo_loader.load
        )

    def test_empty_text(self):
        config_file = "empty-text.yaml"
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            InvalidYAMLValueError,
            lo_loader.load
        )

    def test_curriculum_areas(self):
        config_file = "curriculum-areas.yaml"
        self.test_data.create_curriculum_area("1")
        self.test_data.create_curriculum_area("2")
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        lo_loader.load()
        outcome = LearningOutcome.objects.get(slug="outcome-key")
        self.assertQuerysetEqual(
            outcome.curriculum_areas.order_by("name"),
            [
                "<CurriculumArea: Area 1>",
                "<CurriculumArea: Area 2>",
            ]
        )

    def test_curriculum_areas_undefined(self):
        config_file = "curriculum-areas.yaml"
        self.test_data.create_curriculum_area("1")
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            KeyNotFoundError,
            lo_loader.load
        )

    def test_parent_curriculum_area_raises_exception_when_parent_selected(self):
        config_file = "basic-config.yaml"
        area_1 = self.test_data.create_curriculum_area(1)
        self.test_data.create_curriculum_area(2, parent=area_1)
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            InvalidYAMLValueError,
            lo_loader.load
        )

    def test_translation(self):
        self.test_data.create_curriculum_area(1)
        config_file = "translation.yaml"

        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        lo_loader.load()

        translated = LearningOutcome.objects.get(slug="translated")
        self.assertSetEqual(set(["en", "de"]), set(translated.languages))
        self.assertEqual("English text", translated.text)
        with translation.override("de"):
            self.assertEqual("German text", translated.text)

    def test_missing_translation(self):
        self.test_data.create_curriculum_area(1)
        config_file = "translation.yaml"

        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        lo_loader.load()

        untranslated = LearningOutcome.objects.get(slug="untranslated")
        self.assertSetEqual(set(["en"]), set(untranslated.languages))
        self.assertEqual("English text", untranslated.text)

        # Check name does not fall back to english for missing translation
        with translation.override("de"):
            self.assertEqual("", untranslated.text)

    def test_insert_start(self):
        self.test_data.create_curriculum_area(1)
        config_file = "basic-config.yaml"
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        lo_loader.load()
        lo_objects = LearningOutcome.objects.all()
        self.assertQuerysetEqual(
            lo_objects,
            ["<LearningOutcome: Justify why there aren’t actual 0’s and 1’s zooming around inside a computer.>"]
        )

        config_file = "insert-start.yaml"
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        lo_loader.load()
        lo_objects = LearningOutcome.objects.all()
        self.assertQuerysetEqual(
            lo_objects,
            [
                "<LearningOutcome: Inserted outcome.>",
                "<LearningOutcome: Justify why there aren’t actual 0’s and 1’s zooming around inside a computer.>",
            ]
        )

    def test_delete_start(self):
        self.test_data.create_curriculum_area(1)
        config_file = "insert-start.yaml"
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        lo_loader.load()
        lo_objects = LearningOutcome.objects.all()
        self.assertQuerysetEqual(
            lo_objects,
            [
                "<LearningOutcome: Inserted outcome.>",
                "<LearningOutcome: Justify why there aren’t actual 0’s and 1’s zooming around inside a computer.>",
            ]
        )

        config_file = "basic-config.yaml"
        lo_loader = LearningOutcomesLoader(structure_filename=config_file, base_path=self.base_path)
        lo_loader.load()
        lo_objects = LearningOutcome.objects.all()
        self.assertQuerysetEqual(
            lo_objects,
            ["<LearningOutcome: Justify why there aren’t actual 0’s and 1’s zooming around inside a computer.>"]
        )
