from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.LeftRightCardsResourceGenerator import LeftRightCardsResourceGenerator


@tag("resource")
class LeftRightCardsResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

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
