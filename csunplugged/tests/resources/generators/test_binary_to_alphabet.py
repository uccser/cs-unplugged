from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.BinaryToAlphabetResourceGenerator import BinaryToAlphabetResourceGenerator
from tests.resources.generators.utils import run_parameter_smoke_tests


@tag("resource")
class BinaryToAlphabetResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("worksheet_version=student&paper_size=a4")

    def test_worksheet_version_values(self):
        generator = BinaryToAlphabetResourceGenerator(self.base_valid_query)
        run_parameter_smoke_tests(generator, "worksheet_version")

    def test_subtitle_student_a4(self):
        query = QueryDict("worksheet_version=student&paper_size=a4")
        generator = BinaryToAlphabetResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "student - a4"
        )

    def test_subtitle_student_letter(self):
        query = QueryDict("worksheet_version=student&paper_size=letter")
        generator = BinaryToAlphabetResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "student - letter"
        )

    def test_subtitle_teacher_a4(self):
        query = QueryDict("worksheet_version=teacher&paper_size=a4")
        generator = BinaryToAlphabetResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "teacher - a4"
        )

    def test_subtitle_teacher_letter(self):
        query = QueryDict("worksheet_version=teacher&paper_size=letter")
        generator = BinaryToAlphabetResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "teacher - letter"
        )
