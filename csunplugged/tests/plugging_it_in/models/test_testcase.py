from plugging_it_in.models import TestCase

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class TestCaseModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()

    def create_testcase(self):
        topic = self.test_data.create_topic(1)
        difficulty = self.test_data.create_difficulty_level(1)
        challenge = self.test_data.create_programming_challenge(topic, 1, difficulty)

        self.test_data.create_programming_challenge_test_case(1, challenge)
        self.test_case = TestCase.objects.get(id=1)

    def test_testcase_verbose_model_name(self):
        self.create_testcase()
        verbose_name = self.test_case._meta.verbose_name
        self.assertEquals(verbose_name, "Test Case")
