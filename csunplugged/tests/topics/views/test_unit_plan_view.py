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
        age_range_1 = self.test_data.create_age_range(5, 7)
        lesson1 = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_range_1
        )
        lesson2 = self.test_data.create_lesson(
            topic,
            unit_plan,
            2,
            age_range_1
        )
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["grouped_lessons"]),
            1
        )
        grouped_lessons = response.context["grouped_lessons"]
        for (age_range, lessons) in grouped_lessons.items():
            self.assertEqual(age_range, "<AgeRange: NumericRange(5, 7, '[)')>")
            self.assertEqual(
                lessons,
                [lesson1, lesson2]
            )

    def test_curriculum_integration_view_prerequisite_lessons_context_order(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_range_1 = self.test_data.create_age_range(5, 7)
        age_range_2 = self.test_data.create_age_range(8, 10)
        lesson1 = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_range_2
        )
        lesson2 = self.test_data.create_lesson(
            topic,
            unit_plan,
            2,
            age_range_1
        )
        lesson3 = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_range_1
        )
        kwargs = {
            "topic_slug": topic.slug,
            "unit_plan_slug": unit_plan.slug,
        }
        url = reverse("topics:unit_plan", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["grouped_lessons"]),
            2
        )

        expected_grouped_lessons = [
            ("<AgeRange: NumericRange(5, 7, '[)')>", [lesson3, lesson2]),
            ("<AgeRange: NumericRange(8, 10, '[)')>", [lesson1]),
        ]
        grouped_lessons = response.context["grouped_lessons"]
        i = 0
        for (age_range, lessons) in grouped_lessons.items():
            self.assertEqual(age_range, expected_grouped_lessons[i][0])
            self.assertEqual(
                lessons,
                expected_grouped_lessons[i][1]
            )
            i += 1

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
