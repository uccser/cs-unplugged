from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.BinaryCardsResourceGenerator import BinaryCardsResourceGenerator


@tag("resource")
class BinaryCardsResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_subtitle_numbers_black_a4(self):
        query = QueryDict("display_numbers=yes&black_back=yes&paper_size=a4")
        generator = BinaryCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "with numbers - with black back - a4"
        )

    def test_subtitle_numbers_black_letter(self):
        query = QueryDict("display_numbers=yes&black_back=yes&paper_size=letter")
        generator = BinaryCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "with numbers - with black back - letter"
        )

    def test_subtitle_no_numbers_black_a4(self):
        query = QueryDict("display_numbers=no&black_back=yes&paper_size=a4")
        generator = BinaryCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "without numbers - with black back - a4"
        )

    def test_subtitle_no_numbers_black_letter(self):
        query = QueryDict("display_numbers=no&black_back=yes&paper_size=letter")
        generator = BinaryCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "without numbers - with black back - letter"
        )

    def test_subtitle_numbers_no_black_a4(self):
        query = QueryDict("display_numbers=yes&black_back=no&paper_size=a4")
        generator = BinaryCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "with numbers - without black back - a4"
        )

    def test_subtitle_numbers_no_black_letter(self):
        query = QueryDict("display_numbers=yes&black_back=no&paper_size=letter")
        generator = BinaryCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "with numbers - without black back - letter"
        )

    def test_subtitle_no_numbers_no_black_a4(self):
        query = QueryDict("display_numbers=no&black_back=no&paper_size=a4")
        generator = BinaryCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "without numbers - without black back - a4"
        )

    def test_subtitle_no_numbers_no_black_letter(self):
        query = QueryDict("display_numbers=no&black_back=no&paper_size=letter")
        generator = BinaryCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "without numbers - without black back - letter"
        )
