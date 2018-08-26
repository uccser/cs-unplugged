from django.http import QueryDict
from django.test import tag
from resources.generators.TreasureIslandResourceGenerator import TreasureIslandResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class TreasureIslandResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("type=map&paper_size=a4")

    def test_type_values(self):
        generator = TreasureIslandResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "type")

    def test_subtitle_map_a4(self):
        query = QueryDict("type=map&paper_size=a4")
        generator = TreasureIslandResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Student map - a4"
        )

    def test_subtitle_map_letter(self):
        query = QueryDict("type=map&paper_size=letter")
        generator = TreasureIslandResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Island posters - letter"
        )

    def test_subtitle_islands_a4(self):
        query = QueryDict("type=islands&paper_size=a4")
        generator = TreasureIslandResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Student map - a4"
        )

    def test_subtitle_islands_letter(self):
        query = QueryDict("type=islands&paper_size=letter")
        generator = TreasureIslandResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Island posters - letter"
        )
