from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.ArrowsResourceGenerator import ArrowsResourceGenerator


@tag("resource")
class ArrowsResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_subtitle_a4(self):
        query = QueryDict("paper_size=a4")
        generator = ArrowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "a4"
        )

    def test_subtitle_letter(self):
        query = QueryDict("paper_size=letter")
        generator = ArrowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "letter"
        )
