import os.path
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.CouldNotFindConfigFileError import CouldNotFindConfigFileError
from utils.errors.EmptyConfigFileError import EmptyConfigFileError
from topics.models import LearningOutcome
from topics.management.commands._LearningOutcomesLoader import LearningOutcomesLoader


class LearningOutcomesLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "learning_outcomes"
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        config_file = "basic-config.yaml"
        lo_loader = LearningOutcomesLoader(config_file, self.BASE_PATH)
        lo_loader.load()
        lo_objects = LearningOutcome.objects.all()
        self.assertQuerysetEqual(
            lo_objects,
            ["<LearningOutcome: Justify why there aren’t actual 0’s and 1’s zooming around inside a computer.>"]
        )

    def test_missing_configuration_file(self):
        config_file = "missing.yaml"
        lo_loader = LearningOutcomesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            CouldNotFindConfigFileError,
            lo_loader.load,
        )

    def test_empty_configuration_file(self):
        config_file = "empty.yaml"
        lo_loader = LearningOutcomesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            EmptyConfigFileError,
            lo_loader.load,
        )

    def test_missing_text(self):
        config_file = "missing-text.yaml"
        lo_loader = LearningOutcomesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            lo_loader.load
        )

    def test_empty_text(self):
        config_file = "empty-text.yaml"
        lo_loader = LearningOutcomesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            lo_loader.load
        )

    def test_curriculum_areas(self):
        config_file = "curriculum-areas.yaml"
        self.test_data.create_curriculum_area("1")
        self.test_data.create_curriculum_area("2")
        lo_loader = LearningOutcomesLoader(config_file, self.BASE_PATH)
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
        lo_loader = LearningOutcomesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            KeyNotFoundError,
            lo_loader.load
        )
