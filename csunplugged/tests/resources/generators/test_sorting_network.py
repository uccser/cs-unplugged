from django.http import QueryDict
from django.test import tag
from resources.generators.SortingNetworkResourceGenerator import SortingNetworkResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class SortingNetworkResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("prefilled_values=blank&paper_size=a4")

    def test_prefilled_values_values(self):
        generator = SortingNetworkResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "prefilled_values")

    def test_subtitle_blank_a4(self):
        query = QueryDict("prefilled_values=blank&paper_size=a4")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "None (Blank - Useful as template) - a4"
        )

    def test_subtitle_blank_letter(self):
        query = QueryDict("prefilled_values=blank&paper_size=letter")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "None (Blank - Useful as template) - letter"
        )

    def test_subtitle_easy_a4(self):
        query = QueryDict("prefilled_values=easy&paper_size=a4")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Easy Numbers (1 digits) - a4"
        )

    def test_subtitle_easy_letter(self):
        query = QueryDict("prefilled_values=easy&paper_size=letter")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Easy Numbers (1 digits) - letter"
        )

    def test_subtitle_medium_a4(self):
        query = QueryDict("prefilled_values=medium&paper_size=a4")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Medium Numbers (2 digits) - a4"
        )

    def test_subtitle_medium_letter(self):
        query = QueryDict("prefilled_values=medium&paper_size=letter")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Medium Numbers (2 digits) - letter"
        )

    def test_subtitle_hard_a4(self):
        query = QueryDict("prefilled_values=hard&paper_size=a4")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Hard Numbers (3 digits) - a4"
        )

    def test_subtitle_hard_letter(self):
        query = QueryDict("prefilled_values=hard&paper_size=letter")
        generator = SortingNetworkResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Hard Numbers (3 digits) - letter"
        )
