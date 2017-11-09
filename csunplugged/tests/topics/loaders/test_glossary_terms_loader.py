import os.path
from unittest.mock import Mock

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import GlossaryTerm
from topics.management.commands._GlossaryTermsLoader import GlossaryTermsLoader


class GlossaryTermsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.config_file = Mock()
        self.loader_name = "glossary_terms"
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        folder = "glossary_folder"
        glossary_loader = GlossaryTermsLoader(folder, self.config_file, self.BASE_PATH)
        glossary_loader.load()
        glossary_objects = GlossaryTerm.objects.all()
        self.assertQuerysetEqual(
            glossary_objects,
            ["<GlossaryTerm: Glossary Term 1>"]
        )

    def test_multiple_files(self):
        folder = "glossary_folder_multiple"
        glossary_loader = GlossaryTermsLoader(folder, self.config_file, self.BASE_PATH)
        glossary_loader.load()
        glossary_objects = GlossaryTerm.objects.order_by("term")
        self.assertQuerysetEqual(
            glossary_objects,
            [
                "<GlossaryTerm: Glossary Term 1>",
                "<GlossaryTerm: Glossary Term 2>",
                "<GlossaryTerm: Glossary Term 3>"
            ],
        )

    def test_invalid_files(self):
        folder = "invalid_files"
        glossary_loader = GlossaryTermsLoader(folder, self.config_file, self.BASE_PATH)
        glossary_loader.load()
        glossary_objects = GlossaryTerm.objects.all()
        self.assertQuerysetEqual(
            glossary_objects,
            ["<GlossaryTerm: Glossary Term 1>"]
        )
