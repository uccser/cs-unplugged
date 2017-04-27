from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class ProgrammingExerciseURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = 'en'

    def test_valid_programming_exercise(self):
        url = reverse('topics:programming_exercise', args=['binary-numbers', 'unit-plan', 'lesson-1', 'exercise-1'])
        self.assertEqual(url, '/en/topics/binary-numbers/unit-plan/lesson/lesson-1/plugged-in/exercise-1')
