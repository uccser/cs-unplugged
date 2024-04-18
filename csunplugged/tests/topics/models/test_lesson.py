from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class LessonModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()

    def test_lesson_str(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        self.assertEqual(lesson.__str__(), "Lesson 1 (5 to 7)")

    def test_lesson_model_name(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        self.assertEqual(lesson.MODEL_NAME, "Lesson")

    def test_lesson_model_get_absolute_url(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        self.assertEqual(
            lesson.get_absolute_url(),
            "/en/topics/topic-1/lesson-1/"
        )

    def test_get_filtered_programming_exercises_by_lanaguge(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        self.assertEqual(lesson.MODEL_NAME, "Lesson")

        difficulty = self.test_data.create_difficulty_level(1)
        language1 = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)

        self.test_data.add_challenge_lesson_relationship(
            challenge,
            lesson,
            1,
            1
        )

        # Create an implementation which has a language called "Language 1"
        self.test_data.create_programming_challenge_implementation(
            topic=topic,
            language=language1,
            challenge=challenge
        )

        filtered_challenges = lesson.retrieve_related_programming_challenges("Language 2")

        # No challenges should be returned as there are none that have implemenations with language "Language 2"
        self.assertEqual(len(filtered_challenges), 0)

    def test_get_programming_exercises_without_filter(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        self.assertEqual(lesson.MODEL_NAME, "Lesson")

        difficulty = self.test_data.create_difficulty_level(1)
        language1 = self.test_data.create_programming_language(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)

        self.test_data.add_challenge_lesson_relationship(
            challenge,
            lesson,
            1,
            1
        )

        # Create an implementation which has a language called "Language 1"
        self.test_data.create_programming_challenge_implementation(
            topic=topic,
            language=language1,
            challenge=challenge
        )

        non_filtered_challenges = lesson.retrieve_related_programming_challenges()

        # One challenge should be returned in the non filtered set
        self.assertQuerysetEqual(
            non_filtered_challenges,
            ['<ProgrammingChallenge: Challenge 1.1: 1>'],
            transform=repr,
        )

    def test_get_available_languages(self):
        topic = self.test_data.create_topic(1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            1,
            age_group_1
        )
        self.assertEqual(lesson.MODEL_NAME, "Lesson")

        difficulty = self.test_data.create_difficulty_level(1)
        language1 = self.test_data.create_programming_language(1)
        challenge1 = self.test_data.create_programming_challenge(topic, 1, difficulty)
        challenge2 = self.test_data.create_programming_challenge(topic, 1, difficulty)

        self.test_data.add_challenge_lesson_relationship(
            challenge1,
            lesson,
            1,
            1
        )

        self.test_data.add_challenge_lesson_relationship(
            challenge2,
            lesson,
            2,
            1
        )

        # Create an implementation which has a language called "Language 1"
        self.test_data.create_programming_challenge_implementation(
            topic=topic,
            language=language1,
            challenge=challenge1
        )

        # Create an implementation which has a language called "Language 1"
        self.test_data.create_programming_challenge_implementation(
            topic=topic,
            language=language1,
            challenge=challenge2
        )

        available_languages = lesson.challenge_languages()

        # One distinct language should be returned
        self.assertQuerysetEqual(
            available_languages,
            ['<ProgrammingChallengeLanguage: Language 1>'],
            transform=repr,
        )
