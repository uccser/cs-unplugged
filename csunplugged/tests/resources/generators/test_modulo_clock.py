from django.http import QueryDict
from django.test import tag
from resources.generators.ModuloClockResourceGenerator import ModuloClockResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class ModuloClockResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("modulo_number=1&paper_size=a4")

    def test_modulo_number_values(self):
        generator = ModuloClockResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "modulo_number")

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
