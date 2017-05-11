from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class LessonURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_lesson(self):
        url = reverse("topics:lesson", args=["binary-numbers", "unit-plan", "lesson-1"])
        self.assertEqual(url, "/en/topics/binary-numbers/unit-plan/lesson-1/")
