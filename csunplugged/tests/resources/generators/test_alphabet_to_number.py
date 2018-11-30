from unittest import mock
from django.http import QueryDict
from django.test import tag
from resources.generators.AlphabetToNumberResourceGenerator import AlphabetToNumberResourceGenerator
from tests.resources.generators.utils import BaseGeneratorTest


@tag("resource")
class AlphabetToNumberResourceGenerator(BaseGeneratorTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    # def test_data(self):
    #     generator = AlphabetToNumberResourceGenerator()
    #     data = generator.data()
    #     self.assert_data_valid(data)

    # def test_subtitle_a4(self):
    #     query = QueryDict("paper_size=a4")
    #     generator = AlphabetToNumberResourceGenerator(query)
    #     self.assertEqual(
    #         generator.subtitle,
    #         "a4"
    #     )

    # def test_subtitle_letter(self):
    #     query = QueryDict("paper_size=letter")
    #     generator = AlphabetToNumberResourceGenerator(query)
    #     self.assertEqual(
    #         generator.subtitle,
    #         "letter"
    #     )
    
    # @mock.patch(
    #     "utils.alphabets.get_alphabet",
    #     return_value=["a", "b", "c", "d"]
    # )
    # def test_even_columns(self, get_alphabet):
    #     query = QueryDict("paper_size=a4")
    #     generator = AlphabetToNumberResourceGenerator(query)
    #     generator.data()
    #     self.assertTrue(get_alphabet.called)

    # @mock.patch(
    #     "utils.alphabets.get_alphabet",
    #     return_value=["a", "b", "c"]
    # )
    # def test_uneven_columns(self, get_alphabet):
    #     query = QueryDict("paper_size=a4")
    #     generator = AlphabetToNumberResourceGenerator(query)
    #     generator.data()
