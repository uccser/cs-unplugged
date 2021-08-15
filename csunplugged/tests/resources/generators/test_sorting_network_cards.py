from django.http import QueryDict
from django.test import tag
from resources.generators.SortingNetworkCardsResourceGenerator import SortingNetworkCardsResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class SortingNetworkCardsResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("type=letters&paper_size=a4")

    def test_type_values(self):
        generator = SortingNetworkCardsResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "type")

    def test_subtitle_letters_a4(self):
        query = QueryDict("type=letters&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Letters - a4"
        )

    def test_subtitle_letters_letter(self):
        query = QueryDict("type=letters&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Letters - letter"
        )

    def test_subtitle_words_a4(self):
        query = QueryDict("type=words&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Words - a4"
        )

    def test_subtitle_words_letter(self):
        query = QueryDict("type=words&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Words - letter"
        )

    def test_subtitle_small_numbers_a4(self):
        query = QueryDict("type=small_numbers&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Small numbers (1 to 10) - a4"
        )

    def test_subtitle_small_numbers_letter(self):
        query = QueryDict("type=small_numbers&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Small numbers (1 to 10) - letter"
        )

    def test_subtitle_large_numbers_a4(self):
        query = QueryDict("type=large_numbers&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Large numbers (7 digit numbers) - a4"
        )

    def test_subtitle_large_numbers_letter(self):
        query = QueryDict("type=large_numbers&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Large numbers (7 digit numbers) - letter"
        )

    def test_subtitle_fractions_a4(self):
        query = QueryDict("type=fractions&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Fractions - a4"
        )

    def test_subtitle_fractions_letter(self):
        query = QueryDict("type=fractions&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Fractions - letter"
        )

    def test_subtitle_butterfly_a4(self):
        query = QueryDict("type=butterfly&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Butterfly life cycle - a4"
        )

    def test_subtitle_butterfly_letter(self):
        query = QueryDict("type=butterfly&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Butterfly life cycle - letter"
        )

    def test_subtitle_riding_hood_a4(self):
        query = QueryDict("type=riding_hood&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Little Red Riding Hood - a4"
        )

    def test_subtitle_riding_hood_letter(self):
        query = QueryDict("type=riding_hood&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Little Red Riding Hood - letter"
        )
