from tests.BaseTest import BaseTest
from django.urls import reverse


class ProgrammingExerciseURLTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_valid_programming_exercise(self):
        url = reverse('topics:programming_exercise', args=['binary-numbers', 'unit-plan', 'lesson-1', 'exercise-1'])
        self.assertEqual(url, '/en/topics/binary-numbers/unit-plan/lesson/lesson-1/plugged-in/exercise-1')
