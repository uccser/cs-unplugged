from django.http import QueryDict
from django.test import tag
from resources.generators.SearchingCardsResourceGenerator import SearchingCardsResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class SearchingCardsResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("number_cards=15&max_number=cards&help_sheet=yes&paper_size=a4")

    def test_number_cards_values(self):
        generator = SearchingCardsResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "number_cards")

    def test_max_number_values(self):
        generator = SearchingCardsResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "max_number")

    def test_help_sheet_values(self):
        generator = SearchingCardsResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "help_sheet")

    def test_subtitle_15_cards_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=cards&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 15 - with helper sheet - a4"
        )

    def test_subtitle_15_cards_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=cards&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 15 - with helper sheet - letter"
        )

    def test_subtitle_31_cards_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=cards&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 31 - with helper sheet - a4"
        )

    def test_subtitle_31_cards_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=cards&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 31 - with helper sheet - letter"
        )

    def test_subtitle_15_99_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=99&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 99 - with helper sheet - a4"
        )

    def test_subtitle_15_99_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=99&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 99 - with helper sheet - letter"
        )

    def test_subtitle_31_99_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=99&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 99 - with helper sheet - a4"
        )

    def test_subtitle_31_99_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=99&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 99 - with helper sheet - letter"
        )

    def test_subtitle_15_999_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=999&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 999 - with helper sheet - a4"
        )

    def test_subtitle_15_999_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=999&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 999 - with helper sheet - letter"
        )

    def test_subtitle_31_999_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=999&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 999 - with helper sheet - a4"
        )

    def test_subtitle_31_999_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=999&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 999 - with helper sheet - letter"
        )

    def test_subtitle_15_blank_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=blank&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - Blankwith helper sheet - a4"
        )

    def test_subtitle_15_blank_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=blank&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - Blankwith helper sheet - letter"
        )

    def test_subtitle_31_blank_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=blank&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - Blankwith helper sheet - a4"
        )

    def test_subtitle_31_blank_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=blank&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - Blankwith helper sheet - letter"
        )

    def test_subtitle_15_cards_no_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=cards&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 15 - without helper sheet - a4"
        )

    def test_subtitle_15_cards_no_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=cards&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 15 - without helper sheet - letter"
        )

    def test_subtitle_31_cards_no_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=cards&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 31 - without helper sheet - a4"
        )

    def test_subtitle_31_cards_no_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=cards&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 31 - without helper sheet - letter"
        )

    def test_subtitle_15_99_no_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=99&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 99 - without helper sheet - a4"
        )

    def test_subtitle_15_99_no_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=99&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 99 - without helper sheet - letter"
        )

    def test_subtitle_31_99_no_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=99&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 99 - without helper sheet - a4"
        )

    def test_subtitle_31_99_no_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=99&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 99 - without helper sheet - letter"
        )

    def test_subtitle_15_999_no_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=999&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 999 - without helper sheet - a4"
        )

    def test_subtitle_15_999_no_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=999&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 1 to 999 - without helper sheet - letter"
        )

    def test_subtitle_31_999_no_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=999&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 999 - without helper sheet - a4"
        )

    def test_subtitle_31_999_no_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=999&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 1 to 999 - without helper sheet - letter"
        )

    def test_subtitle_15_blank_no_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=blank&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - Blankwithout helper sheet - a4"
        )

    def test_subtitle_15_blank_no_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=blank&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - Blankwithout helper sheet - letter"
        )

    def test_subtitle_31_blank_no_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=blank&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - Blankwithout helper sheet - a4"
        )

    def test_subtitle_31_blank_no_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=blank&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - Blankwithout helper sheet - letter"
        )
