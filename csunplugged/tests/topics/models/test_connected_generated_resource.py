from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from topics.models import ConnectedGeneratedResource


class ConnectedGeneratedResourceModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_topics_data = TopicsTestDataGenerator()
        self.test_resources_data = ResourcesTestDataGenerator()

    def test_connected_generated_resource(self):
        resource = self.test_resources_data.create_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "binary_cards.py",
        )
        topic = self.test_topics_data.create_topic(1)
        unit_plan = self.test_topics_data.create_unit_plan(topic, 1)
        age_range = self.test_topics_data.create_age_range(1, 99)
        lesson = self.test_topics_data.create_lesson(topic, unit_plan, age_range, 1)
        new_resource = ConnectedGeneratedResource.objects.create(
            resource=resource,
            lesson=lesson,
            description="this is a description"
        )
        query_result = ConnectedGeneratedResource.objects.get(resource=resource, lesson=lesson)
        self.assertEqual(query_result, new_resource)
