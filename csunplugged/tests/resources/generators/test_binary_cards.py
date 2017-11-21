from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.BinaryCardsResourceGenerator import BinaryCardsResourceGenerator
from tests.resources.generators.utils import run_parameter_smoke_tests


@tag("resource")
class BinaryCardsResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("display_numbers=yes&black_back=yes&paper_size=a4")

    def test_black_back_values(self):
        generator = BinaryCardsResourceGenerator(self.base_valid_query)
        run_parameter_smoke_tests(generator, "black_back")

    def test_display_numbers_values(self):
        generator = BinaryCardsResourceGenerator(self.base_valid_query)
        run_parameter_smoke_tests(generator, "display_numbers")

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
