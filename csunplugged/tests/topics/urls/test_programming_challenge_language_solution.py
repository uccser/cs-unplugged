from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class ProgrammingChallengeLanguageSolutionURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_programming_challenge_solution(self):
        args = ["binary-numbers", "challenge-1", "python"]
        url = reverse("topics:programming_challenge_solution", args=args)
        expected_url = "/en/topics/binary-numbers/programming/challenge-1/python-solution"
        self.assertEqual(url, expected_url)
