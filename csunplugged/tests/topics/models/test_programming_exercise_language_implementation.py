from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import ProgrammingExercise


class ProgrammingExerciseLanguageImplementationModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()

    def test_implementation(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        exercise = self.test_data.create_programming_exercise(topic, 1, difficulty)
        implementation = self.test_data.create_programming_exercise_implementation(
            topic=topic,
            language=language,
            exercise=exercise
        )
        self.assertEqual(
            ProgrammingExercise.objects.get(slug="exercise-1").implementations.get(language__slug="language-1"),
            implementation
        )

    def test_implementation_str(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language = self.test_data.create_programming_language(1)
        exercise = self.test_data.create_programming_exercise(topic, 1, difficulty)
        implementation = self.test_data.create_programming_exercise_implementation(
            topic=topic,
            language=language,
            exercise=exercise,
        )
        self.assertEqual(
            implementation.__str__(),
            "Language 1 for exercise 1.1, Exercise 1"
        )

    def test_implementation_order(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        language_1 = self.test_data.create_programming_language(1)
        language_2 = self.test_data.create_programming_language(2)
        language_3 = self.test_data.create_programming_language(3)
        language_4 = self.test_data.create_programming_language(4)
        exercise = self.test_data.create_programming_exercise(topic, 1, difficulty)
        self.test_data.create_programming_exercise_implementation(
            topic=topic,
            language=language_4,
            exercise=exercise,
        )
        self.test_data.create_programming_exercise_implementation(
            topic=topic,
            language=language_1,
            exercise=exercise,
        )
        self.test_data.create_programming_exercise_implementation(
            topic=topic,
            language=language_3,
            exercise=exercise,
        )
        self.test_data.create_programming_exercise_implementation(
            topic=topic,
            language=language_2,
            exercise=exercise,
        )
        self.assertQuerysetEqual(
            ProgrammingExercise.objects.get(slug="exercise-1").ordered_implementations(),
            [
                "<ProgrammingExerciseLanguageImplementation: Language 1 for exercise 1.1, Exercise 1>",
                "<ProgrammingExerciseLanguageImplementation: Language 2 for exercise 1.1, Exercise 1>",
                "<ProgrammingExerciseLanguageImplementation: Language 3 for exercise 1.1, Exercise 1>",
                "<ProgrammingExerciseLanguageImplementation: Language 4 for exercise 1.1, Exercise 1>",
            ]
        )
