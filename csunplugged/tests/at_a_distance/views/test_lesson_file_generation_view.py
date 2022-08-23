from django.conf import settings
from django.test import override_settings
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.at_a_distance.AtADistanceTestDataGenerator import AtADistanceTestDataGenerator

TEST_TEMPLATES = settings.TEMPLATES
TEST_TEMPLATES[0]["DIRS"].append("tests/at_a_distance/views/assets/templates")


@override_settings(TEMPLATES=TEST_TEMPLATES)
class LessonFileGenerationViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = AtADistanceTestDataGenerator()
        self.language = "en"

    def test_lesson_file_generation_view_context(self):
        lesson = self.test_data.create_lesson(1)
        kwargs = {
            "lesson_slug": lesson.slug,
        }
        url = reverse("at_a_distance:lesson_file_generation", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(
            response.context["lesson"],
            lesson
        )
        self.assertEqual(response.context["fragments"], "false")
        self.assertEqual(response.context["slide_number"], "false")
