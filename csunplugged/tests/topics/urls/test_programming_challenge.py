from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class ProgrammingChallengeURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_programming_challenge(self):
        url = reverse("topics:programming_challenge", args=["binary-numbers", "challenge-1"])
        self.assertEqual(url, "/en/topics/binary-numbers/programming/challenge-1")
