from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class CurriculumIntegrationModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()

    def test_curriculum_integration_str(self):
        topic = self.test_data.create_topic(1)
        curriculum_integration = self.test_data.create_integration(topic, 1)
        self.assertEqual(curriculum_integration.__str__(), "Integration 1")

    def test_curriculum_integration_model_type(self):
        topic = self.test_data.create_topic(1)
        curriculum_integration = self.test_data.create_integration(topic, 1)
        self.assertEqual(curriculum_integration.model_type(), "Curriculum Integration")

    def test_curriculum_integration_model_get_absolute_url(self):
        topic = self.test_data.create_topic(1)
        curriculum_integration = self.test_data.create_integration(topic, 1)
        self.assertEqual(
            curriculum_integration.get_absolute_url(),
            "/en/topics/topic-1/integrations/integration-1/"
        )
