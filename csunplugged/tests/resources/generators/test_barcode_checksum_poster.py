from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.BarcodeChecksumPosterResourceGenerator import BarcodeChecksumPosterResourceGenerator
from tests.resources.generators.utils import run_parameter_smoke_tests

@tag("resource")
class BarcodeChecksumPosterResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"
        self.base_valid_query = QueryDict("barcode_length=12&paper_size=a4")

    def test_barcode_length_values(self):
        generator = BarcodeChecksumPosterResourceGenerator(self.base_valid_query)
        run_parameter_smoke_tests(generator, "barcode_length")

    def test_subtitle_12_a4(self):
        query = QueryDict("barcode_length=12&paper_size=a4")
        generator = BarcodeChecksumPosterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "12 digits - a4"
        )

    def test_subtitle_12_letter(self):
        query = QueryDict("barcode_length=12&paper_size=letter")
        generator = BarcodeChecksumPosterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "12 digits - letter"
        )

    def test_subtitle_13_a4(self):
        query = QueryDict("barcode_length=13&paper_size=a4")
        generator = BarcodeChecksumPosterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "13 digits - a4"
        )

    def test_subtitle_13_letter(self):
        query = QueryDict("barcode_length=13&paper_size=letter")
        generator = BarcodeChecksumPosterResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "13 digits - letter"
        )
