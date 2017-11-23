from django.http import QueryDict
from django.test import tag
from resources.generators.LeftRightCardsResourceGenerator import LeftRightCardsResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class LeftRightCardsResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_data(self):
        generator = LeftRightCardsResourceGenerator()
        data = generator.data()
        self.assert_data_valid(data)

    def test_subtitle_a4(self):
        query = QueryDict("paper_size=a4")
        generator = LeftRightCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "a4"
        )

    def test_subtitle_letter(self):
        query = QueryDict("paper_size=letter")
        generator = LeftRightCardsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "letter"
        )
