import os.path
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import CurriculumIntegration
from topics.management.commands._CurriculumIntegrationsLoader import CurriculumIntegrationsLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError


class CurriculumIntegrationsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "curriculum_integrations"

    def test_basic_config(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        ci_loader.load()
        ci_objects = CurriculumIntegration.objects.all()
        self.assertQuerysetEqual(
            ci_objects,
            ["<CurriculumIntegration: Integration 1>"]
        )

    def test_missing_number_key(self):
        config_file = os.path.join(self.loader_name, "missing-number.yaml")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )

    def test_missing_areas_key(self):
        config_file = os.path.join(self.loader_name, "missing-areas.yaml")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )

    def test_blank_number_value(self):
        config_file = os.path.join(self.loader_name, "blank-number.yaml")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )

    def test_blank_areas_value(self):
        config_file = os.path.join(self.loader_name, "blank-areas.yaml")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )

    def test_area_undefined(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            KeyNotFoundError,
            ci_loader.load
        )

    def test_prerequisite_lessons(self):
        config_file = os.path.join(self.loader_name, "prerequisite-lessons.yaml")
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "1")
        self.test_data.create_lesson(topic, unit_plan, "1")
        self.test_data.create_lesson(topic, unit_plan, "2")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        ci_loader.load()
        ci_objects = CurriculumIntegration.objects.all()
        self.assertQuerysetEqual(
            ci_objects,
            ["<CurriculumIntegration: Integration 1>"]
        )
        integration = CurriculumIntegration.objects.get(slug="integration-1")
        self.assertQuerysetEqual(
            integration.prerequisite_lessons.all(),
            [
                "<Lesson: Lesson 1 (none to none)>",
                "<Lesson: Lesson 2 (none to none)>",
            ],
            ordered=False,
        )

    def test_prerequisite_lessons_blank(self):
        config_file = os.path.join(self.loader_name, "prerequisite-lessons-blank.yaml")
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        ci_loader.load()
        ci_objects = CurriculumIntegration.objects.all()
        self.assertQuerysetEqual(
            ci_objects,
            ["<CurriculumIntegration: Integration 1>"]
        )
        integration = CurriculumIntegration.objects.get(slug="integration-1")
        self.assertQuerysetEqual(
            integration.prerequisite_lessons.all(),
            [],
        )

    def test_prerequisite_lessons_blank_lessons(self):
        config_file = os.path.join(self.loader_name, "prerequisite-lessons-blank-lessons.yaml")
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )

    def test_prerequisite_lessons_invalid_lesson(self):
        config_file = os.path.join(self.loader_name, "prerequisite-lessons-invalid-lesson.yaml")
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        self.test_data.create_unit_plan(topic, "1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            KeyNotFoundError,
            ci_loader.load
        )

    def test_prerequisite_lessons_invalid_unit_plan(self):
        config_file = os.path.join(self.loader_name, "prerequisite-lessons-invalid-unit-plan.yaml")
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            KeyNotFoundError,
            ci_loader.load
        )
