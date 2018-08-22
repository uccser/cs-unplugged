from django.http import QueryDict
from django.test import tag
from resources.generators.TrainStationsResourceGenerator import TrainStationsResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class TrainStationsResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("tracks=circular&paper_size=a4")

    def test_tracks_values(self):
        generator = TrainStationsResourceGenerator(self.base_valid_query)
        self.run_parameter_smoke_tests(generator, "tracks")

    def test_subtitle_circular_a4(self):
        query = QueryDict("tracks=circular&paper_size=a4")
        generator = TrainStationsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Circular - a4"
        )

    def test_subtitle_circular_letter(self):
        query = QueryDict("tracks=circular&paper_size=letter")
        generator = TrainStationsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Circular - letter"
        )

    def test_subtitle_twisted_a4(self):
        query = QueryDict("tracks=twisted&paper_size=a4")
        generator = TrainStationsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Twisted - a4"
        )

    def test_subtitle_twisted_letter(self):
        query = QueryDict("tracks=twisted&paper_size=letter")
        generator = TrainStationsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "Twisted - letter"
        )
