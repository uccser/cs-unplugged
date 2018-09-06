from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator


class LessonModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()

    def test_lesson_str(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        self.assertEqual(lesson.__str__(), "Lesson 1 (5 to 7)")

    def test_lesson_model_name(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        self.assertEqual(lesson.MODEL_NAME, "Lesson")

    def test_lesson_model_get_absolute_url(self):
        topic = self.test_data.create_topic(1)
        unit_plan = self.test_data.create_unit_plan(topic, 1)
        age_group_1 = self.test_data.create_age_group(5, 7)
        lesson = self.test_data.create_lesson(
            topic,
            unit_plan,
            1,
            age_group_1
        )
        self.assertEqual(
            lesson.get_absolute_url(),
            "/en/topics/topic-1/unit-plan-1/lesson-1/"
        )
