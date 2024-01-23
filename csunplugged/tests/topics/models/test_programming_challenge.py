from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import ProgrammingChallenge


class ProgrammingChallengeModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()

    def test_programming_challenge_str(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge_implementation(
            topic,
            language,
            challenge,
        )
        self.assertEqual(challenge.__str__(), "Challenge 1.1: 1")

    def test_programming_challenge_model_name(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge_implementation(
            topic,
            language,
            challenge,
        )
        self.assertEqual(challenge.MODEL_NAME, "Programming Challenge")

    def test_programming_challenge_model_get_absolute_url(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge_implementation(
            topic,
            language,
            challenge,
        )
        self.assertEqual(
            challenge.get_absolute_url(),
            "/en/topics/topic-1/programming/challenge-1/"
        )

    def test_programming_challenge_related_test_cases(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        test_case = self.test_data.create_programming_challenge_test_case(
            1,
            challenge
        )
        self.assertQuerysetEqual(
            ProgrammingChallenge.objects.get(slug="challenge-1").related_test_cases(),
            [
                f"<TestCase: TestCase object ({test_case.pk})>",
            ],
            transform=repr,
        )
