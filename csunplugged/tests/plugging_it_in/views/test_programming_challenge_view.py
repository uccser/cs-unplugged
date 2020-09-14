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
            "programming_challenge_slug": self.challenge.slug,
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_programming_challenge_view_with_invalid_topic_slug(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": "wrong_slug",
            "lesson_slug": self.lesson.slug,
            "programming_challenge_slug": self.challenge.slug,
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_view_with_invalid_lesson_slug(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": "wrong_slug",
            "programming_challenge_slug": self.challenge.slug,
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_view_with_invalid_challenge_slug(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "programming_challenge_slug": "wrong_slug",
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_view_topic_context(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "programming_challenge_slug": self.challenge.slug,
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
            "programming_challenge_slug": self.challenge.slug,
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
            "programming_challenge_slug": self.challenge.slug,
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
            "programming_challenge_slug": self.challenge.slug,
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)

        # TODO - assert the json context
        # Should only return the first challenge with the python language
        # Not sure how to assert this - the challenge object doesn't seem to become json easily
        # This is returned [{"topic_id": 15, "id": 18, "slug": "cha[259 chars]1"}]
        # If acheiving this statically is also difficult as finding the topic id...
        # self.assertEqual(
        #     response.context["programming_exercises_json"],
        #     {"slug": self.challenge.slug,
        #     "difficulty_id": self.difficulty.id,
        #     "languages": ["python"]
        #     }
        # )

    def test_programming_challenge_view_test_cases_context(self):
        self.create_challenge()
        self.test_data.create_programming_challenge_test_case(
            1,
            self.challenge
        )
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "programming_challenge_slug": self.challenge.slug,
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)

        # TODO: this returns the test cases queryset values() - its in a weird semi json format...
        # Perhaps it can be done such that the testcases are returned and the values are only used when creating the json version
        # self.assertQuerysetEqual(
        #     response.context["test_cases"],
        #     [
        #         "<TestCase: TestCase object (1)>",
        #     ]
        # )

    def test_programming_challenge_view_test_cases_json_context(self):
        self.create_challenge()
        test_test_case = self.test_data.create_programming_challenge_test_case(
            1,
            self.challenge
        )
        test_test_case.question_type = "input"
        test_test_case.expected_input = "test_input"
        test_test_case.expected_output = "test_output"

        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "programming_challenge_slug": self.challenge.slug,
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)

        # TODO: the get related test cases uses select_related not sure if this is needed.
        # This will get rid of number and languages I'd imagine. Thinking a query will need to be made to get the challenge and test case ids.
        # self.assertQuerysetEqual(
        #     response.context["test_cases_json"],
        #     [{"id": "?", "languages": [], "number": 1, "test_input": "test_input", "expected_output": "test_output", "question_type": "input", "challenge_id": "?"}]
        # )

    def test_programming_challenge_view_jobe_proxy_url_context(self):
        self.create_challenge()
        kwargs = {
            "topic_slug": self.topic.slug,
            "lesson_slug": self.lesson.slug,
            "programming_challenge_slug": self.challenge.slug,
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
            "programming_challenge_slug": self.challenge.slug,
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["saved_attempts"],
            {"test_session": "testing"}
        )
