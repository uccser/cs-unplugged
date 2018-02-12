from tests.BaseTestWithDB import BaseTestWithDB
from classic.models import ClassicPage
from classic.management.commands._ClassicPagesLoader import ClassicPagesLoader
from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.EmptyYAMLFileError import EmptyYAMLFileError


class ResourceLoaderTest(BaseTestWithDB):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loader_name = "classicpage"
        self.BASE_PATH = "tests/classic/loaders/assets/classicpages/"

    def test_basic_classicpage_loader_config(self):
        config_file = "basic-config.yaml"
        classicpage_loader = ClassicPagesLoader(
            structure_dir="",
            structure_filename=config_file,
            base_path=self.BASE_PATH,
        )
        classicpage_loader.load()
        pages = ClassicPage.objects.all()
        self.assertEqual(1, len(pages))
        page = pages[0]
        self.assertEqual("Binary numbers", page.name)
        self.assertEqual("binary-numbers", page.slug)
        self.assertEqual("https://classic.csunplugged.org/binary-numbers", page.redirect)

    def test_classicpage_loader_missing_configuration_file(self):
        config_file = "missing.yaml"
        classicpage_loader = ClassicPagesLoader(
            structure_dir="",
            structure_filename=config_file,
            base_path=self.BASE_PATH,
        )
        self.assertRaises(
            CouldNotFindYAMLFileError,
            classicpage_loader.load,
        )

    def test_classicpage_loader_empty_configuration_file(self):
        config_file = "empty.yaml"
        classicpage_loader = ClassicPagesLoader(
            structure_dir="",
            structure_filename=config_file,
            base_path=self.BASE_PATH,
        )
        self.assertRaises(
            EmptyYAMLFileError,
            classicpage_loader.load,
        )

    def test_classicpage_loader_missing_name_value(self):
        config_file = "missing-name.yaml"
        classicpage_loader = ClassicPagesLoader(
            structure_dir="",
            structure_filename=config_file,
            base_path=self.BASE_PATH,
        )
        self.assertRaises(
            MissingRequiredFieldError,
            classicpage_loader.load,
        )

    def test_classicpage_loader_multiple_configuration(self):
        config_file = "multiple.yaml"
        classicpage_loader = ClassicPagesLoader(
            structure_dir="",
            structure_filename=config_file,
            base_path=self.BASE_PATH,
        )
        classicpage_loader.load()
        pages = ClassicPage.objects.order_by("name")
        self.assertEqual(4, len(pages))
        self.assertQuerysetEqual(
            pages,
            [
                "<ClassicPage: Activities>",
                "<ClassicPage: Artificial intelligence>",
                "<ClassicPage: Binary numbers>",
                "<ClassicPage: CS Unplugged Book>",
            ],
        )
