from tests.BaseTestWithDB import BaseTestWithDB
from tests.at_a_distance.AtADistanceTestDataGenerator import AtADistanceTestDataGenerator


class AtADistanceLessonModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = AtADistanceTestDataGenerator()

    def test_at_a_distance_lesson_model_get_absolute_url(self):
        lesson = self.test_data.create_lesson(1)
        self.assertEqual(
            lesson.get_absolute_url(),
            "/en/at-a-distance/lesson-1/"
        )

    def test_at_a_distance_lesson_model_get_slides_path(self):
        lesson = self.test_data.create_lesson(1)
        self.assertEqual(
            lesson.get_slides_path(),
            "at_a_distance/lesson-slides/lesson-1.html"
        )
