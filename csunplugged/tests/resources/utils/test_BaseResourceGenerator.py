from django.test import tag
from django.http import QueryDict
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from tests.resources.BareResourceGenerator import BareResourceGenerator
from unittest.mock import MagicMock
from utils.errors.ThumbnailPageNotFound import ThumbnailPageNotFound
from utils.errors.MoreThanOneThumbnailPageFound import MoreThanOneThumbnailPageFound
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from io import BytesIO
from PyPDF2 import PdfFileReader


@tag("resource")
class BaseResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()

    def test_pdf_single_page(self):
        generator = BareResourceGenerator()
        (pdf_file, filename) = generator.pdf("Test")
        pdf = PdfFileReader(BytesIO(pdf_file))
        self.assertEqual(pdf.getNumPages(), 1)

    def test_pdf_single_page_copies(self):
        generator = BareResourceGenerator(QueryDict("paper_size=a4&copies=8"))
        (pdf_file, filename) = generator.pdf("Test")
        pdf = PdfFileReader(BytesIO(pdf_file))
        self.assertEqual(pdf.getNumPages(), 8)

    def test_pdf_multiple_pages(self):
        generator = BareResourceGenerator()
        generator.data = MagicMock(
            return_value=[
                {"type": "html", "data": "Page 1"},
                {"type": "html", "data": "Page 2"},
            ]
        )
        (pdf_file, filename) = generator.pdf("Test")
        pdf = PdfFileReader(BytesIO(pdf_file))
        self.assertEqual(pdf.getNumPages(), 2)

    def test_pdf_multiple_pages_copies(self):
        generator = BareResourceGenerator(QueryDict("paper_size=a4&copies=8"))
        generator.data = MagicMock(
            return_value=[
                {"type": "html", "data": "Page 1"},
                {"type": "html", "data": "Page 2"},
            ]
        )
        (pdf_file, filename) = generator.pdf("Test")
        pdf = PdfFileReader(BytesIO(pdf_file))
        self.assertEqual(pdf.getNumPages(), 16)

    def test_generate_thumbnail_valid_single_page(self):
        generator = BareResourceGenerator()
        thumbnail_data = generator.generate_thumbnail()
        self.assertEqual(thumbnail_data["data"], "Page 1")

    def test_generate_thumbnail_valid_multiple_pages(self):
        generator = BareResourceGenerator()
        generator.data = MagicMock(
            return_value=[
                {"type": "html", "data": "Page 1"},
                {"type": "html", "data": "Page 2", "thumbnail": True}
            ]
        )
        thumbnail_data = generator.generate_thumbnail()
        self.assertEqual(thumbnail_data["data"], "Page 2")

    def test_generate_thumbnail_none_given(self):
        generator = BareResourceGenerator()
        generator.data = MagicMock(
            return_value=[
                {"type": "html", "data": ""},
                {"type": "html", "data": ""}
            ]
        )
        self.assertRaises(
            ThumbnailPageNotFound,
            generator.generate_thumbnail,
        )

    def test_generate_thumbnail_more_than_one_given(self):
        generator = BareResourceGenerator()
        generator.data = MagicMock(
            return_value=[
                {"type": "html", "data": "", "thumbnail": True},
                {"type": "html", "data": "", "thumbnail": True}
            ]
        )
        self.assertRaises(
            MoreThanOneThumbnailPageFound,
            generator.generate_thumbnail,
        )

    def test_data_not_implemented(self):
        # Create generator without data method defined.
        class InvalidGenerator(BaseResourceGenerator):
            pass

        with self.assertRaises(TypeError):
            generator = InvalidGenerator()
