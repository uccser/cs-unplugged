from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.PianoKeysResourceGenerator import PianoKeysResourceGenerator


@tag("resource")
class PianoKeysResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_subtitle_no_a4(self):
        query = QueryDict("highlight=no&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "no highlight - a4"
        )

    def test_subtitle_no_letter(self):
        query = QueryDict("highlight=no&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "no highlight - letter"
        )

    def test_subtitle_A_a4(self):
        query = QueryDict("highlight=A&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "A highlight - a4"
        )

    def test_subtitle_A_letter(self):
        query = QueryDict("highlight=A&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "A highlight - letter"
        )

    def test_subtitle_B_a4(self):
        query = QueryDict("highlight=B&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "B highlight - a4"
        )

    def test_subtitle_B_letter(self):
        query = QueryDict("highlight=B&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "B highlight - letter"
        )

    def test_subtitle_C_a4(self):
        query = QueryDict("highlight=C&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "C highlight - a4"
        )

    def test_subtitle_C_letter(self):
        query = QueryDict("highlight=C&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "C highlight - letter"
        )

    def test_subtitle_D_a4(self):
        query = QueryDict("highlight=D&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "D highlight - a4"
        )

    def test_subtitle_D_letter(self):
        query = QueryDict("highlight=D&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "D highlight - letter"
        )

    def test_subtitle_E_a4(self):
        query = QueryDict("highlight=E&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "E highlight - a4"
        )

    def test_subtitle_E_letter(self):
        query = QueryDict("highlight=E&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "E highlight - letter"
        )

    def test_subtitle_F_a4(self):
        query = QueryDict("highlight=F&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "F highlight - a4"
        )

    def test_subtitle_F_letter(self):
        query = QueryDict("highlight=F&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "F highlight - letter"
        )

    def test_subtitle_G_a4(self):
        query = QueryDict("highlight=G&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "G highlight - a4"
        )

    def test_subtitle_G_letter(self):
        query = QueryDict("highlight=G&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "G highlight - letter"
        )
