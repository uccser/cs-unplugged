from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class ProgrammingChallengeSolutionViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_programming_challenge_solution_view_with_valid_slugs(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge_implementation(
            topic,
            language,
            challenge,
        )
        kwargs = {
            "topic_slug": topic.slug,
            "programming_challenge_slug": challenge.slug,
            "programming_language_slug": language.slug,
        }
        url = reverse("topics:programming_challenge_solution", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_programming_challenge_solution_view_with_invalid_topic_slug(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge_implementation(
            topic,
            language,
            challenge,
        )
        kwargs = {
            "topic_slug": "wrong_slug",
            "programming_challenge_slug": challenge.slug,
            "programming_language_slug": language.slug,
        }
        url = reverse("topics:programming_challenge_solution", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_solution_view_with_invalid_challenge_slug(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge_implementation(
            topic,
            language,
            challenge,
        )
        kwargs = {
            "topic_slug": topic.slug,
            "programming_challenge_slug": "wrong_slug",
            "programming_language_slug": language.slug,
        }
        url = reverse("topics:programming_challenge_solution", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_solution_view_with_invalid_language_slug(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge_implementation(
            topic,
            language,
            challenge,
        )
        kwargs = {
            "topic_slug": topic.slug,
            "programming_challenge_slug": challenge.slug,
            "programming_language_slug": "wrong_slug",
        }
        url = reverse("topics:programming_challenge_solution", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_solution_view_topic_context(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge_implementation(
            topic,
            language,
            challenge,
        )
        kwargs = {
            "topic_slug": topic.slug,
            "programming_challenge_slug": challenge.slug,
            "programming_language_slug": language.slug,
        }
        url = reverse("topics:programming_challenge_solution", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            topic
        )

    def test_programming_challenge_solution_view_challenge_context(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge_implementation(
            topic,
            language,
            challenge,
        )
        kwargs = {
            "topic_slug": topic.slug,
            "programming_challenge_slug": challenge.slug,
            "programming_language_slug": language.slug,
        }
        url = reverse("topics:programming_challenge_solution", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["programming_challenge"],
            challenge
        )
