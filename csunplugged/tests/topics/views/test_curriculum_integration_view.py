from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class CurriculumIntegrationViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_curriculum_integration_view_with_valid_slugs(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_integration(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "integration_slug": "integration-1",
        }
        url = reverse("topics:integration", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_curriculum_integration_view_with_invalid_topic_slug(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_integration(topic, 1)
        kwargs = {
            "topic_slug": "no-slug",
            "integration_slug": "integration-1",
        }
        url = reverse("topics:integration", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_curriculum_integration_view_with_invalid_integration_slug(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_integration(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "integration_slug": "integration-2",
        }
        url = reverse("topics:integration", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_curriculum_integration_view_topic_context(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_integration(topic, 1)
        kwargs = {
            "topic_slug": "topic-1",
            "integration_slug": "integration-1",
        }
        url = reverse("topics:integration", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            topic
        )

    def test_curriculum_integration_view_curriculum_areas_context(self):
        topic = self.test_data.create_topic(1)
        area_1 = self.test_data.create_curriculum_area(1)
        area_2 = self.test_data.create_curriculum_area(2)
        self.test_data.create_integration(
            topic,
            1,
            curriculum_areas=[area_1, area_2]
        )
        kwargs = {
            "topic_slug": "topic-1",
            "integration_slug": "integration-1",
        }
        url = reverse("topics:integration", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["integration_curriculum_areas"]),
            2
        )
        self.assertQuerysetEqual(
            response.context["integration_curriculum_areas"],
            [
                "<CurriculumArea: Area 1>",
                "<CurriculumArea: Area 2>",
            ],
            transform=repr,
        )

    def test_curriculum_integration_view_prerequisite_lessons_context(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson_1 = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        lesson_2 = self.test_data.create_lesson(
            topic,
            2,
            age_group_1
        )
        self.test_data.create_integration(
            topic,
            1,
            lessons=[lesson_1, lesson_2]
        )
        kwargs = {
            "topic_slug": "topic-1",
            "integration_slug": "integration-1",
        }
        url = reverse("topics:integration", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["prerequisite_lessons"]),
            2
        )
        self.assertQuerysetEqual(
            response.context["prerequisite_lessons"],
            [
                "<Lesson: Lesson 1 (5 to 7)>",
                "<Lesson: Lesson 2 (5 to 7)>",
            ],
            transform=repr,
        )
