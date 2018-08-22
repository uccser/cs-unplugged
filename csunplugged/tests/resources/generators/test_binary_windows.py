from django.http import QueryDict
from django.test import tag
from resources.generators.BinaryWindowsResourceGenerator import BinaryWindowsResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class BinaryWindowsResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("number_bits=4&value_type=binary&dot_counts=yes&paper_size=a4")

    def test_number_bits_values(self):
        generator = BinaryWindowsResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "number_bits")

    def test_value_type_values(self):
        generator = BinaryWindowsResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "value_type")

    def test_dot_counts_values(self):
        generator = BinaryWindowsResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "dot_counts")

    def test_subtitle_4_binary_dots_a4(self):
        query = QueryDict("number_bits=4&value_type=binary&dot_counts=yes&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - Binary (0 or 1) - with dot counts - a4"
        )

    def test_subtitle_4_binary_dots_letter(self):
        query = QueryDict("number_bits=4&value_type=binary&dot_counts=yes&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - Binary (0 or 1) - with dot counts - letter"
        )

    def test_subtitle_4_lightbulb_dots_a4(self):
        query = QueryDict("number_bits=4&value_type=lightbulb&dot_counts=yes&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - Lightbulb (off or on) - with dot counts - a4"
        )

    def test_subtitle_4_lightbulb_dots_letter(self):
        query = QueryDict("number_bits=4&value_type=lightbulb&dot_counts=yes&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - Lightbulb (off or on) - with dot counts - letter"
        )

    def test_subtitle_4_binary_no_dots_a4(self):
        query = QueryDict("number_bits=4&value_type=binary&dot_counts=no&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - Binary (0 or 1) - without dot counts - a4"
        )

    def test_subtitle_4_binary_no_dots_letter(self):
        query = QueryDict("number_bits=4&value_type=binary&dot_counts=no&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - Binary (0 or 1) - without dot counts - letter"
        )

    def test_subtitle_4_lightbulb_no_dots_a4(self):
        query = QueryDict("number_bits=4&value_type=lightbulb&dot_counts=no&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - Lightbulb (off or on) - without dot counts - a4"
        )

    def test_subtitle_4_lightbulb_no_dots_letter(self):
        query = QueryDict("number_bits=4&value_type=lightbulb&dot_counts=no&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Four (1 to 8) - Lightbulb (off or on) - without dot counts - letter"
        )

    def test_subtitle_8_binary_dots_a4(self):
        query = QueryDict("number_bits=8&value_type=binary&dot_counts=yes&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - Binary (0 or 1) - with dot counts - a4"
        )

    def test_subtitle_8_binary_dots_letter(self):
        query = QueryDict("number_bits=8&value_type=binary&dot_counts=yes&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - Binary (0 or 1) - with dot counts - letter"
        )

    def test_subtitle_8_lightbulb_dots_a4(self):
        query = QueryDict("number_bits=8&value_type=lightbulb&dot_counts=yes&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - Lightbulb (off or on) - with dot counts - a4"
        )

    def test_subtitle_8_lightbulb_dots_letter(self):
        query = QueryDict("number_bits=8&value_type=lightbulb&dot_counts=yes&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - Lightbulb (off or on) - with dot counts - letter"
        )

    def test_subtitle_8_binary_no_dots_a4(self):
        query = QueryDict("number_bits=8&value_type=binary&dot_counts=no&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - Binary (0 or 1) - without dot counts - a4"
        )

    def test_subtitle_8_binary_no_dots_letter(self):
        query = QueryDict("number_bits=8&value_type=binary&dot_counts=no&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - Binary (0 or 1) - without dot counts - letter"
        )

    def test_subtitle_8_lightbulb_no_dots_a4(self):
        query = QueryDict("number_bits=8&value_type=lightbulb&dot_counts=no&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - Lightbulb (off or on) - without dot counts - a4"
        )

    def test_subtitle_8_lightbulb_no_dots_letter(self):
        query = QueryDict("number_bits=8&value_type=lightbulb&dot_counts=no&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Eight (1 to 128) - Lightbulb (off or on) - without dot counts - letter"
        )
