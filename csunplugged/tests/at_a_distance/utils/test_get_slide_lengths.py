"""Test class for get_slide_lengths module."""

from django.conf import settings
from django.test import override_settings
from tests.BaseTestWithDB import BaseTestWithDB
from tests.at_a_distance.AtADistanceTestDataGenerator import AtADistanceTestDataGenerator
from at_a_distance.utils import get_slide_lengths

TEST_TEMPLATES = settings.TEMPLATES
TEST_TEMPLATES[0]["DIRS"].append("tests/at_a_distance/utils/assets/templates")


@override_settings(TEMPLATES=TEST_TEMPLATES)
class GetSlideLengthsTest(BaseTestWithDB):
    """Test class for get_slide_lengths module."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = AtADistanceTestDataGenerator()

    def test_single_lesson(self):
        lesson1 = self.test_data.create_lesson(1)
        lesson1.slug = "lengths-lesson-1"
        lesson1.save()
        result = get_slide_lengths()
        self.assertDictEqual(
            result,
            {
                "lengths-lesson-1": 2,
            }
        )

    def test_multiple_lessons(self):
        lesson1 = self.test_data.create_lesson(1)
        lesson1.slug = "lengths-lesson-1"
        lesson1.save()
        lesson2 = self.test_data.create_lesson(2)
        lesson2.slug = "lengths-lesson-2"
        lesson2.save()
        lesson3 = self.test_data.create_lesson(3)
        lesson3.slug = "lengths-lesson-3"
        lesson3.save()
        result = get_slide_lengths()
        self.assertDictEqual(
            result,
            {
                "lengths-lesson-1": 2,
                "lengths-lesson-2": 5,
                "lengths-lesson-3": 1,
            }
        )
