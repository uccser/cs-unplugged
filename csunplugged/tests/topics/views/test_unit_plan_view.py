from django.urls import reverse

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class UnitPlanViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_unit_plan_view_with_valid_slugs(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_unit_plan_view_with_invalid_topic_slug(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": "wrong_slug",
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_unit_plan_view_with_invalid_unit_plan_slug(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": "wrong_slug",
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_unit_plan_view_topic_context(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            topic
        )

    def test_unit_plan_view_lessons_context(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            5,
            7
        )
        self.test_data.create_lesson(
            topic,
            unit_plan,
            2,
            5,
            7
        )
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["lessons"]),
            2
        )
        self.assertQuerysetEqual(
            response.context["lessons"],
            [
                "<Lesson: Lesson 1 (5 to 7)>",
                "<Lesson: Lesson 2 (5 to 7)>",
            ]
        )

    def test_curriculum_integration_view_prerequisite_lessons_context_order(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            8,
            10
        )
        self.test_data.create_lesson(
            topic,
            unit_plan,
            2,
            5,
            7
        )
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            5,
            7
        )
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["lessons"]),
            3
        )
        self.assertQuerysetEqual(
            response.context["lessons"],
            [
                "<Lesson: Lesson 1 (5 to 7)>",
                "<Lesson: Lesson 2 (5 to 7)>",
                "<Lesson: Lesson 1 (8 to 10)>",
            ]
        )

    def test_unit_plan_view_templates(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        template_found = False
        for template in response.templates:
            if template.name == "topics/unit-plan.html":
                template_found = True
        self.assertTrue(template_found)
