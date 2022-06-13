from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class IndexViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_pii_index_view_with_valid_slug(self):
        self.test_data.create_topic(1)
        url = reverse("plugging_it_in:index")
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_pii_index_view_topics_context_without_programming_challenge(self):
        self.test_data.create_topic(1)
        url = reverse("plugging_it_in:index")
        response = self.client.get(url)
        self.assertEqual(
            response.context["programming_topics"],
            []
        )

    def test_pii_index_view_topics_context_with_programming_challenge(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
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

        url = reverse("plugging_it_in:index")
        response = self.client.get(url)
        self.assertEqual(
            response.context["programming_topics"],
            [topic]
        )

    def test_pii_index_view_grouped_lessons_context_with_programming_challenges(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
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

        url = reverse("plugging_it_in:index")
        response = self.client.get(url)
        self.assertEqual(
            len(response.context["programming_topics"][0].grouped_lessons),
            1
        )
        grouped_lessons = response.context["programming_topics"][0].grouped_lessons
        for (age_group, lessons) in grouped_lessons.items():
            self.assertEqual(repr(age_group), "<AgeGroup: NumericRange(5, 7, '[)')>")
            self.assertEqual(
                lessons,
                [lesson]
            )

    def test_pii_index_view_grouped_lessons_context_with_lesson_without_programming_challenges(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )

        lesson_with_programming_exercise = self.test_data.create_lesson(
            topic,
            2,
            age_group_1
        )

        difficulty = self.test_data.create_difficulty_level(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.add_challenge_lesson_relationship(
            challenge,
            lesson_with_programming_exercise,
            1,
            1
        )

        url = reverse("plugging_it_in:index")
        response = self.client.get(url)

        # Should only return one of the lessons
        grouped_lessons = response.context["programming_topics"][0].grouped_lessons
        self.assertEqual(
            len(grouped_lessons),
            1
        )

        for (age_group, lessons) in grouped_lessons.items():
            self.assertEqual(repr(age_group), "<AgeGroup: NumericRange(5, 7, '[)')>")
            self.assertEqual(
                lessons,
                [lesson_with_programming_exercise]
            )

    def test_pii_index_view_templates(self):
        self.test_data.create_topic(1)
        url = reverse("plugging_it_in:index")
        response = self.client.get(url)
        template_found = False
        for template in response.templates:
            if template.name == "plugging_it_in/index.html":
                template_found = True
        self.assertTrue(template_found)
