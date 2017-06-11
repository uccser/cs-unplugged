from tests.BaseTestWithDB import BaseTestWithDB
from django.urls import reverse


class ProgrammingChallengesListURLTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_programming_challenges_list(self):
        url = reverse("topics:programming_challenges_list", args=["binary-numbers", "unit-plan", "lesson-1"])
        self.assertEqual(url, "/en/topics/binary-numbers/unit-plan/lesson-1/programming/")
