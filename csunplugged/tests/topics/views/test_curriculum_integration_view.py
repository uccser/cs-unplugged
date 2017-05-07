from django.urls import reverse
from model_mommy import mommy
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics import create_topics_test_data
from topics.models import UnitPlan


class CurriculumIntegrationViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_curriculum_integration_view_with_valid_slugs(self):
        topic = create_topics_test_data.create_test_topic(1)
        create_topics_test_data.create_test_integration(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "integration_slug": "integration_1",
            }
        url = reverse("topics:integration", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_curriculum_integration_view_with_invalid_topic_slug(self):
        topic = create_topics_test_data.create_test_topic(1)
        create_topics_test_data.create_test_integration(topic, 1)
        kwargs = {
            "topic_slug": "no_slug",
            "integration_slug": "integration_1",
        }
        url = reverse("topics:integration", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_curriculum_integration_view_with_invalid_integration_slug(self):
        topic = create_topics_test_data.create_test_topic(1)
        create_topics_test_data.create_test_integration(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "integration_slug": "integration_2",
            }
        url = reverse("topics:integration", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_curriculum_integration_view_topic_context(self):
        topic = create_topics_test_data.create_test_topic(1)
        create_topics_test_data.create_test_integration(topic, 1)
        kwargs = {
            "topic_slug": "topic_1",
            "integration_slug": "integration_1",
        }
        url = reverse("topics:integration", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            topic
        )

    def test_curriculum_integration_view_curriculum_areas_context(self):
        topic = create_topics_test_data.create_test_topic(1)
        area_1 = create_topics_test_data.create_test_curriculum_area(1)
        area_2 = create_topics_test_data.create_test_curriculum_area(2)
        create_topics_test_data.create_test_integration(
            topic,
            1,
            curriculum_areas=[area_1, area_2]
        )
        kwargs = {
            "topic_slug": "topic_1",
            "integration_slug": "integration_1",
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
            ]
        )

    def test_curriculum_integration_view_prerequisite_lessons_context(self):
        topic = create_topics_test_data.create_test_topic(1)
        unit_plan = mommy.make(UnitPlan)
        lesson_1 = create_topics_test_data.create_test_lesson(
            topic,
            unit_plan,
            1,
            5,
            7
        )
        lesson_2 = create_topics_test_data.create_test_lesson(
            topic,
            unit_plan,
            2,
            5,
            7
        )
        create_topics_test_data.create_test_integration(
            topic,
            1,
            lessons=[lesson_1, lesson_2]
        )
        kwargs = {
            "topic_slug": "topic_1",
            "integration_slug": "integration_1",
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
            ]
        )

    def test_curriculum_integration_view_prerequisite_lessons_context_order(self):
        topic = create_topics_test_data.create_test_topic(1)
        unit_plan = mommy.make(UnitPlan)
        lesson_3 = create_topics_test_data.create_test_lesson(
            topic,
            unit_plan,
            1,
            8,
            10
        )
        lesson_2 = create_topics_test_data.create_test_lesson(
            topic,
            unit_plan,
            2,
            5,
            7
        )
        lesson_1 = create_topics_test_data.create_test_lesson(
            topic,
            unit_plan,
            1,
            5,
            7
        )
        create_topics_test_data.create_test_integration(
            topic,
            1,
            lessons=[lesson_3, lesson_2, lesson_1]
        )
        kwargs = {
            "topic_slug": "topic_1",
            "integration_slug": "integration_1",
        }
        url = reverse("topics:integration", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["prerequisite_lessons"]),
            3
        )
        self.assertQuerysetEqual(
            response.context["prerequisite_lessons"],
            [
                "<Lesson: Lesson 1 (5 to 7)>",
                "<Lesson: Lesson 2 (5 to 7)>",
                "<Lesson: Lesson 1 (8 to 10)>",
            ]
        )
