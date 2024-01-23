import os.path

from django.utils import translation

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import GlossaryTerm
from topics.management.commands._GlossaryTermsLoader import GlossaryTermsLoader


class GlossaryTermsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "glossary_terms"
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        folder = "glossary_folder"
        glossary_loader = GlossaryTermsLoader(base_path=self.base_path, content_path=folder)
        glossary_loader.load()
        glossary_objects = GlossaryTerm.objects.all()
        self.assertQuerysetEqual(
            glossary_objects,
            ["<GlossaryTerm: Glossary Term 1 English>"],
            transform=repr,
        )

    def test_multiple_files(self):
        folder = "glossary_folder_multiple"
        glossary_loader = GlossaryTermsLoader(base_path=self.base_path, content_path=folder)
        glossary_loader.load()
        glossary_objects = GlossaryTerm.objects.order_by("term")
        self.assertQuerysetEqual(
            glossary_objects,
            [
                "<GlossaryTerm: Glossary Term 1>",
                "<GlossaryTerm: Glossary Term 2>",
                "<GlossaryTerm: Glossary Term 3>"
            ],
            transform=repr,
        )

    def test_invalid_files(self):
        folder = "invalid_files"
        glossary_loader = GlossaryTermsLoader(base_path=self.base_path, content_path=folder)
        glossary_loader.load()
        glossary_objects = GlossaryTerm.objects.all()
        self.assertQuerysetEqual(
            glossary_objects,
            ["<GlossaryTerm: Glossary Term 1>"],
            transform=repr,
        )

    def test_translation(self):
        folder = "glossary_translation"

        glossary_loader = GlossaryTermsLoader(base_path=self.base_path, content_path=folder)
        glossary_loader.load()

        glossary_objects = GlossaryTerm.objects.all()
        self.assertEqual(2, len(glossary_objects))

        translated_term = GlossaryTerm.objects.get(slug="glossary-term-1")
        untranslated_term = GlossaryTerm.objects.get(slug="glossary-term-2")

        self.assertSetEqual(set(["en", "de"]), set(translated_term.languages))
        self.assertSetEqual(set(["en"]), set(untranslated_term.languages))

        self.assertEqual("Glossary Term 1 English", translated_term.term)
        self.assertIn("English definition.", translated_term.definition)
        with translation.override("de"):
            self.assertEqual("Glossary Term 1 German", translated_term.term)
            self.assertIn("German definition.", translated_term.definition)
