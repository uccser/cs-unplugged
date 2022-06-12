import os.path
from django.utils import translation
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import CurriculumIntegration
from topics.management.commands._CurriculumIntegrationsLoader import CurriculumIntegrationsLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError


class CurriculumIntegrationsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, "curriculum_integrations")

    def test_basic_config(self):
        config_file = "basic-config.yaml"
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        ci_loader.load()
        ci_objects = CurriculumIntegration.objects.all()
        self.assertEqual(1, len(ci_objects))
        ci = ci_objects[0]
        self.assertSetEqual(set(["en"]), set(ci.languages))
        self.assertEqual("Integration 1", ci.name)
        self.assertIn("English curriculum integration content", ci.content)

    def test_translation(self):
        config_file = "translation.yaml"
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        ci_loader.load()
        ci_objects = CurriculumIntegration.objects.all()
        self.assertQuerysetEqual(
            ci_objects,
            ["<CurriculumIntegration: English Heading>"]
        )

    def test_missing_data(self):
        config_file = "missing-data.yaml"
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )

    def test_missing_number_key(self):
        config_file = "missing-number.yaml"
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )

    def test_missing_curriculum_areas_key(self):
        config_file = "missing-areas.yaml"
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )

    def test_blank_number_value(self):
        config_file = "blank-number.yaml"
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )

    def test_blank_curriculum_areas_value(self):
        config_file = "blank-areas.yaml"
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )

    def test_curriculum_area_undefined(self):
        config_file = "basic-config.yaml"
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        self.assertRaises(
            KeyNotFoundError,
            ci_loader.load
        )

    def test_parent_curriculum_area_raises_exception_when_parent_selected(self):
        config_file = "basic-config.yaml"
        area_1 = self.test_data.create_curriculum_area(1)
        self.test_data.create_curriculum_area(2, parent=area_1)
        topic = self.test_data.create_topic(1)
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        self.assertRaises(
            InvalidYAMLValueError,
            ci_loader.load
        )

    def test_prerequisite_lessons(self):
        config_file = "prerequisite-lessons.yaml"
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        self.test_data.create_lesson(topic, "1")
        self.test_data.create_lesson(topic, "2")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
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
        self.assertEqual(1, len(ci_objects))

    def test_prerequisite_lessons_translation(self):
        config_file = "prerequisite-lessons-translation.yaml"
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        self.test_data.create_lesson(topic, "1")
        self.test_data.create_lesson(topic, "2")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        ci_loader.load()
        ci_objects = CurriculumIntegration.objects.all()
        self.assertQuerysetEqual(
            ci_objects,
            ["<CurriculumIntegration: English Heading>"]
        )
        integration = CurriculumIntegration.objects.get(slug="translation")
        self.assertQuerysetEqual(
            integration.prerequisite_lessons.all(),
            [
                "<Lesson: Lesson 1 (none to none)>",
                "<Lesson: Lesson 2 (none to none)>",
            ],
            ordered=False,
        )
        self.assertEqual(1, len(ci_objects))
        ci = ci_objects[0]
        self.assertSetEqual(set(["en", "de"]), set(ci.languages))
        self.assertEqual("English Heading", ci.name)
        self.assertIn("English curriculum integration content", ci.content)
        with translation.override("de"):
            self.assertEqual("German Heading", ci.name)
            self.assertIn("German curriculum integration content", ci.content)

    def test_prerequisite_lessons_blank(self):
        config_file = "prerequisite-lessons-blank.yaml"
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
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

    def test_prerequisite_lessons_invalid_lesson(self):
        config_file = "prerequisite-lessons-invalid-lesson.yaml"
        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        self.assertRaises(
            KeyNotFoundError,
            ci_loader.load
        )
