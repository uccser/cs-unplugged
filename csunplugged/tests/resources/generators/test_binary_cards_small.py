from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.BinaryCardsSmallResourceGenerator import BinaryCardsSmallResourceGenerator


@tag("resource")
class BinaryCardsSmallResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_subtitle_4_dots_black_a4(self):
        query = QueryDict("number_bits=4&dot_counts=yes&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - with dot counts - with black back - a4"
        )

    def test_subtitle_4_dots_black_letter(self):
        query = QueryDict("number_bits=4&dot_counts=yes&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - with dot counts - with black back - letter"
        )

    def test_subtitle_4_no_dots_black_a4(self):
        query = QueryDict("number_bits=4&dot_counts=no&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - without dot counts - with black back - a4"
        )

    def test_subtitle_4_no_dots_black_letter(self):
        query = QueryDict("number_bits=4&dot_counts=no&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - without dot counts - with black back - letter"
        )

    def test_subtitle_4_dots_no_black_a4(self):
        query = QueryDict("number_bits=4&dot_counts=yes&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - with dot counts - without black back - a4"
        )

    def test_subtitle_4_dots_no_black_letter(self):
        query = QueryDict("number_bits=4&dot_counts=yes&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - with dot counts - without black back - letter"
        )

    def test_subtitle_4_no_dots_no_black_a4(self):
        query = QueryDict("number_bits=4&dot_counts=no&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - without dot counts - without black back - a4"
        )

    def test_subtitle_4_no_dots_no_black_letter(self):
        query = QueryDict("number_bits=4&dot_counts=no&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - without dot counts - without black back - letter"
        )

    def test_subtitle_8_dots_black_a4(self):
        query = QueryDict("number_bits=8&dot_counts=yes&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - with dot counts - with black back - a4"
        )

    def test_subtitle_8_dots_black_letter(self):
        query = QueryDict("number_bits=8&dot_counts=yes&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - with dot counts - with black back - letter"
        )

    def test_subtitle_8_no_dots_black_a4(self):
        query = QueryDict("number_bits=8&dot_counts=no&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - without dot counts - with black back - a4"
        )

    def test_subtitle_8_no_dots_black_letter(self):
        query = QueryDict("number_bits=8&dot_counts=no&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - without dot counts - with black back - letter"
        )

    def test_subtitle_8_dots_no_black_a4(self):
        query = QueryDict("number_bits=8&dot_counts=yes&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - with dot counts - without black back - a4"
        )

    def test_subtitle_8_dots_no_black_letter(self):
        query = QueryDict("number_bits=8&dot_counts=yes&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - with dot counts - without black back - letter"
        )

    def test_subtitle_8_no_dots_no_black_a4(self):
        query = QueryDict("number_bits=8&dot_counts=no&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - without dot counts - without black back - a4"
        )

    def test_subtitle_8_no_dots_no_black_letter(self):
        query = QueryDict("number_bits=8&dot_counts=no&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - without dot counts - without black back - letter"
        )

    def test_subtitle_12_dots_black_a4(self):
        query = QueryDict("number_bits=12&dot_counts=yes&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "12 bits - with dot counts - with black back - a4"
        )

    def test_subtitle_12_dots_black_letter(self):
        query = QueryDict("number_bits=12&dot_counts=yes&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "12 bits - with dot counts - with black back - letter"
        )

    def test_subtitle_12_no_dots_black_a4(self):
        query = QueryDict("number_bits=12&dot_counts=no&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "12 bits - without dot counts - with black back - a4"
        )

    def test_subtitle_12_no_dots_black_letter(self):
        query = QueryDict("number_bits=12&dot_counts=no&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "12 bits - without dot counts - with black back - letter"
        )

    def test_subtitle_12_dots_no_black_a4(self):
        query = QueryDict("number_bits=12&dot_counts=yes&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "12 bits - with dot counts - without black back - a4"
        )

    def test_subtitle_12_dots_no_black_letter(self):
        query = QueryDict("number_bits=12&dot_counts=yes&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "12 bits - with dot counts - without black back - letter"
        )

    def test_subtitle_12_no_dots_no_black_a4(self):
        query = QueryDict("number_bits=12&dot_counts=no&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "12 bits - without dot counts - without black back - a4"
        )

    def test_subtitle_12_no_dots_no_black_letter(self):
        query = QueryDict("number_bits=12&dot_counts=no&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "12 bits - without dot counts - without black back - letter"
        )
