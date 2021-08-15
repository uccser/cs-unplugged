from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class ProgrammingChallengeURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_programming_challenge(self):
        kwargs = {
            "topic_slug": "binary-numbers",
            "programming_challenge_slug": "challenge-1",
        }
        url = reverse("topics:programming_challenge", kwargs=kwargs)
        self.assertEqual(url, "/en/topics/binary-numbers/programming/challenge-1/")
