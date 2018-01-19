"""Module for the testing custom Django commands."""

from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management
from django.test import tag
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


@tag("management")
class ManagementCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_rebuild_index_command_no_items(self):
        management.call_command("rebuild_index", "--noinput")

    def test_rebuild_index_command_one_model(self):
        self.test_data.create_topic(1)
        self.test_data.create_topic(2)
        self.test_data.create_topic(3)
        management.call_command("rebuild_index", "--noinput")

    def test_rebuild_index_command_multiple_models(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        management.call_command("rebuild_index", "--noinput")
