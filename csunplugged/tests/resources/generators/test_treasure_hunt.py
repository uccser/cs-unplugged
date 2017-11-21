from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.TreasureHuntResourceGenerator import TreasureHuntResourceGenerator
from tests.resources.generators.utils import run_parameter_smoke_tests


@tag("resource")
class TreasureHuntResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict(
            "prefilled_values=blank&number_order=sorted&instructions=yes&art=colour&paper_size=a4"
        )

    def test_prefilled_values_values(self):
        generator = TreasureHuntResourceGenerator(self.base_valid_query)
        run_parameter_smoke_tests(generator, "prefilled_values")

    def test_number_order_values(self):
        generator = TreasureHuntResourceGenerator(self.base_valid_query)
        run_parameter_smoke_tests(generator, "number_order")

    def test_instructions_values(self):
        generator = TreasureHuntResourceGenerator(self.base_valid_query)
        run_parameter_smoke_tests(generator, "instructions")

    def test_art_values(self):
        generator = TreasureHuntResourceGenerator(self.base_valid_query)
        run_parameter_smoke_tests(generator, "art")

    def test_subtitle_blank_sorted_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=sorted&instructions=yes&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - full colour - with instructions - a4"
        )

    def test_subtitle_blank_sorted_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=sorted&instructions=yes&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - full colour - with instructions - letter"
        )

    def test_subtitle_blank_unsorted_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=unsorted&instructions=yes&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - full colour - with instructions - a4"
        )

    def test_subtitle_blank_unsorted_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=unsorted&instructions=yes&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - full colour - with instructions - letter"
        )

    def test_subtitle_blank_sorted_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=sorted&instructions=yes&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - black and white - with instructions - a4"
        )

    def test_subtitle_blank_sorted_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=sorted&instructions=yes&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - black and white - with instructions - letter"
        )

    def test_subtitle_blank_unsorted_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=unsorted&instructions=yes&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - black and white - with instructions - a4"
        )

    def test_subtitle_blank_unsorted_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=unsorted&instructions=yes&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - black and white - with instructions - letter"
        )

    def test_subtitle_blank_sorted_no_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=sorted&instructions=no&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - full colour - without instructions - a4"
        )

    def test_subtitle_blank_sorted_no_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=sorted&instructions=no&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - full colour - without instructions - letter"
        )

    def test_subtitle_blank_unsorted_no_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=unsorted&instructions=no&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - full colour - without instructions - a4"
        )

    def test_subtitle_blank_unsorted_no_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=unsorted&instructions=no&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - full colour - without instructions - letter"
        )

    def test_subtitle_blank_sorted_no_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=sorted&instructions=no&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - black and white - without instructions - a4"
        )

    def test_subtitle_blank_sorted_no_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=sorted&instructions=no&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - black and white - without instructions - letter"
        )

    def test_subtitle_blank_unsorted_no_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=unsorted&instructions=no&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - black and white - without instructions - a4"
        )

    def test_subtitle_blank_unsorted_no_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=blank&number_order=unsorted&instructions=no&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "blank - black and white - without instructions - letter"
        )

    def test_subtitle_easy_sorted_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=sorted&instructions=yes&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 99 - full colour - with instructions - a4"
        )

    def test_subtitle_easy_sorted_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=sorted&instructions=yes&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 99 - full colour - with instructions - letter"
        )

    def test_subtitle_easy_unsorted_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=unsorted&instructions=yes&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 99 - full colour - with instructions - a4"
        )

    def test_subtitle_easy_unsorted_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=unsorted&instructions=yes&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 99 - full colour - with instructions - letter"
        )

    def test_subtitle_easy_sorted_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=sorted&instructions=yes&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 99 - black and white - with instructions - a4"
        )

    def test_subtitle_easy_sorted_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=sorted&instructions=yes&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 99 - black and white - with instructions - letter"
        )

    def test_subtitle_easy_unsorted_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=unsorted&instructions=yes&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 99 - black and white - with instructions - a4"
        )

    def test_subtitle_easy_unsorted_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=unsorted&instructions=yes&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 99 - black and white - with instructions - letter"
        )

    def test_subtitle_easy_sorted_no_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=sorted&instructions=no&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 99 - full colour - without instructions - a4"
        )

    def test_subtitle_easy_sorted_no_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=sorted&instructions=no&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 99 - full colour - without instructions - letter"
        )

    def test_subtitle_easy_unsorted_no_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=unsorted&instructions=no&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 99 - full colour - without instructions - a4"
        )

    def test_subtitle_easy_unsorted_no_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=unsorted&instructions=no&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 99 - full colour - without instructions - letter"
        )

    def test_subtitle_easy_sorted_no_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=sorted&instructions=no&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 99 - black and white - without instructions - a4"
        )

    def test_subtitle_easy_sorted_no_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=sorted&instructions=no&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 99 - black and white - without instructions - letter"
        )

    def test_subtitle_easy_unsorted_no_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=unsorted&instructions=no&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 99 - black and white - without instructions - a4"
        )

    def test_subtitle_easy_unsorted_no_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=easy&number_order=unsorted&instructions=no&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 99 - black and white - without instructions - letter"
        )

    def test_subtitle_medium_sorted_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=sorted&instructions=yes&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 999 - full colour - with instructions - a4"
        )

    def test_subtitle_medium_sorted_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=sorted&instructions=yes&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 999 - full colour - with instructions - letter"
        )

    def test_subtitle_medium_unsorted_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=unsorted&instructions=yes&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 999 - full colour - with instructions - a4"
        )

    def test_subtitle_medium_unsorted_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=unsorted&instructions=yes&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 999 - full colour - with instructions - letter"
        )

    def test_subtitle_medium_sorted_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=sorted&instructions=yes&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 999 - black and white - with instructions - a4"
        )

    def test_subtitle_medium_sorted_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=sorted&instructions=yes&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 999 - black and white - with instructions - letter"
        )

    def test_subtitle_medium_unsorted_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=unsorted&instructions=yes&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 999 - black and white - with instructions - a4"
        )

    def test_subtitle_medium_unsorted_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=unsorted&instructions=yes&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 999 - black and white - with instructions - letter"
        )

    def test_subtitle_medium_sorted_no_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=sorted&instructions=no&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 999 - full colour - without instructions - a4"
        )

    def test_subtitle_medium_sorted_no_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=sorted&instructions=no&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 999 - full colour - without instructions - letter"
        )

    def test_subtitle_medium_unsorted_no_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=unsorted&instructions=no&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 999 - full colour - without instructions - a4"
        )

    def test_subtitle_medium_unsorted_no_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=unsorted&instructions=no&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 999 - full colour - without instructions - letter"
        )

    def test_subtitle_medium_sorted_no_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=sorted&instructions=no&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 999 - black and white - without instructions - a4"
        )

    def test_subtitle_medium_sorted_no_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=sorted&instructions=no&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 999 - black and white - without instructions - letter"
        )

    def test_subtitle_medium_unsorted_no_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=unsorted&instructions=no&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 999 - black and white - without instructions - a4"
        )

    def test_subtitle_medium_unsorted_no_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=medium&number_order=unsorted&instructions=no&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 999 - black and white - without instructions - letter"
        )

    def test_subtitle_hard_sorted_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=sorted&instructions=yes&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 9999 - full colour - with instructions - a4"
        )

    def test_subtitle_hard_sorted_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=sorted&instructions=yes&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 9999 - full colour - with instructions - letter"
        )

    def test_subtitle_hard_unsorted_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=unsorted&instructions=yes&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 9999 - full colour - with instructions - a4"
        )

    def test_subtitle_hard_unsorted_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=unsorted&instructions=yes&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 9999 - full colour - with instructions - letter"
        )

    def test_subtitle_hard_sorted_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=sorted&instructions=yes&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 9999 - black and white - with instructions - a4"
        )

    def test_subtitle_hard_sorted_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=sorted&instructions=yes&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 9999 - black and white - with instructions - letter"
        )

    def test_subtitle_hard_unsorted_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=unsorted&instructions=yes&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 9999 - black and white - with instructions - a4"
        )

    def test_subtitle_hard_unsorted_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=unsorted&instructions=yes&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 9999 - black and white - with instructions - letter"
        )

    def test_subtitle_hard_sorted_no_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=sorted&instructions=no&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 9999 - full colour - without instructions - a4"
        )

    def test_subtitle_hard_sorted_no_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=sorted&instructions=no&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 9999 - full colour - without instructions - letter"
        )

    def test_subtitle_hard_unsorted_no_instructions_colour_a4(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=unsorted&instructions=no&art=colour&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 9999 - full colour - without instructions - a4"
        )

    def test_subtitle_hard_unsorted_no_instructions_colour_letter(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=unsorted&instructions=no&art=colour&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 9999 - full colour - without instructions - letter"
        )

    def test_subtitle_hard_sorted_no_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=sorted&instructions=no&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 9999 - black and white - without instructions - a4"
        )

    def test_subtitle_hard_sorted_no_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=sorted&instructions=no&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Sorted - 0 to 9999 - black and white - without instructions - letter"
        )

    def test_subtitle_hard_unsorted_no_instructions_bw_a4(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=unsorted&instructions=no&art=bw&paper_size=a4"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 9999 - black and white - without instructions - a4"
        )

    def test_subtitle_hard_unsorted_no_instructions_bw_letter(self):
        query = QueryDict(
            "prefilled_values=hard&number_order=unsorted&instructions=no&art=bw&paper_size=letter"
        )
        generator = TreasureHuntResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Unsorted - 0 to 9999 - black and white - without instructions - letter"
        )
