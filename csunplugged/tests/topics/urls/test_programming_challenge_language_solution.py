from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class ProgrammingChallengeSolutionURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_programming_challenge_solution(self):
        kwargs = {
            "topic_slug": "binary-numbers",
            "programming_challenge_slug": "challenge-1",
            "programming_language_slug": "python",
        }
        url = reverse("topics:programming_challenge_solution", kwargs=kwargs)
        expected_url = "/en/topics/binary-numbers/programming/challenge-1/python-solution/"
        self.assertEqual(url, expected_url)
