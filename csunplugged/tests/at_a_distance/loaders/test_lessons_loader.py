import os.path
from django.test import override_settings
from tests.BaseTestWithDB import BaseTestWithDB
from tests.at_a_distance.AtADistanceTestDataGenerator import AtADistanceTestDataGenerator
from at_a_distance.models import Lesson
from at_a_distance.management.commands._LessonLoader import AtADistanceLessonLoader
from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.NoHeadingFoundInMarkdownFileError import NoHeadingFoundInMarkdownFileError
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError


class AtADistanceLessonsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = AtADistanceTestDataGenerator()
        self.loader_name = "lessons"
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_lesson_loader_configuration(self):
        test_name = "basic-config"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertQuerysetEqual(
            Lesson.objects.all(),
            ["<Lesson: Lesson 1>"],
            transform=repr
        )

    def test_lesson_loader_slug_set_correctly(self):
        test_name = "valid-slug"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.all()[0].slug,
            "valid-slug",
        )

    def test_lesson_loader_name_set_correctly(self):
        test_name = "valid-name"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug=test_name).name,
            "Lesson 1",
        )

    def test_lesson_loader_missing_name_text(self):
        test_name = "missing-title"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        self.assertRaises(
            NoHeadingFoundInMarkdownFileError,
            lesson_loader.load,
        )

    def test_lesson_loader_content_set_correctly(self):
        test_name = "valid-content"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug=test_name).introduction,
            "<p>Example content text.</p>",
        )

    def test_lesson_loader_missing_content_text(self):
        test_name = "missing-content"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        self.assertRaises(
            EmptyMarkdownFileError,
            lesson_loader.load,
        )

    def test_lesson_loader_missing_suitable_for_teaching_students(self):
        test_name = "missing-suitable-for-teaching-students"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        self.assertRaises(
            MissingRequiredFieldError,
            lesson_loader.load,
        )

    def test_lesson_loader_invalid_value_suitable_for_teaching_students(self):
        test_name = "invalid-value-suitable-for-teaching-students"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        self.assertRaises(
            InvalidYAMLValueError,
            lesson_loader.load,
        )

    def test_lesson_loader_missing_suitable_for_teaching_educators(self):
        test_name = "missing-suitable-for-teaching-educators"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        self.assertRaises(
            MissingRequiredFieldError,
            lesson_loader.load,
        )

    def test_lesson_loader_invalid_value_suitable_for_teaching_educators(self):
        test_name = "invalid-value-suitable-for-teaching-educators"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        self.assertRaises(
            InvalidYAMLValueError,
            lesson_loader.load,
        )

    @override_settings(STATIC_ROOT="tests/at_a_distance/loaders/assets/lessons/static")
    def test_lesson_loader_valid_icon(self):
        test_name = "valid-icon"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEquals(
            Lesson.objects.get(slug=test_name).icon,
            "img/valid-icon.png",
        )

    def test_lesson_loader_missing_icon(self):
        test_name = "missing-icon"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertIsNone(Lesson.objects.get(slug=test_name).icon)

    def test_lesson_loader_updating_lesson(self):
        test_name = "basic-config"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEqual(
            Lesson.objects.get(slug=test_name).order_number,
            1,
        )
        lesson_loader = AtADistanceLessonLoader(
            2,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertEqual(
            Lesson.objects.get(slug=test_name).order_number,
            2,
        )

    def test_lesson_loader_valid_supporting_resources(self):
        test_name = "valid-supporting-resources"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        lesson_loader.load()
        self.assertIsNone(Lesson.objects.get(slug=test_name).icon)

    def test_lesson_loader_missing_supporting_resources(self):
        test_name = "missing-supporting-resources"
        lesson_loader = AtADistanceLessonLoader(
            1,
            structure_filename=f"{test_name}.yaml",
            content_path=test_name,
            base_path=self.base_path
        )
        self.assertRaises(
            CouldNotFindYAMLFileError,
            lesson_loader.load,
        )
