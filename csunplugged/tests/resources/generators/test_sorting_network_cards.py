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
            "letters - a4"
        )

    def test_subtitle_letters_letter(self):
        query = QueryDict("type=letters&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "letters - letter"
        )

    def test_subtitle_words_a4(self):
        query = QueryDict("type=words&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "words - a4"
        )

    def test_subtitle_words_letter(self):
        query = QueryDict("type=words&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "words - letter"
        )

    def test_subtitle_small_numbers_a4(self):
        query = QueryDict("type=small_numbers&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "small numbers - a4"
        )

    def test_subtitle_small_numbers_letter(self):
        query = QueryDict("type=small_numbers&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "small numbers - letter"
        )

    def test_subtitle_large_numbers_a4(self):
        query = QueryDict("type=large_numbers&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "large numbers - a4"
        )

    def test_subtitle_large_numbers_letter(self):
        query = QueryDict("type=large_numbers&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "large numbers - letter"
        )

    def test_subtitle_fractions_a4(self):
        query = QueryDict("type=fractions&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "fractions - a4"
        )

    def test_subtitle_fractions_letter(self):
        query = QueryDict("type=fractions&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "fractions - letter"
        )

    def test_subtitle_maori_colours_a4(self):
        query = QueryDict("type=maori_colours&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "maori colours - a4"
        )

    def test_subtitle_maori_colours_letter(self):
        query = QueryDict("type=maori_colours&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "maori colours - letter"
        )

    def test_subtitle_maori_numbers_a4(self):
        query = QueryDict("type=maori_numbers&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "maori numbers - a4"
        )

    def test_subtitle_maori_numbers_letter(self):
        query = QueryDict("type=maori_numbers&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "maori numbers - letter"
        )

    def test_subtitle_butterfly_a4(self):
        query = QueryDict("type=butterfly&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "butterfly - a4"
        )

    def test_subtitle_butterfly_letter(self):
        query = QueryDict("type=butterfly&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "butterfly - letter"
        )

    def test_subtitle_riding_hood_a4(self):
        query = QueryDict("type=riding_hood&paper_size=a4")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "riding hood - a4"
        )

    def test_subtitle_riding_hood_letter(self):
        query = QueryDict("type=riding_hood&paper_size=letter")
        generator = SortingNetworkCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "riding hood - letter"
        )
