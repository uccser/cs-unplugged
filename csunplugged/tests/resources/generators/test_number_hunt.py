from django.http import QueryDict
from django.test import tag
from resources.generators.NumberHuntResourceGenerator import NumberHuntResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class NumberHuntResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict(
            "prefilled_values=easy&number_order=sorted&paper_size=a4"
        )

    def test_prefilled_values_values(self):
        generator = NumberHuntResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "prefilled_values")

    def test_number_order_values(self):
        generator = NumberHuntResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "number_order")

    def test_get_range_descriptor(self):
        get_number_range = NumberHuntResourceGenerator.get_number_range
        self.assertEqual((0, 100, 70), get_number_range("easy"))
        self.assertEqual((0, 1000, 65), get_number_range("medium"))
        self.assertEqual((0, 10000, 60), get_number_range("hard"))

    def test_get_range_descriptor_invalid(self):
        get_number_range = NumberHuntResourceGenerator.get_number_range
        with self.assertRaises(ValueError):
            get_number_range("invalid")

    def test_subtitle_a4(self):
        query = QueryDict("prefilled_values=easy&number_order=sorted&paper_size=a4")
        generator = NumberHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted Numbers - 0 to 99 - a4"
        )

    def test_subtitle_letter(self):
        query = QueryDict("prefilled_values=easy&number_order=sorted&paper_size=letter")
        generator = NumberHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted Numbers - 0 to 99 - letter"
        )

    def test_subtitle_sorted(self):
        query = QueryDict("prefilled_values=easy&number_order=sorted&paper_size=a4")
        generator = NumberHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted Numbers - 0 to 99 - a4"
        )

    def test_subtitle_unsorted(self):
        query = QueryDict("prefilled_values=easy&number_order=unsorted&paper_size=a4")
        generator = NumberHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted Numbers - 0 to 99 - a4"
        )

    def test_subtitle_blank(self):
        query = QueryDict("prefilled_values=blank&number_order=sorted&paper_size=a4")
        generator = NumberHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Blank - a4"
        )

    def test_subtitle_easy(self):
        query = QueryDict("prefilled_values=easy&number_order=sorted&paper_size=a4")
        generator = NumberHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted Numbers - 0 to 99 - a4"
        )

    def test_subtitle_medium(self):
        query = QueryDict("prefilled_values=medium&number_order=sorted&paper_size=a4")
        generator = NumberHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted Numbers - 0 to 999 - a4"
        )

    def test_subtitle_hard(self):
        query = QueryDict("prefilled_values=hard&number_order=sorted&paper_size=a4")
        generator = NumberHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted Numbers - 0 to 9999 - a4"
        )
