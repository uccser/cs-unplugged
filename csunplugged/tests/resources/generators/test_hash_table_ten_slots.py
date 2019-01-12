from django.http import QueryDict
from django.test import tag
from resources.generators.HashTableTenSlotsWorksheetResourceGenerator import HashTableTenSlotsWorksheetResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class HashTableTenSlotsWorksheetResourceGeneratorTest(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_data(self):
        generator = HashTableTenSlotsWorksheetResourceGenerator()
        data = generator.data()
        self.assert_data_valid(data)

    def test_subtitle_a4(self):
        query = QueryDict("paper_size=a4")
        generator = HashTableTenSlotsWorksheetResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "a4"
        )

    def test_subtitle_letter(self):
        query = QueryDict("paper_size=letter")
        generator = HashTableTenSlotsWorksheetResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "letter"
        )
