from http import HTTPStatus
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class ProgrammingChallengeViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = TopicsTestDataGenerator()

    def test_programming_challenge_view_with_valid_slugs(self):
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
        }
        url = reverse("topics:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_programming_challenge_view_with_invalid_topic_slug(self):
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
        }
        url = reverse("topics:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_view_with_invalid_challenge_slug(self):
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
        }
        url = reverse("topics:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)

    def test_programming_challenge_view_topic_context(self):
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
        }
        url = reverse("topics:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["topic"],
            topic
        )

    def test_programming_challenge_view_lessons_context(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson1 = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        lesson2 = self.test_data.create_lesson(
            topic,
            2,
            age_group_1
        )
        difficulty = self.test_data.create_difficulty_level(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.add_challenge_lesson_relationship(
            challenge,
            lesson1,
            1,
            1
        )
        self.test_data.add_challenge_lesson_relationship(
            challenge,
            lesson2,
            1,
            2
        )
        kwargs = {
            "topic_slug": topic.slug,
            "programming_challenge_slug": challenge.slug,
        }
        url = reverse("topics:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context["lessons"],
            [
                "<Lesson: Lesson 1 (5 to 7)>",
                "<Lesson: Lesson 2 (5 to 7)>",
            ],
            ordered=False,
        )

    def test_programming_challenge_view_learning_outcomes_context(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        learning_outcome = self.test_data.create_learning_outcome(1)
        challenge.learning_outcomes.add(learning_outcome)
        kwargs = {
            "topic_slug": topic.slug,
            "programming_challenge_slug": challenge.slug,
        }
        url = reverse("topics:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context["learning_outcomes"],
            ["<LearningOutcome: Outcome 1>"]
        )

    def test_programming_challenge_view_learning_outcomes_context_order(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        learning_outcome3 = self.test_data.create_learning_outcome(3)
        challenge.learning_outcomes.add(learning_outcome3)
        learning_outcome2 = self.test_data.create_learning_outcome(2)
        challenge.learning_outcomes.add(learning_outcome2)
        learning_outcome1 = self.test_data.create_learning_outcome(1)
        challenge.learning_outcomes.add(learning_outcome1)
        kwargs = {
            "topic_slug": topic.slug,
            "programming_challenge_slug": challenge.slug,
        }
        url = reverse("topics:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context["learning_outcomes"],
            [
                "<LearningOutcome: Outcome 1>",
                "<LearningOutcome: Outcome 2>",
                "<LearningOutcome: Outcome 3>",
            ]
        )

    # Created to avoid https://github.com/uccser/cs-unplugged/issues/827
    def test_programming_challenge_view_ages_context_learning_outcome_not_duplicated(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        learning_outcome = self.test_data.create_learning_outcome(1)
        area_1 = self.test_data.create_curriculum_area(1)
        area_2 = self.test_data.create_curriculum_area(2)
        learning_outcome.curriculum_areas.add(area_1, area_2)
        challenge.learning_outcomes.add(learning_outcome)
        kwargs = {
            "topic_slug": topic.slug,
            "programming_challenge_slug": challenge.slug,
        }
        url = reverse("topics:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context["learning_outcomes"],
            ["<LearningOutcome: Outcome 1>"]
        )

    def test_programming_challenge_view_implementations_context(self):
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
        }
        url = reverse("topics:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context["implementations"],
            ["<ProgrammingChallengeImplementation: Language 1 for challenge 1.1, Challenge 1.1: 1>"]
        )

    def test_programming_challenge_view_implementations_context_order(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language1 = self.test_data.create_programming_language(1)
        language2 = self.test_data.create_programming_language(2)
        language3 = self.test_data.create_programming_language(3)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge_implementation(
            topic,
            language3,
            challenge,
        )
        self.test_data.create_programming_challenge_implementation(
            topic,
            language2,
            challenge,
        )
        self.test_data.create_programming_challenge_implementation(
            topic,
            language1,
            challenge,
        )
        kwargs = {
            "topic_slug": topic.slug,
            "programming_challenge_slug": challenge.slug,
        }
        url = reverse("topics:programming_challenge", kwargs=kwargs)
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context["implementations"],
            [
                "<ProgrammingChallengeImplementation: Language 1 for challenge 1.1, Challenge 1.1: 1>",
                "<ProgrammingChallengeImplementation: Language 2 for challenge 1.1, Challenge 1.1: 1>",
                "<ProgrammingChallengeImplementation: Language 3 for challenge 1.1, Challenge 1.1: 1>",
            ]
        )
