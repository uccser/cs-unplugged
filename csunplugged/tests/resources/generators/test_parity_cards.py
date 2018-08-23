from django.http import QueryDict
from django.test import tag
from resources.generators.ParityCardsResourceGenerator import ParityCardsResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class ParityCardsResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("back_colour=black&paper_size=a4")

    def test_back_colour_values(self):
        generator = ParityCardsResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "back_colour")

    def test_subtitle_black_a4(self):
        query = QueryDict("back_colour=black&paper_size=a4")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Black - a4"
        )

    def test_subtitle_black_letter(self):
        query = QueryDict("back_colour=black&paper_size=letter")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Black - letter"
        )

    def test_subtitle_blue_a4(self):
        query = QueryDict("back_colour=blue&paper_size=a4")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Blue - a4"
        )

    def test_subtitle_blue_letter(self):
        query = QueryDict("back_colour=blue&paper_size=letter")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Blue - letter"
        )

    def test_subtitle_green_a4(self):
        query = QueryDict("back_colour=green&paper_size=a4")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Green - a4"
        )

    def test_subtitle_green_letter(self):
        query = QueryDict("back_colour=green&paper_size=letter")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Green - letter"
        )

    def test_subtitle_purple_a4(self):
        query = QueryDict("back_colour=purple&paper_size=a4")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Purple - a4"
        )

    def test_subtitle_purple_letter(self):
        query = QueryDict("back_colour=purple&paper_size=letter")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Purple - letter"
        )

    def test_subtitle_red_a4(self):
        query = QueryDict("back_colour=red&paper_size=a4")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Red - a4"
        )

    def test_subtitle_red_letter(self):
        query = QueryDict("back_colour=red&paper_size=letter")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Red - letter"
        )
