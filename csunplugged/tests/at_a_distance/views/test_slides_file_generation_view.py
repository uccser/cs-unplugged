from django.conf import settings
from django.test import override_settings
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.at_a_distance.AtADistanceTestDataGenerator import AtADistanceTestDataGenerator

TEST_TEMPLATES = settings.TEMPLATES
TEST_TEMPLATES[0]["DIRS"].append("tests/at_a_distance/views/assets/templates")
LANGUAGE1 = "lang1"
LANGUAGE2 = "lang2"
MULTIPLE_LANGUAGES = ((LANGUAGE1, LANGUAGE1), (LANGUAGE2, LANGUAGE2))


@override_settings(TEMPLATES=TEST_TEMPLATES)
class LessonFileGenerationViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = AtADistanceTestDataGenerator()
        self.language = "en"

    def test_slides_file_generation_view_single_lesson(self):
        self.test_data.create_lesson(1)
        url = reverse("at_a_distance:slides_file_generation_json")
        response = self.client.get(url)
        self.assertJSONEqual(
            response.content.decode(),
            {
                "resolution": "1920x1080",
                "slide_counts": {
                    "lesson-1": 2,
                },
                "languages": {
                    "en": [
                        "lesson-1",
                    ]
                },
            }
        )

    def test_slides_file_generation_view_multiple_lessons(self):
        self.test_data.create_lesson(1)
        self.test_data.create_lesson(2)
        self.test_data.create_lesson(3)
        url = reverse("at_a_distance:slides_file_generation_json")
        response = self.client.get(url)
        self.assertJSONEqual(
            response.content.decode(),
            {
                "resolution": "1920x1080",
                "slide_counts": {
                    "lesson-1": 2,
                    "lesson-2": 4,
                    "lesson-3": 7,
                },
                "languages": {
                    "en": [
                        "lesson-1",
                        "lesson-2",
                        "lesson-3",
                    ]
                },
            }
        )

    @override_settings(DEFAULT_LANGUAGES=MULTIPLE_LANGUAGES)
    def test_slides_file_generation_view_single_lesson_multiple_languages(self):
        lesson = self.test_data.create_lesson(1)
        lesson.languages = [LANGUAGE1, LANGUAGE2]
        lesson.save()
        url = reverse("at_a_distance:slides_file_generation_json") + "?language=all"
        response = self.client.get(url)
        self.assertJSONEqual(
            response.content.decode(),
            {
                "resolution": "1920x1080",
                "slide_counts": {
                    "lesson-1": 2,
                },
                "languages": {
                    LANGUAGE1: [
                        "lesson-1",
                    ],
                    LANGUAGE2: [
                        "lesson-1",
                    ]
                },
            }
        )

    @override_settings(DEFAULT_LANGUAGES=MULTIPLE_LANGUAGES)
    def test_slides_file_generation_view_multiple_lessons_multiple_languages(self):
        lesson1 = self.test_data.create_lesson(1)
        lesson1.languages = [LANGUAGE1, LANGUAGE2]
        lesson1.save()
        lesson2 = self.test_data.create_lesson(2)
        lesson2.languages = [LANGUAGE1]
        lesson2.save()
        lesson3 = self.test_data.create_lesson(3)
        lesson3.languages = [LANGUAGE2]
        lesson3.save()
        url = reverse("at_a_distance:slides_file_generation_json") + "?language=all"
        response = self.client.get(url)
        self.assertJSONEqual(
            response.content.decode(),
            {
                "resolution": "1920x1080",
                "slide_counts": {
                    "lesson-1": 2,
                    "lesson-2": 4,
                    "lesson-3": 7,
                },
                "languages": {
                    LANGUAGE1: [
                        "lesson-1",
                        "lesson-2",
                    ],
                    LANGUAGE2: [
                        "lesson-1",
                        "lesson-3",
                    ]
                },
            }
        )
