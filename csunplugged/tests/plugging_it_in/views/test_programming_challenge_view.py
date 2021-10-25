import json

from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import (
    ProgrammingChallengeLanguage
)


class ProgrammingChallengeViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def create_challenge(self):
        self.topic = self.test_data.create_topic(1)
        self.unit_plan = self.test_data.create_unit_plan(self.topic, 1)
        self.age_group = self.test_data.create_age_group(5, 7)
        self.lesson = self.test_data.create_lesson(
            self.topic,
            self.unit_plan,
            1,
            self.age_group
        )
        self.difficulty = self.test_data.create_difficulty_level(1)
        self.challenge = self.test_data.create_programming_challenge(self.topic, 1, self.difficulty)
        self.test_data.add_challenge_lesson_relationship(
            self.challenge,
            self.lesson,
            1,
            1
        )

    def test_programming_challenge_view_with_valid_slugs(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "challenge_slug": self.challenge.slug,
            "language_slug": "python",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_programming_challenge_view_with_invalid_topic_slug(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": "wrong_slug",
            "lesson_slug": self.lesson.slug,
            "challenge_slug": self.challenge.slug,
            "language_slug": "python",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_view_with_invalid_lesson_slug(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": "wrong_slug",
            "challenge_slug": self.challenge.slug,
            "language_slug": "python",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_view_with_invalid_language_slug(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "challenge_slug": self.challenge.slug,
            "language_slug": "wrong_slug",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_view_with_invalid_challenge_slug(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "challenge_slug": "wrong_slug",
            "language_slug": "python",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_view_topic_context(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "challenge_slug": self.challenge.slug,
            "language_slug": "python",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            self.topic
        )

    def test_programming_challenge_view_lesson_context(self):
        self.create_challenge()
        lesson2 = self.test_data.create_lesson(
            self.topic,
            self.unit_plan,
            2,
            self.age_group
        )
        self.test_data.add_challenge_lesson_relationship(
            self.challenge,
            lesson2,
            1,
            2
        )
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "challenge_slug": self.challenge.slug,
            "language_slug": "python"
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)

        # It should only return the first lesson which corresponds with the slug
        self.assertEqual(
            response.context["lesson"],
            self.lesson
        )

    def test_programming_challenge_view_programming_challenges_context(self):
        self.create_challenge()
        challenge2 = self.test_data.create_programming_challenge(self.topic, 2, self.difficulty)

        # Creating the programming challenge language for python manually
        python_language = ProgrammingChallengeLanguage(
            slug="python",
            name="Python",
            number=1,
            languages=["en"],
        )
        python_language.save()
        other_language = self.test_data.create_programming_language(2)

        self.test_data.add_challenge_lesson_relationship(
            challenge2,
            self.lesson,
            1,
            2
        )

        # Add implementations
        self.test_data.create_programming_challenge_implementation(
            self.topic,
            python_language,
            self.challenge,
        )
        self.test_data.create_programming_challenge_implementation(
            self.topic,
            other_language,
            self.challenge,
        )

        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "challenge_slug": self.challenge.slug,
            "language_slug": "python",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)

        # Should only return the first challenge with the python language
        self.assertQuerysetEqual(
            response.context["programming_challenges"],
            ["<ProgrammingChallenge: Challenge 1.1: 1>"]
        )

    def test_programming_challenge_view_programming_challenges_json_context(self):
        self.create_challenge()
        challenge2 = self.test_data.create_programming_challenge(self.topic, 2, self.difficulty)

        # Creating the programming challenge language for python manually
        python_language = ProgrammingChallengeLanguage(
            slug="python",
            name="Python",
            number=1,
            languages=["en"],
        )
        python_language.save()
        other_language = self.test_data.create_programming_language(2)

        self.test_data.add_challenge_lesson_relationship(
            challenge2,
            self.lesson,
            1,
            2
        )
        self.test_data.create_programming_challenge_implementation(
            self.topic,
            python_language,
            self.challenge,
        )
        self.test_data.create_programming_challenge_implementation(
            self.topic,
            other_language,
            challenge2,
        )

        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "challenge_slug": self.challenge.slug,
            "language_slug": "python",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)

        self.assertEqual(
            response.context["programming_exercises_json"],
            json.dumps(list(self.lesson.retrieve_related_programming_challenges("Python").values()))
        )

    def test_programming_challenge_view_test_cases_context(self):
        self.create_challenge()
        test_case = self.test_data.create_programming_challenge_test_case(
            1,
            self.challenge
        )
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "challenge_slug": self.challenge.slug,
            "language_slug": "python",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)

        self.assertQuerysetEqual(
            response.context["test_cases"],
            [
                f"<TestCase: TestCase object ({test_case.pk})>",
            ]
        )

    def test_programming_challenge_view_test_cases_json_context(self):
        self.create_challenge()
        test_test_case = self.test_data.create_programming_challenge_test_case(
            1,
            self.challenge
        )
        test_test_case.question_type = "input"
        test_test_case.expected_input = "test_input"
        test_test_case.expected_output = "test_output"
        test_test_case.save()

        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "challenge_slug": self.challenge.slug,
            "language_slug": "python",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)

        self.assertEqual(
            response.context["test_cases_json"],
            json.dumps(list(self.challenge.related_test_cases().values()))
        )

    def test_programming_challenge_view_jobe_proxy_url_context(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "challenge_slug": self.challenge.slug,
            "language_slug": "python"
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["jobe_proxy_url"],
            reverse('plugging_it_in:jobe_proxy')
        )

    def test_programming_challenge_view_saved_attempts_context(self):
        self.create_challenge()

        # Setting the session manually
        session = self.client.session
        session['saved_attempts'] = {"test_session": "testing"}
        session.save()

        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "challenge_slug": self.challenge.slug,
            "language_slug": "python",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["saved_attempts"],
            {"test_session": "testing"}
        )
