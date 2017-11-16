from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.ModuloClockResourceGenerator import ModuloClockResourceGenerator


@tag("resource")
class ModuloClockResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_subtitle_1_a4(self):
        query = QueryDict("modulo_number=1&paper_size=a4")
        generator = ModuloClockResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - a4"
        )

    def test_subtitle_1_letter(self):
        query = QueryDict("modulo_number=1&paper_size=letter")
        generator = ModuloClockResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - letter"
        )

    def test_subtitle_2_a4(self):
        query = QueryDict("modulo_number=2&paper_size=a4")
        generator = ModuloClockResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "2 - a4"
        )

    def test_subtitle_2_letter(self):
        query = QueryDict("modulo_number=2&paper_size=letter")
        generator = ModuloClockResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "2 - letter"
        )

    def test_subtitle_10_a4(self):
        query = QueryDict("modulo_number=10&paper_size=a4")
        generator = ModuloClockResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "10 - a4"
        )

    def test_subtitle_10_letter(self):
        query = QueryDict("modulo_number=10&paper_size=letter")
        generator = ModuloClockResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "10 - letter"
        )
