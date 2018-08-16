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
            "no labels - a4"
        )

    def test_subtitle_no_letter(self):
        query = QueryDict("label=no&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "no labels - letter"
        )

    def test_subtitle_type_1_a4(self):
        query = QueryDict("label=type-1&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "type-1 labels - a4"
        )

    def test_subtitle_type_1_letter(self):
        query = QueryDict("label=type-1&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "type-1 labels - letter"
        )

    def test_subtitle_type_2_a4(self):
        query = QueryDict("label=type-2&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "type-2 labels - a4"
        )

    def test_subtitle_type_2_letter(self):
        query = QueryDict("label=type-2&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "type-2 labels - letter"
        )

    def test_subtitle_type_3_a4(self):
        query = QueryDict("label=type-3&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "type-3 labels - a4"
        )

    def test_subtitle_type_3_letter(self):
        query = QueryDict("label=type-3&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "type-3 labels - letter"
        )

    def test_subtitle_type_4_a4(self):
        query = QueryDict("label=type-4&paper_size=a4")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "type-4 labels - a4"
        )

    def test_subtitle_type_4_letter(self):
        query = QueryDict("label=type-4&paper_size=letter")
        generator = PianoKeysResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "type-4 labels - letter"
        )
