"""Test class for get_lesson_speaker_notes module."""

from django.conf import settings
from django.test import override_settings
from tests.BaseTestWithDB import BaseTestWithDB
from tests.at_a_distance.AtADistanceTestDataGenerator import AtADistanceTestDataGenerator
from at_a_distance.utils import get_lesson_speaker_notes

TEST_TEMPLATES = settings.TEMPLATES
TEST_TEMPLATES[0]["DIRS"].append("tests/at_a_distance/utils/assets/templates")


@override_settings(TEMPLATES=TEST_TEMPLATES)
class GetLessonSpeakerNotesTest(BaseTestWithDB):
    """Test class for get_lesson_speaker_notes module."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.test_data = AtADistanceTestDataGenerator()

    def test_single_slide_speaker_notes(self):
        test_name = "single-speaker-notes"
        lesson = self.test_data.create_lesson(1)
        lesson.slug = test_name
        lesson.save()
        speaker_notes = get_lesson_speaker_notes(lesson)
        self.assertEqual(len(speaker_notes), 2)
        self.assertFalse(speaker_notes[0])
        self.assertHTMLEqual(
            speaker_notes[1],
            '<aside class="notes"><p>Speaker notes.</p></aside>',
        )

    def test_multiple_slide_speaker_notes(self):
        test_name = "multiple-speaker-notes"
        lesson = self.test_data.create_lesson(1)
        lesson.slug = test_name
        lesson.save()
        speaker_notes = get_lesson_speaker_notes(lesson)
        self.assertEqual(len(speaker_notes), 4)
        self.assertFalse(speaker_notes[0])
        self.assertHTMLEqual(
            speaker_notes[1],
            '<aside class="notes"><p>Speaker notes.</p></aside>',
        )
        self.assertHTMLEqual(
            speaker_notes[2],
            '<aside class="notes"><p>Some more speaker notes.</p></aside>',
        )
        self.assertHTMLEqual(
            speaker_notes[3],
            '<aside class="notes"><p>Final speaker notes.</p></aside>',
        )

    def test_all_missing_slide_speaker_notes(self):
        test_name = "all-missing-speaker-notes"
        lesson = self.test_data.create_lesson(1)
        lesson.slug = test_name
        lesson.save()
        speaker_notes = get_lesson_speaker_notes(lesson)
        expected_length = 10
        self.assertEqual(len(speaker_notes), expected_length)
        self.assertListEqual(
            speaker_notes,
            [False] * expected_length,
        )

    def test_some_missing_slide_speaker_notes(self):
        test_name = "some-missing-speaker-notes"
        lesson = self.test_data.create_lesson(1)
        lesson.slug = test_name
        lesson.save()
        speaker_notes = get_lesson_speaker_notes(lesson)
        self.assertEqual(len(speaker_notes), 6)
        self.assertFalse(speaker_notes[0])
        self.assertHTMLEqual(
            speaker_notes[1],
            '<aside class="notes"><p>Speaker notes.</p></aside>',
        )
        self.assertFalse(speaker_notes[2])
        self.assertHTMLEqual(
            speaker_notes[3],
            '<aside class="notes"><p>Some more speaker notes.</p></aside>',
        )
        self.assertFalse(speaker_notes[4])
        self.assertHTMLEqual(
            speaker_notes[5],
            '<aside class="notes"><p>Final speaker notes.</p></aside>',
        )
