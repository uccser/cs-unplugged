from django.http import QueryDict
from django.test import tag
from resources.generators.RandomNumbersResourceGenerator import RandomNumbersResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class RandomNumbersResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_data(self):
        generator = RandomNumbersResourceGenerator()
        data = generator.data()
        self.assert_data_valid(data)

    def test_subtitle_a4(self):
        query = QueryDict("paper_size=a4")
        generator = RandomNumbersResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "a4"
        )

    def test_subtitle_letter(self):
        query = QueryDict("paper_size=letter")
        generator = RandomNumbersResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "letter"
        )
