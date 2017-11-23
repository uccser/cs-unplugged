from django.http import QueryDict
from django.test import tag
from resources.generators.GridResourceGenerator import GridResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class GridResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_data(self):
        generator = GridResourceGenerator()
        data = generator.data()
        self.assert_data_valid(data)

    def test_subtitle_a4(self):
        query = QueryDict("paper_size=a4")
        generator = GridResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "a4"
        )

    def test_subtitle_letter(self):
        query = QueryDict("paper_size=letter")
        generator = GridResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "letter"
        )
