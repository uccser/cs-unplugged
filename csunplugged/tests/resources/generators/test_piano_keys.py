from django.http import QueryDict
from django.test import tag
from resources.generators.PianoKeysResourceGenerator import PianoKeysResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class PianoKeysResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("label=no&paper_size=a4")

    def test_label_values(self):
        generator = PianoKeysResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "label")

    def test_subtitle_no_a4(self):
        query = QueryDict("label=no&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Blank - a4"
        )

    def test_subtitle_no_letter(self):
        query = QueryDict("label=no&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Blank - letter"
        )

    def test_subtitle_type_1_a4(self):
        query = QueryDict("label=type-1&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "C, D, E, F, G, A, B - a4"
        )

    def test_subtitle_type_1_letter(self):
        query = QueryDict("label=type-1&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "C, D, E, F, G, A, B - letter"
        )

    def test_subtitle_type_2_a4(self):
        query = QueryDict("label=type-2&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "C, D, E, F, G, A, H - a4"
        )

    def test_subtitle_type_2_letter(self):
        query = QueryDict("label=type-2&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "C, D, E, F, G, A, H - letter"
        )

    def test_subtitle_type_3_a4(self):
        query = QueryDict("label=type-3&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Do, Re, Mi, Fa, So, La, Ti - a4"
        )

    def test_subtitle_type_3_letter(self):
        query = QueryDict("label=type-3&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Do, Re, Mi, Fa, So, La, Ti - letter"
        )

    def test_subtitle_type_4_a4(self):
        query = QueryDict("label=type-4&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Do, Re, Mi, Fa, Sol, La, Si - a4"
        )

    def test_subtitle_type_4_letter(self):
        query = QueryDict("label=type-4&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Do, Re, Mi, Fa, Sol, La, Si - letter"
        )
