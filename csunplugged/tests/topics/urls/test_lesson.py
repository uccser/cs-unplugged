from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class LessonURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_lesson(self):
        kwargs = {
            "topic_slug": "binary-numbers",
            "lesson_slug": "lesson-1",
        }
        url = reverse("topics:lesson", kwargs=kwargs)
        self.assertEqual(url, "/en/topics/binary-numbers/lesson-1/")
