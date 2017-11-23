from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.SortingNetworkResourceGenerator import SortingNetworkResourceGenerator


@tag("resource")
class SortingNetworkResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_subtitle_blank_a4(self):
        query = QueryDict("prefilled_values=blank&paper_size=a4")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - a4"
        )

    def test_subtitle_blank_letter(self):
        query = QueryDict("prefilled_values=blank&paper_size=letter")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - letter"
        )

    def test_subtitle_easy_a4(self):
        query = QueryDict("prefilled_values=easy&paper_size=a4")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "1 to 9 - a4"
        )

    def test_subtitle_easy_letter(self):
        query = QueryDict("prefilled_values=easy&paper_size=letter")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "1 to 9 - letter"
        )

    def test_subtitle_medium_a4(self):
        query = QueryDict("prefilled_values=medium&paper_size=a4")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "10 to 99 - a4"
        )

    def test_subtitle_medium_letter(self):
        query = QueryDict("prefilled_values=medium&paper_size=letter")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "10 to 99 - letter"
        )

    def test_subtitle_hard_a4(self):
        query = QueryDict("prefilled_values=hard&paper_size=a4")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "100 to 999 - a4"
        )

    def test_subtitle_hard_letter(self):
        query = QueryDict("prefilled_values=hard&paper_size=letter")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "100 to 999 - letter"
        )
