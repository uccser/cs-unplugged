import os.path
from unittest.mock import Mock

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
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_unit_plan_configuration(self):
        config_file = "unit-plan-1/unit-plan-1.yaml"

        # create test objects so that lesson exist for age range
        factory = Mock()
        topic = self.test_data.create_topic("1")
        unit_plan = self.test_data.create_unit_plan(topic, "test")
        self.test_data.create_lesson(topic, unit_plan, "1")

        up_loader = UnitPlanLoader(factory, config_file, topic, self.BASE_PATH)
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

    def test_unit_plan_loader_missing_lessons_config_value(self):
        config_file = "unit-plan-1/missing-lessons-config.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")

        up_loader = UnitPlanLoader(factory, config_file, topic, self.BASE_PATH)

        self.assertRaises(
            MissingRequiredFieldError,
            up_loader.load,
        )

    def test_unit_plan_loader_missing_content_text(self):
        config_file = "missing-content/missing-content.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")

        up_loader = UnitPlanLoader(factory, config_file, topic, self.BASE_PATH)

        self.assertRaises(
            EmptyMarkdownFileError,
            up_loader.load,
        )

    def test_unit_plan_loader_missing_name_text(self):
        config_file = "missing-name/missing-name.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")

        up_loader = UnitPlanLoader(factory, config_file, topic, self.BASE_PATH)

        self.assertRaises(
            NoHeadingFoundInMarkdownFileError,
            up_loader.load,
        )

    def test_unit_plan_missing_age_groups(self):
        config_file = "unit-plan-1/missing-age-groups.yaml"

        factory = Mock()
        topic = self.test_data.create_topic("1")

        up_loader = UnitPlanLoader(factory, config_file, topic, self.BASE_PATH)

        self.assertRaises(
            MissingRequiredFieldError,
            up_loader.load,
        )
