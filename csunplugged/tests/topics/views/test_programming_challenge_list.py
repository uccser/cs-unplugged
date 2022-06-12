from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class ProgrammingChallengeListTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_programming_challenge_list_with_valid_slugs(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        difficulty = self.test_data.create_difficulty_level(1)
        challenge1 = self.test_data.create_programming_challenge(topic, 1, difficulty)
        challenge2 = self.test_data.create_programming_challenge(topic, 2, difficulty)
        self.test_data.add_challenge_lesson_relationship(
            challenge1,
            lesson,
            1,
            1
        )
        self.test_data.add_challenge_lesson_relationship(
            challenge2,
            lesson,
            1,
            2
        )
        kwargs = {
            "topic_slug": topic.slug,
            "lesson_slug": lesson.slug,
        }
        url = reverse("topics:programming_challenges_list", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_programming_challenge_list_with_invalid_topic_slug(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        difficulty = self.test_data.create_difficulty_level(1)
        challenge1 = self.test_data.create_programming_challenge(topic, 1, difficulty)
        challenge2 = self.test_data.create_programming_challenge(topic, 2, difficulty)
        self.test_data.add_challenge_lesson_relationship(
            challenge1,
            lesson,
            1,
            1
        )
        self.test_data.add_challenge_lesson_relationship(
            challenge2,
            lesson,
            1,
            2
        )
        kwargs = {
            "topic_slug": "wrong_slug",
            "lesson_slug": lesson.slug,
        }
        url = reverse("topics:programming_challenges_list", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_list_with_invalid_lesson_slug(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        difficulty = self.test_data.create_difficulty_level(1)
        challenge1 = self.test_data.create_programming_challenge(topic, 1, difficulty)
        challenge2 = self.test_data.create_programming_challenge(topic, 2, difficulty)
        self.test_data.add_challenge_lesson_relationship(
            challenge1,
            lesson,
            1,
            1
        )
        self.test_data.add_challenge_lesson_relationship(
            challenge2,
            lesson,
            1,
            2
        )
        kwargs = {
            "topic_slug": topic.slug,
            "lesson_slug": "wrong_slug",
        }
        url = reverse("topics:programming_challenges_list", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_list_topic_context(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        difficulty = self.test_data.create_difficulty_level(1)
        challenge1 = self.test_data.create_programming_challenge(topic, 1, difficulty)
        challenge2 = self.test_data.create_programming_challenge(topic, 2, difficulty)
        self.test_data.add_challenge_lesson_relationship(
            challenge1,
            lesson,
            1,
            1
        )
        self.test_data.add_challenge_lesson_relationship(
            challenge2,
            lesson,
            1,
            2
        )
        kwargs = {
            "topic_slug": topic.slug,
            "lesson_slug": lesson.slug,
        }
        url = reverse("topics:programming_challenges_list", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            topic
        )

    def test_programming_challenge_list_lesson_context(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        difficulty = self.test_data.create_difficulty_level(1)
        challenge1 = self.test_data.create_programming_challenge(topic, 1, difficulty)
        challenge2 = self.test_data.create_programming_challenge(topic, 2, difficulty)
        self.test_data.add_challenge_lesson_relationship(
            challenge1,
            lesson,
            1,
            1
        )
        self.test_data.add_challenge_lesson_relationship(
            challenge2,
            lesson,
            1,
            2
        )
        kwargs = {
            "topic_slug": topic.slug,
            "lesson_slug": lesson.slug,
        }
        url = reverse("topics:programming_challenges_list", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["lesson"],
            lesson
        )

    def test_programming_challenge_list_challenges_context(self):
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
        kwargs = {
            "topic_slug": topic.slug,
            "lesson_slug": lesson.slug,
        }
        url = reverse("topics:programming_challenges_list", kwargs=kwargs)
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context["programming_challenges"],
            [
                "<ProgrammingChallenge: Challenge 1.1: 1>",
            ]
        )
