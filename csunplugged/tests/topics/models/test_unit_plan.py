from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class UnitPlanModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()

    def test_unit_plan_str(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        self.assertEqual(unit_plan.__str__(), "Unit Plan 1")

    def test_unit_plan_model_name(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        self.assertEqual(unit_plan.MODEL_NAME, "Unit Plan")

    def test_unit_plan_model_get_absolute_url(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        self.assertEqual(
            unit_plan.get_absolute_url(),
            "/en/topics/topic-1/unit-plan-1/"
        )
