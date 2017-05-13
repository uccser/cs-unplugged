from django.urls import reverse

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TestDataGenerator import TestDataGenerator


class AllCurriculumIntegrationViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TestDataGenerator()

    def test_all_curriculum_integration_view_with_no_integrations(self):
        url = reverse("topics:all_curriculum_integrations")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["curriculum_integrations"]), 0)

    def test_all_curriculum_integration_view_with_one_integration(self):
        topic = self.test_data.create_topics_test_data.create_test_topic(1)
        self.test_data.create_topics_test_data.create_test_integration(topic, 1)

        url = reverse("topics:all_curriculum_integrations")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["curriculum_integrations"]), 1)
        self.assertQuerysetEqual(
            response.context["curriculum_integrations"],
            ["<CurriculumIntegration: Integration 1>"]
        )

    def test_all_curriculum_integration_view_with_multiple_integration(self):
        topic = self.test_data.create_topics_test_data.create_test_topic(1)
        self.test_data.create_topics_test_data.create_test_integration(topic, 1)
        self.test_data.create_topics_test_data.create_test_integration(topic, 2)
        self.test_data.create_topics_test_data.create_test_integration(topic, 3)

        url = reverse("topics:all_curriculum_integrations")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["curriculum_integrations"]), 3)
        self.assertQuerysetEqual(
            response.context["curriculum_integrations"],
            [
                "<CurriculumIntegration: Integration 1>",
                "<CurriculumIntegration: Integration 2>",
                "<CurriculumIntegration: Integration 3>",
            ]
        )

    def test_all_curriculum_integration_view_order(self):
        topic_1 = self.test_data.create_topics_test_data.create_test_topic(1)
        topic_2 = self.test_data.create_topics_test_data.create_test_topic(2)
        self.test_data.create_topics_test_data.create_test_integration(topic_2, 3)
        self.test_data.create_topics_test_data.create_test_integration(topic_2, 2)
        self.test_data.create_topics_test_data.create_test_integration(topic_2, 1)
        self.test_data.create_topics_test_data.create_test_integration(topic_1, 4)
        self.test_data.create_topics_test_data.create_test_integration(topic_1, 5)
        self.test_data.create_topics_test_data.create_test_integration(topic_1, 6)

        url = reverse("topics:all_curriculum_integrations")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.context["curriculum_integrations"]), 6)
        self.assertQuerysetEqual(
            response.context["curriculum_integrations"],
            [
                "<CurriculumIntegration: Integration 4>",
                "<CurriculumIntegration: Integration 5>",
                "<CurriculumIntegration: Integration 6>",
                "<CurriculumIntegration: Integration 1>",
                "<CurriculumIntegration: Integration 2>",
                "<CurriculumIntegration: Integration 3>",
            ]
        )
