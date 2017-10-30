import os.path
from unittest.mock import Mock

from django.utils import translation

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.NoHeadingFoundInMarkdownFileError import NoHeadingFoundInMarkdownFileError

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import UnitPlan
from topics.management.commands._UnitPlanLoader import UnitPlanLoader


class UnitPlanLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "unit_plan"
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_unit_plan_configuration(self):
        content_path, structure_filename = "unit-plan-1", "unit-plan-1.yaml"

        # create test objects so that lesson exist for age group
        factory = Mock()
        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "test")
        self.test_data.create_lesson(topic, unit_plan, "1")
        self.test_data.create_age_group(8, 10)

        up_loader = UnitPlanLoader(
            factory,
            topic,
            structure_filename=structure_filename,
            base_path=self.base_path,
            content_path=content_path
        )
        up_loader.load()

        up_objects = UnitPlan.objects.all()

        self.assertQuerysetEqual(
            up_objects,
            [
                "<UnitPlan: Unit Plan test>",
                "<UnitPlan: Unit Plan 1>"
            ],
            ordered=False
        )

        up = UnitPlan.objects.get(slug="unit-plan-1")
        self.assertSetEqual(set(["en"]), set(up.languages))

    def test_unit_plan_loader_missing_lessons_config_value(self):
        content_path, structure_filename = "unit-plan-1", "missing-lessons-config.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")

        up_loader = UnitPlanLoader(
            factory,
            topic,
            structure_filename=structure_filename,
            base_path=self.base_path,
            content_path=content_path
        )

        self.assertRaises(
            MissingRequiredFieldError,
            up_loader.load,
        )

    def test_unit_plan_loader_missing_content_text(self):
        content_path, structure_filename = "missing-content", "missing-content.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")

        up_loader = UnitPlanLoader(
            factory,
            topic,
            structure_filename=structure_filename,
            base_path=self.base_path,
            content_path=content_path
        )

        self.assertRaises(
            EmptyMarkdownFileError,
            up_loader.load,
        )

    def test_unit_plan_loader_missing_name_text(self):
        content_path, structure_filename = "missing-name", "missing-name.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")

        up_loader = UnitPlanLoader(
            factory,
            topic,
            structure_filename=structure_filename,
            base_path=self.base_path,
            content_path=content_path
        )

        self.assertRaises(
            NoHeadingFoundInMarkdownFileError,
            up_loader.load,
        )

    def test_unit_plan_missing_age_groups(self):
        content_path, structure_filename = "unit-plan-1", "missing-age-groups.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")

        up_loader = UnitPlanLoader(
            factory,
            topic,
            structure_filename=structure_filename,
            base_path=self.base_path,
            content_path=content_path
        )

        self.assertRaises(
            MissingRequiredFieldError,
            up_loader.load,
        )

    def test_unit_plan_loader_valid_computational_thinking_content(self):
        content_path, structure_filename = "ct-links", "ct-links.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "test")
        self.test_data.create_lesson(topic, unit_plan, "1")
        self.test_data.create_age_group(8, 10)

        up_loader = UnitPlanLoader(
            factory,
            topic,
            structure_filename=structure_filename,
            base_path=self.base_path,
            content_path=content_path
        )
        up_loader.load()

        self.assertEqual(
            UnitPlan.objects.get(slug="ct-links").computational_thinking_links,
            "<p>CT link text</p>"
        )

    def test_unit_plan_loader_missing_computational_thinking_content(self):
        content_path, structure_filename = "unit-plan-1", "unit-plan-1.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "test")
        self.test_data.create_lesson(topic, unit_plan, "1")
        self.test_data.create_age_group(8, 10)

        up_loader = UnitPlanLoader(
            factory,
            topic,
            structure_filename=structure_filename,
            base_path=self.base_path,
            content_path=content_path
        )
        up_loader.load()

        up_objects = UnitPlan.objects.all()

        self.assertQuerysetEqual(
            up_objects,
            [
                "<UnitPlan: Unit Plan test>",
                "<UnitPlan: Unit Plan 1>"
            ],
            ordered=False
        )

    def test_unit_plan_missing_lesson_keys(self):
        content_path, structure_filename = "unit-plan-1", "missing-lesson-keys.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")
        self.test_data.create_age_group(8, 10)

        up_loader = UnitPlanLoader(
            factory,
            topic,
            structure_filename=structure_filename,
            base_path=self.base_path,
            content_path=content_path
        )

        self.assertRaises(
            MissingRequiredFieldError,
            up_loader.load,
        )

    def test_unit_plan_missing_lesson_number(self):
        content_path, structure_filename = "unit-plan-1", "missing-lesson-number.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "test")
        self.test_data.create_lesson(topic, unit_plan, "1")
        self.test_data.create_age_group(8, 10)

        up_loader = UnitPlanLoader(
            factory,
            topic,
            structure_filename=structure_filename,
            base_path=self.base_path,
            content_path=content_path
        )

        self.assertRaises(
            MissingRequiredFieldError,
            up_loader.load,
        )

    def test_unit_plan_translation(self):
        content_path, structure_filename = "translation", "translation.yaml"

        # create test objects so that lesson exist for age group
        factory = Mock()
        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "test")
        self.test_data.create_lesson(topic, unit_plan, "1")
        self.test_data.create_age_group(8, 10)

        up_loader = UnitPlanLoader(
            factory,
            topic,
            structure_filename=structure_filename,
            base_path=self.base_path,
            content_path=content_path
        )
        up_loader.load()

        up = UnitPlan.objects.get(slug="translation")

        self.assertSetEqual(set(["en", "de"]), set(up.languages))

        self.assertEqual("English Heading", up.name)
        self.assertIn("English unit plan content.", up.content)
        self.assertIn("English CT links content.", up.computational_thinking_links)
        with translation.override("de"):
            self.assertEqual("German Heading", up.name)
            self.assertIn("German unit plan content.", up.content)
            self.assertIn("German CT links content.", up.computational_thinking_links)

    def test_unit_plan_translation_missing_ct_links(self):
        content_path, structure_filename = "translation", "translation-missing-ct-links.yaml"

        # create test objects so that lesson exist for age group
        factory = Mock()
        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "test")
        self.test_data.create_lesson(topic, unit_plan, "1")
        self.test_data.create_age_group(8, 10)

        up_loader = UnitPlanLoader(
            factory,
            topic,
            structure_filename=structure_filename,
            base_path=self.base_path,
            content_path=content_path
        )

        up_loader.load()

        up = UnitPlan.objects.get(slug="translation-missing-ct-links")

        # 'de' should still be an available language as ct_links is optional
        self.assertSetEqual(set(["en", "de"]), set(up.languages))

        self.assertEqual("English Heading", up.name)
        self.assertIn("English unit plan content.", up.content)
        self.assertIn("English CT links content.", up.computational_thinking_links)
        with translation.override("de"):
            self.assertEqual("German Heading", up.name)
            self.assertIn("German unit plan content.", up.content)
            # accessing the untranslated field should not default back to english
            self.assertEqual("", up.computational_thinking_links)
