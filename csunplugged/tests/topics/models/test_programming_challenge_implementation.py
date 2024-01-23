from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import ProgrammingChallenge


class ProgrammingChallengeImplementationModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()

    def test_implementation(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        implementation = self.test_data.create_programming_challenge_implementation(
            topic=topic,
            language=language,
            challenge=challenge
        )
        self.assertEqual(
            ProgrammingChallenge.objects.get(slug="challenge-1").implementations.get(language__slug="language-1"),
            implementation
        )

    def test_implementation_str(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        implementation = self.test_data.create_programming_challenge_implementation(
            topic=topic,
            language=language,
            challenge=challenge,
        )
        self.assertEqual(
            implementation.__str__(),
            "Language 1 for challenge 1.1, Challenge 1.1: 1"
        )

    def test_implementation_order(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language_1 = self.test_data.create_programming_language(1)
        language_2 = self.test_data.create_programming_language(2)
        language_3 = self.test_data.create_programming_language(3)
        language_4 = self.test_data.create_programming_language(4)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)
        self.test_data.create_programming_challenge_implementation(
            topic=topic,
            language=language_4,
            challenge=challenge,
        )
        self.test_data.create_programming_challenge_implementation(
            topic=topic,
            language=language_1,
            challenge=challenge,
        )
        self.test_data.create_programming_challenge_implementation(
            topic=topic,
            language=language_3,
            challenge=challenge,
        )
        self.test_data.create_programming_challenge_implementation(
            topic=topic,
            language=language_2,
            challenge=challenge,
        )
        self.assertQuerysetEqual(
            ProgrammingChallenge.objects.get(slug="challenge-1").ordered_implementations(),
            [
                "<ProgrammingChallengeImplementation: Language 1 for challenge 1.1, Challenge 1.1: 1>",
                "<ProgrammingChallengeImplementation: Language 2 for challenge 1.1, Challenge 1.1: 1>",
                "<ProgrammingChallengeImplementation: Language 3 for challenge 1.1, Challenge 1.1: 1>",
                "<ProgrammingChallengeImplementation: Language 4 for challenge 1.1, Challenge 1.1: 1>",
            ],
            transform=repr,
        )
