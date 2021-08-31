from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class ProgrammingChallengeURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_programming_challenge(self):
        kwargs = {
            "topic_slug": "binary-numbers",
            "lesson_slug": "lesson-1",
            "challenge_slug": "challenge-1",
            "language_slug": "python"
        }
        url = reverse("plugging_it_in:programming_challenge", kwargs=kwargs)
        self.assertEqual(url, "/en/plugging-it-in/binary-numbers/lesson-1/challenge-1/python/")
