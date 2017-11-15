from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.ParityCardsResourceGenerator import ParityCardsResourceGenerator


@tag("resource")
class ParityCardsResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_subtitle_black_a4(self):
        query = QueryDict("back_colour=black&paper_size=a4")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "black back - a4"
        )

    def test_subtitle_black_letter(self):
        query = QueryDict("back_colour=black&paper_size=letter")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "black back - letter"
        )

    def test_subtitle_blue_a4(self):
        query = QueryDict("back_colour=blue&paper_size=a4")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blue back - a4"
        )

    def test_subtitle_blue_letter(self):
        query = QueryDict("back_colour=blue&paper_size=letter")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blue back - letter"
        )

    def test_subtitle_green_a4(self):
        query = QueryDict("back_colour=green&paper_size=a4")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "green back - a4"
        )

    def test_subtitle_green_letter(self):
        query = QueryDict("back_colour=green&paper_size=letter")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "green back - letter"
        )

    def test_subtitle_purple_a4(self):
        query = QueryDict("back_colour=purple&paper_size=a4")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "purple back - a4"
        )

    def test_subtitle_purple_letter(self):
        query = QueryDict("back_colour=purple&paper_size=letter")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "purple back - letter"
        )

    def test_subtitle_red_a4(self):
        query = QueryDict("back_colour=red&paper_size=a4")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "red back - a4"
        )

    def test_subtitle_red_letter(self):
        query = QueryDict("back_colour=red&paper_size=letter")
        generator = ParityCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "red back - letter"
        )
