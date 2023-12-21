from django.test import tag
from django.http import QueryDict
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from tests.resources.BareResourceGenerator import BareResourceGenerator, BareResourceGeneratorWithCopies
from unittest.mock import MagicMock
from utils.errors.ThumbnailPageNotFoundError import ThumbnailPageNotFoundError
from utils.errors.MoreThanOneThumbnailPageFoundError import MoreThanOneThumbnailPageFoundError
from resources.utils.BaseResourceGenerator import BaseResourceGenerator
from resources.utils.resource_parameters import ResourceParameter, EnumResourceParameter
from io import BytesIO
from pypdf import PdfReader


@tag("resource")
class BaseResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()

    def test_pdf_single_page(self):
        generator = BareResourceGenerator()
        (pdf_file, filename) = generator.pdf("Test")
        pdf = PdfReader(BytesIO(pdf_file))
        self.assertEqual(len(pdf.pages), 1)

    def test_pdf_single_page_copies(self):
        generator = BareResourceGeneratorWithCopies(QueryDict("paper_size=a4&copies=8"))
        (pdf_file, filename) = generator.pdf("Test")
        pdf = PdfReader(BytesIO(pdf_file))
        self.assertEqual(len(pdf.pages), 8)

    def test_pdf_multiple_pages(self):
        generator = BareResourceGenerator()
        generator.data = MagicMock(
            return_value=[
                {"type": "html", "data": "Page 1"},
                {"type": "html", "data": "Page 2"},
            ]
        )
        (pdf_file, filename) = generator.pdf("Test")
        pdf = PdfReader(BytesIO(pdf_file))
        self.assertEqual(len(pdf.pages), 2)

    def test_pdf_multiple_pages_copies(self):
        generator = BareResourceGeneratorWithCopies(QueryDict("paper_size=a4&copies=8"))
        generator.data = MagicMock(
            return_value=[
                {"type": "html", "data": "Page 1"},
                {"type": "html", "data": "Page 2"},
            ]
        )
        (pdf_file, filename) = generator.pdf("Test")
        pdf = PdfReader(BytesIO(pdf_file))
        self.assertEqual(len(pdf.pages), 16)

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
            ThumbnailPageNotFoundError,
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
            MoreThanOneThumbnailPageFoundError,
            generator.generate_thumbnail,
        )

    def test_data_not_implemented(self):
        # Create generator without data method defined.
        class InvalidGenerator(BaseResourceGenerator):
            pass

        with self.assertRaises(TypeError):
            InvalidGenerator()

    def test_get_options(self):
        options = BaseResourceGenerator.get_options()
        options_order = ["paper_size"]
        # check options are correct, including ordering
        self.assertListEqual(options_order, list(options))
        for option in options.values():
            self.assertIsInstance(option, ResourceParameter)

    def test_get_local_options(self):
        local_options = BaseResourceGenerator.get_local_options()
        options_order = ["header_text"]
        self.assertListEqual(options_order, list(local_options))
        for option in local_options.values():
            self.assertIsInstance(option, ResourceParameter)

    def test_get_local_options_with_copies(self):
        class SubclassWithCopies(BaseResourceGenerator):
            copies = True
        local_options = SubclassWithCopies.get_local_options()
        options_order = ["header_text", "copies"]
        self.assertListEqual(options_order, list(local_options))
        for option in local_options.values():
            self.assertIsInstance(option, ResourceParameter)

    def test_all_options(self):
        generator = BareResourceGenerator()
        normal_options = generator.get_options()
        local_options = generator.get_local_options()
        # Order should be normal options, then local options
        options_order = list(normal_options) + list(local_options)
        self.assertListEqual(options_order, list(generator.options))
        for option in local_options.values():
            self.assertIsInstance(option, ResourceParameter)

    def test_get_options_subclass_additional_options(self):
        class GeneratorSubclass(BaseResourceGenerator):
            @classmethod
            def get_additional_options(cls):
                return {
                    "subclass_option": EnumResourceParameter(
                        name="subclass_option",
                        description="Description",
                        values={"value1": "Value 1"}
                    ),
                }

        options = GeneratorSubclass.get_options()
        # Subclass options before base class options
        options_order = ["subclass_option", "paper_size"]
        self.assertListEqual(options_order, list(options))
        for option in options.values():
            self.assertIsInstance(option, ResourceParameter)

    def test_get_local_options_subclass_additional_local_options(self):
        class GeneratorSubclass(BaseResourceGenerator):

            @classmethod
            def get_additional_options(cls):
                return {
                    "subclass_local_option": EnumResourceParameter(
                        name="subclass_local_option",
                        description="Description",
                        values={"value1": "Value 1"}
                    ),
                }

        local_options = GeneratorSubclass.get_options()
        # Subclass options before base class options
        options_order = ["subclass_local_option", "paper_size"]
        self.assertListEqual(options_order, list(local_options))
        for option in local_options.values():
            self.assertIsInstance(option, ResourceParameter)

    def test_get_option_defaults(self):
        option_defaults = BaseResourceGenerator.get_option_defaults()
        self.assertEqual(
            option_defaults,
            {
                "paper_size": "a4",
            }
        )
