from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class ProgrammingExerciseLanguageSolutionURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_valid_programming_exercise_language_solution(self):
        args = ['binary-numbers', 'unit-plan', 'lesson-1', 'exercise-1', 'python']
        url = reverse('topics:programming_exercise_language_solution', args=args)
        expected_url = '/en/topics/binary-numbers/unit-plan/lesson/lesson-1/plugged-in/exercise-1/python-solution'
        self.assertEqual(url, expected_url)
