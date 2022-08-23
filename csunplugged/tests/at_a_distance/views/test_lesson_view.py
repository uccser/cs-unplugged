from http import HTTPStatus
from django.conf import settings
from django.test import override_settings
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.at_a_distance.AtADistanceTestDataGenerator import AtADistanceTestDataGenerator

TEST_TEMPLATES = settings.TEMPLATES
TEST_TEMPLATES[0]["DIRS"].append("tests/at_a_distance/views/assets/templates")


@override_settings(TEMPLATES=TEST_TEMPLATES)
class LessonViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = AtADistanceTestDataGenerator()
        self.language = "en"

    def test_lesson_view_with_valid_slug(self):
        lesson = self.test_data.create_lesson(1)
        kwargs = {
            "lesson_slug": lesson.slug
        }
        url = reverse("at_a_distance:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_lesson_view_with_invalid_slug(self):
        self.test_data.create_lesson(1)
        kwargs = {
            "lesson_slug": "wrong_slug",
        }
        url = reverse("at_a_distance:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)

    def test_lesson_view_context(self):
        lesson = self.test_data.create_lesson(1)
        kwargs = {
            "lesson_slug": lesson.slug,
        }
        url = reverse("at_a_distance:lesson", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["lesson"],
            lesson
        )
        self.assertEqual(
            response.context["slides_pdf"],
            "slides/en/lesson-1/lesson-1-slides.pdf"
        )
        self.assertEqual(
            response.context["notes_pdf"],
            "slides/en/lesson-1/lesson-1-speaker-notes.pdf"
        )
