from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.SearchingCardsResourceGenerator import SearchingCardsResourceGenerator
from tests.resources.generators.utils import run_parameter_smoke_tests


@tag("resource")
class SearchingCardsResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("number_cards=15&max_number=cards&help_sheet=yes&paper_size=a4")

    def test_number_cards_values(self):
        generator = SearchingCardsResourceGenerator(self.base_valid_query)
        run_parameter_smoke_tests(generator, "number_cards")

    def test_max_number_values(self):
        generator = SearchingCardsResourceGenerator(self.base_valid_query)
        run_parameter_smoke_tests(generator, "max_number")

    def test_help_sheet_values(self):
        generator = SearchingCardsResourceGenerator(self.base_valid_query)
        run_parameter_smoke_tests(generator, "help_sheet")

    def test_subtitle_15_cards_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=cards&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 15 - with helper sheet - a4"
        )

    def test_subtitle_15_cards_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=cards&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 15 - with helper sheet - letter"
        )

    def test_subtitle_31_cards_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=cards&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 31 - with helper sheet - a4"
        )

    def test_subtitle_31_cards_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=cards&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 31 - with helper sheet - letter"
        )

    def test_subtitle_15_99_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=99&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 99 - with helper sheet - a4"
        )

    def test_subtitle_15_99_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=99&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 99 - with helper sheet - letter"
        )

    def test_subtitle_31_99_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=99&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 99 - with helper sheet - a4"
        )

    def test_subtitle_31_99_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=99&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 99 - with helper sheet - letter"
        )

    def test_subtitle_15_999_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=999&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 999 - with helper sheet - a4"
        )

    def test_subtitle_15_999_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=999&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 999 - with helper sheet - letter"
        )

    def test_subtitle_31_999_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=999&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 999 - with helper sheet - a4"
        )

    def test_subtitle_31_999_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=999&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 999 - with helper sheet - letter"
        )

    def test_subtitle_15_blank_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=blank&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - blank - with helper sheet - a4"
        )

    def test_subtitle_15_blank_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=blank&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - blank - with helper sheet - letter"
        )

    def test_subtitle_31_blank_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=blank&help_sheet=yes&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - blank - with helper sheet - a4"
        )

    def test_subtitle_31_blank_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=blank&help_sheet=yes&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - blank - with helper sheet - letter"
        )

    def test_subtitle_15_cards_no_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=cards&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 15 - without helper sheet - a4"
        )

    def test_subtitle_15_cards_no_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=cards&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 15 - without helper sheet - letter"
        )

    def test_subtitle_31_cards_no_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=cards&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 31 - without helper sheet - a4"
        )

    def test_subtitle_31_cards_no_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=cards&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 31 - without helper sheet - letter"
        )

    def test_subtitle_15_99_no_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=99&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 99 - without helper sheet - a4"
        )

    def test_subtitle_15_99_no_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=99&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 99 - without helper sheet - letter"
        )

    def test_subtitle_31_99_no_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=99&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 99 - without helper sheet - a4"
        )

    def test_subtitle_31_99_no_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=99&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 99 - without helper sheet - letter"
        )

    def test_subtitle_15_999_no_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=999&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 999 - without helper sheet - a4"
        )

    def test_subtitle_15_999_no_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=999&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - 0 to 999 - without helper sheet - letter"
        )

    def test_subtitle_31_999_no_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=999&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 999 - without helper sheet - a4"
        )

    def test_subtitle_31_999_no_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=999&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - 0 to 999 - without helper sheet - letter"
        )

    def test_subtitle_15_blank_no_sheet_a4(self):
        query = QueryDict("number_cards=15&max_number=blank&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - blank - without helper sheet - a4"
        )

    def test_subtitle_15_blank_no_sheet_letter(self):
        query = QueryDict("number_cards=15&max_number=blank&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "15 cards - blank - without helper sheet - letter"
        )

    def test_subtitle_31_blank_no_sheet_a4(self):
        query = QueryDict("number_cards=31&max_number=blank&help_sheet=no&paper_size=a4")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - blank - without helper sheet - a4"
        )

    def test_subtitle_31_blank_no_sheet_letter(self):
        query = QueryDict("number_cards=31&max_number=blank&help_sheet=no&paper_size=letter")
        generator = SearchingCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "31 cards - blank - without helper sheet - letter"
        )
