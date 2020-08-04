from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class LessonsViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_pii_topic_view_with_valid_slug(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": topic.slug
        }
        url = reverse("plugging_it_in:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_pii_topic_view_with_invalid_slug(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": "wrong_slug",
        }
        url = reverse("plugging_it_in:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_pii_topic_view_topic_context(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": topic.slug
        }
        url = reverse("plugging_it_in:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            topic
        )

    def test_pii_topic_view_lessons_context_with_programming_challenge(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )

        difficulty = self.test_data.create_difficulty_level(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.add_challenge_lesson_relationship(
            challenge,
            lesson,
            1,
            1
        )

        kwargs = {
            "topic_slug": topic.slug
        }
        url = reverse("plugging_it_in:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["grouped_lessons"]),
            1
        )
        grouped_lessons = response.context["grouped_lessons"]
        for (age_group, lessons) in grouped_lessons.items():
            self.assertEqual(repr(age_group), "<AgeGroup: NumericRange(5, 7, '[)')>")
            self.assertEqual(
                lessons,
                [lesson]
            )

    def test_pii_topic_view_lessons_context_without_programming_challenge(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )

        kwargs = {
            "topic_slug": topic.slug
        }
        url = reverse("plugging_it_in:topic", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["grouped_lessons"]),
            0
        )

    def test_pii_topic_view_templates(self):
        topic = self.test_data.create_topic(1)
        self.test_data.create_unit_plan(topic, 1)
        kwargs = {
            "topic_slug": topic.slug
        }
        url = reverse("plugging_it_in:topic", kwargs=kwargs)
        response = self.client.get(url)
        template_found = False
        for template in response.templates:
            if template.name == "plugging_it_in/topic.html":
                template_found = True
        self.assertTrue(template_found)
