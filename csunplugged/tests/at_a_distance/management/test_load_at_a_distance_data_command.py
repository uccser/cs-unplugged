"""Module for the testing custom Django load_at_a_distance_data command."""

import os.path
from unittest import mock
from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management
from django.test import tag, override_settings
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError
from utils.errors.EmptyYAMLFileError import EmptyYAMLFileError

TEST_BASE_PATH = "tests/at_a_distance/management/assets/"


@tag("management")
class LoadAtADistanceDataCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    @mock.patch(
        "at_a_distance.management.commands._LessonLoader.AtADistanceLessonLoader.load",
        return_value=True
    )
    @override_settings(
        AT_A_DISTANCE_CONTENT_BASE_PATH=os.path.join(TEST_BASE_PATH, "lessons-valid")
    )
    def test_load_at_a_distance_data_lessons_valid(self, lesson_loader):
        management.call_command("load_at_a_distance_data")
        self.assertTrue(lesson_loader.called)

    @mock.patch(
        "at_a_distance.management.commands._LessonLoader.AtADistanceLessonLoader.load",
        return_value=True
    )
    @override_settings(
        AT_A_DISTANCE_CONTENT_BASE_PATH=os.path.join(TEST_BASE_PATH, "lessons-empty")
    )
    def test_load_at_a_distance_data_lessons_empty(self, lesson_loader):
        self.assertRaises(
            EmptyYAMLFileError,
            management.call_command,
            "load_at_a_distance_data"
        )

    @mock.patch(
        "at_a_distance.management.commands._LessonLoader.AtADistanceLessonLoader.load",
        return_value=True
    )
    @override_settings(
        AT_A_DISTANCE_CONTENT_BASE_PATH=os.path.join(TEST_BASE_PATH, "lessons-missing")
    )
    def test_load_at_a_distance_data_lessons_missing(self, lesson_loader):
        self.assertRaises(
            MissingRequiredFieldError,
            management.call_command,
            "load_at_a_distance_data"
        )

    @mock.patch(
        "at_a_distance.management.commands._LessonLoader.AtADistanceLessonLoader.load",
        return_value=True
    )
    @override_settings(
        AT_A_DISTANCE_CONTENT_BASE_PATH=os.path.join(TEST_BASE_PATH, "lessons-not-list")
    )
    def test_load_at_a_distance_data_lessons_not_list(self, lesson_loader):
        self.assertRaises(
            InvalidYAMLValueError,
            management.call_command,
            "load_at_a_distance_data"
        )
