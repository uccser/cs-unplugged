from django.http import QueryDict
from django.test import tag
from resources.generators.BinaryCardsSmallResourceGenerator import BinaryCardsSmallResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class BinaryCardsSmallResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("number_bits=4&dot_counts=yes&black_back=yes&paper_size=a4")

    def test_number_bits_values(self):
        generator = BinaryCardsSmallResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "number_bits")

    def test_black_back_values(self):
        generator = BinaryCardsSmallResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "black_back")

    def test_dot_counts(self):
        generator = BinaryCardsSmallResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "dot_counts")

    def test_subtitle_4_dots_black_a4(self):
        query = QueryDict("number_bits=4&dot_counts=yes&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - with dot counts - with black back - a4"
        )

    def test_subtitle_4_dots_black_letter(self):
        query = QueryDict("number_bits=4&dot_counts=yes&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - with dot counts - with black back - letter"
        )

    def test_subtitle_4_no_dots_black_a4(self):
        query = QueryDict("number_bits=4&dot_counts=no&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - without dot counts - with black back - a4"
        )

    def test_subtitle_4_no_dots_black_letter(self):
        query = QueryDict("number_bits=4&dot_counts=no&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - without dot counts - with black back - letter"
        )

    def test_subtitle_4_dots_no_black_a4(self):
        query = QueryDict("number_bits=4&dot_counts=yes&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - with dot counts - without black back - a4"
        )

    def test_subtitle_4_dots_no_black_letter(self):
        query = QueryDict("number_bits=4&dot_counts=yes&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - with dot counts - without black back - letter"
        )

    def test_subtitle_4_no_dots_no_black_a4(self):
        query = QueryDict("number_bits=4&dot_counts=no&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - without dot counts - without black back - a4"
        )

    def test_subtitle_4_no_dots_no_black_letter(self):
        query = QueryDict("number_bits=4&dot_counts=no&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - without dot counts - without black back - letter"
        )

    def test_subtitle_8_dots_black_a4(self):
        query = QueryDict("number_bits=8&dot_counts=yes&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - with dot counts - with black back - a4"
        )

    def test_subtitle_8_dots_black_letter(self):
        query = QueryDict("number_bits=8&dot_counts=yes&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - with dot counts - with black back - letter"
        )

    def test_subtitle_8_no_dots_black_a4(self):
        query = QueryDict("number_bits=8&dot_counts=no&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - without dot counts - with black back - a4"
        )

    def test_subtitle_8_no_dots_black_letter(self):
        query = QueryDict("number_bits=8&dot_counts=no&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - without dot counts - with black back - letter"
        )

    def test_subtitle_8_dots_no_black_a4(self):
        query = QueryDict("number_bits=8&dot_counts=yes&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - with dot counts - without black back - a4"
        )

    def test_subtitle_8_dots_no_black_letter(self):
        query = QueryDict("number_bits=8&dot_counts=yes&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - with dot counts - without black back - letter"
        )

    def test_subtitle_8_no_dots_no_black_a4(self):
        query = QueryDict("number_bits=8&dot_counts=no&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - without dot counts - without black back - a4"
        )

    def test_subtitle_8_no_dots_no_black_letter(self):
        query = QueryDict("number_bits=8&dot_counts=no&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - without dot counts - without black back - letter"
        )

    def test_subtitle_12_dots_black_a4(self):
        query = QueryDict("number_bits=12&dot_counts=yes&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Twelve (1 to 2048) - with dot counts - with black back - a4"
        )

    def test_subtitle_12_dots_black_letter(self):
        query = QueryDict("number_bits=12&dot_counts=yes&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Twelve (1 to 2048) - with dot counts - with black back - letter"
        )

    def test_subtitle_12_no_dots_black_a4(self):
        query = QueryDict("number_bits=12&dot_counts=no&black_back=yes&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Twelve (1 to 2048) - without dot counts - with black back - a4"
        )

    def test_subtitle_12_no_dots_black_letter(self):
        query = QueryDict("number_bits=12&dot_counts=no&black_back=yes&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Twelve (1 to 2048) - without dot counts - with black back - letter"
        )

    def test_subtitle_12_dots_no_black_a4(self):
        query = QueryDict("number_bits=12&dot_counts=yes&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Twelve (1 to 2048) - with dot counts - without black back - a4"
        )

    def test_subtitle_12_dots_no_black_letter(self):
        query = QueryDict("number_bits=12&dot_counts=yes&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Twelve (1 to 2048) - with dot counts - without black back - letter"
        )

    def test_subtitle_12_no_dots_no_black_a4(self):
        query = QueryDict("number_bits=12&dot_counts=no&black_back=no&paper_size=a4")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Twelve (1 to 2048) - without dot counts - without black back - a4"
        )

    def test_subtitle_12_no_dots_no_black_letter(self):
        query = QueryDict("number_bits=12&dot_counts=no&black_back=no&paper_size=letter")
        generator = BinaryCardsSmallResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Twelve (1 to 2048) - without dot counts - without black back - letter"
        )
