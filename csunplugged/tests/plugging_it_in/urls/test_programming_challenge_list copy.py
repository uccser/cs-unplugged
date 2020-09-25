from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class ProgrammingChallengeListURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_lesson_programming_challenge_list(self):
        kwargs = {
            "topic_slug": "binary-numbers",
            "lesson_slug": "lesson-1",
        }
        url = reverse("plugging_it_in:lesson", kwargs=kwargs)
        self.assertEqual(url, "/en/plugging-it-in/binary-numbers/lesson-1/")
