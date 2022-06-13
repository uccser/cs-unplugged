from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from topics.models import ResourceDescription


class ResourceDescriptionModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_topics_data = TopicsTestDataGenerator()
        self.test_resources_data = ResourcesTestDataGenerator()

    def test_connected_generated_resource(self):
        resource = self.test_resources_data.create_resource(
            "binary-cards",
            "Binary Cards",
            "resources/binary-cards.html",
            "BinaryCardsResourceGenerator",
        )
        topic = self.test_topics_data.create_topic(1)
        age_group = self.test_topics_data.create_age_group(1, 99)
        lesson = self.test_topics_data.create_lesson(topic, 1, age_group)
        new_resource = ResourceDescription.objects.create(
            resource=resource,
            lesson=lesson,
            description="this is a description"
        )
        query_result = ResourceDescription.objects.get(resource=resource, lesson=lesson)
        self.assertEqual(query_result, new_resource)
