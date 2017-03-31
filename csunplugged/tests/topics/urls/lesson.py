from tests.BaseTest import BaseTest
from django.urls import reverse


class LessonURLTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_valid_lesson(self):
        url = reverse('topics:lesson', args=['binary-numbers', 'unit-plan', 'lesson-1'])
        self.assertEqual(url, '/en/topics/binary-numbers/unit-plan/lesson/lesson-1/')
