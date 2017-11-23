from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.BinaryToAlphabetResourceGenerator import BinaryToAlphabetResourceGenerator


@tag("resource")
class BinaryToAlphabetResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

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
