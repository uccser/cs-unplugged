from django.http import QueryDict
from django.test import tag
from resources.generators.RunLengthEncodingResourceGenerator import RunLengthEncodingResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class RunLengthEncodingResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_worksheet_version_values(self):
        query = QueryDict("worksheet_type=student-basic&paper_size=a4")
        generator = RunLengthEncodingResourceGenerator(query)
        self.run_parameter_smoke_tests(generator, "worksheet_type")

    def test_subtitle_student_basic_a4(self):
        query = QueryDict("worksheet_type=student-basic&paper_size=a4")
        generator = RunLengthEncodingResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Student Worksheet - Kid Fax - a4"
        )

    def test_subtitle_student_basic_letter(self):
        query = QueryDict("worksheet_type=student-basic&paper_size=letter")
        generator = RunLengthEncodingResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Student Worksheet - Kid Fax - letter"
        )

    def test_subtitle_student_create_a4(self):
        query = QueryDict("worksheet_type=student-create&paper_size=a4")
        generator = RunLengthEncodingResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Student Worksheet - Create your own - a4"
        )

    def test_subtitle_student_create_letter(self):
        query = QueryDict("worksheet_type=student-create&paper_size=letter")
        generator = RunLengthEncodingResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Student Worksheet - Create your own - letter"
        )

    def test_subtitle_student_create_colour_a4(self):
        query = QueryDict("worksheet_type=student-create-colour&paper_size=a4")
        generator = RunLengthEncodingResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Student Worksheet - Create your own in colour - a4"
        )

    def test_subtitle_student_create_colour_letter(self):
        query = QueryDict("worksheet_type=student-create-colour&paper_size=letter")
        generator = RunLengthEncodingResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Student Worksheet - Create your own in colour - letter"
        )

    def test_subtitle_student_teacher_a4(self):
        query = QueryDict("worksheet_type=teacher&paper_size=a4")
        generator = RunLengthEncodingResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Teacher Worksheet - a4"
        )

    def test_subtitle_student_teacher_letter(self):
        query = QueryDict("worksheet_type=teacher&paper_size=letter")
        generator = RunLengthEncodingResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Teacher Worksheet - letter"
        )
