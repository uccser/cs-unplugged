from tests.BaseTest import BaseTest
from django.urls import reverse


class ProgrammingExerciseDifficultyURLTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)
    
    def test_valid_programming_exercise_difficulty(self):
        url = reverse('topics:programming_exercise_difficulty', args=['1'])
        self.assertEqual(url, '/en/topics/plugged-in/difficulty/1')

