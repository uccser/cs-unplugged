from django.http import QueryDict
from django.test import tag
from resources.generators.HashTableTwentySlotsWorksheetResourceGenerator import HashTableTwentySlotsWorksheetResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class HashTableTwentySlotsWorksheetResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_data(self):
        generator = HashTableTwentySlotsWorksheetResourceGenerator()
        data = generator.data()
        self.assert_data_valid(data)

    def test_subtitle_a4(self):
        query = QueryDict("paper_size=a4")
        generator = HashTableTwentySlotsWorksheetResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "a4"
        )

    def test_subtitle_letter(self):
        query = QueryDict("paper_size=letter")
        generator = HashTableTwentySlotsWorksheetResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "letter"
        )
