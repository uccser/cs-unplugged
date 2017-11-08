"""Test class for TranslatableModelLoader."""

from django.test import SimpleTestCase
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.errors.MissingRequiredModelsError import MissingRequiredModelsError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from django.utils import translation
from unittest import mock
from modeltranslation import settings


class MockTranslatableModel(object):
    """Mock behaviour of a translatable model registered with django-modeltranslation."""
    def __init__(self, translatable_fields=[]):
        self.translatable_fields = translatable_fields

    def __setattr__(self, field, value):
        # Set property first to prevent recursiong on self.translatable_fields
        super().__setattr__(field, value)
        if field in self.translatable_fields:
            # Remove property just created
            delattr(self, field)
            language = translation.get_language()
            field = "{}_{}".format(field, language)
            super().__setattr__(field, value)

    def __getattr__(self, field):
        if field in self.translatable_fields:
            language = translation.get_language()
            field_template = "{}_{}"
            trans_field = field_template.format(field, language)
            try:
                return super().__getattribute__(trans_field)
            except AttributeError:
                if language == "en":
                    return ""
                elif settings.ENABLE_FALLBACKS:
                    with translation.override("en"):
                        return getattr(self, field)
                else:
                    return None


class TranslatableModelLoaderTest(SimpleTestCase):
    """Test class for TranslatableModelLoader."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_path = "tests/utils/translatable_model_loader/assets"

    def test_get_yaml_translations_english(self):
        yaml_file = "basic.yaml"
        loader = TranslatableModelLoader(base_path=self.base_path)
        translations = loader.get_yaml_translations(yaml_file)

        self.assertIsInstance(translations, dict)
        self.assertSetEqual(set(["model1", "model2"]), set(translations.keys()))

        model1_translations = translations["model1"]
        self.assertIsInstance(model1_translations, dict)
        self.assertSetEqual(set(["en"]), set(model1_translations.keys()))
        model1_english = model1_translations["en"]
        self.assertIsInstance(model1_english, dict)
        self.assertSetEqual(set(["field1", "field2"]), set(model1_english.keys()))
        self.assertEqual("value 1-1", model1_english["field1"])
        self.assertEqual("value 1-2", model1_english["field2"])

        model2_translations = translations["model2"]
        self.assertIsInstance(model2_translations, dict)
        self.assertSetEqual(set(["en"]), set(model2_translations.keys()))
        model2_english = model2_translations["en"]
        self.assertIsInstance(model2_english, dict)
        self.assertSetEqual(set(["field1", "field2"]), set(model2_english.keys()))
        self.assertEqual("value 2-1", model2_english["field1"])
        self.assertEqual("value 2-2", model2_english["field2"])

    def test_get_yaml_translations_english_missing_reqd_field(self):
        yaml_file = "missingreqdfield.yaml"
        loader = TranslatableModelLoader(base_path=self.base_path)
        with self.assertRaises(MissingRequiredFieldError):
            loader.get_yaml_translations(yaml_file, required_fields=["field1"])

    def test_get_yaml_translations_english_missing_reqd_slug(self):
        yaml_file = "missingreqdslug.yaml"
        loader = TranslatableModelLoader(base_path=self.base_path)
        with self.assertRaises(MissingRequiredModelsError):
            loader.get_yaml_translations(yaml_file, required_slugs=["model1", "model2"])

    def test_get_yaml_translations_english_missing_file_with_reqd_slugs(self):
        yaml_file = "doesnotexist.yaml"
        loader = TranslatableModelLoader(base_path=self.base_path)
        # With required slugs, a missing english yaml file should raise Exception
        with self.assertRaises(CouldNotFindYAMLFileError):
            loader.get_yaml_translations(yaml_file, required_slugs=["model1", "model2"])

    def test_get_yaml_translations_english_missing_yaml_no_reqd_slugs(self):
        yaml_file = "doesnotexist.yaml"
        loader = TranslatableModelLoader(base_path=self.base_path)
        # If no required slugs, no error should be raised
        loader.get_yaml_translations(yaml_file)

    def test_get_yaml_translations_field_map(self):
        yaml_file = "basic.yaml"
        loader = TranslatableModelLoader(base_path=self.base_path)
        translations = loader.get_yaml_translations(
            yaml_file,
            field_map={"field1": "new_field1"}
        )
        model1 = translations["model1"]["en"]
        self.assertSetEqual(set(["new_field1", "field2"]), set(model1.keys()))
        self.assertEqual("value 1-1", model1["new_field1"])

    def test_get_yaml_translations_translated(self):
        yaml_file = "translation.yaml"
        loader = TranslatableModelLoader(base_path=self.base_path)
        translations = loader.get_yaml_translations(yaml_file)

        self.assertIsInstance(translations, dict)
        self.assertSetEqual(set(["model1", "model2"]), set(translations.keys()))

        model1_translations = translations["model1"]
        self.assertIsInstance(model1_translations, dict)
        self.assertSetEqual(set(["en", "de"]), set(model1_translations.keys()))

        model1_english = model1_translations["en"]
        self.assertIsInstance(model1_english, dict)
        self.assertSetEqual(set(["field1", "field2"]), set(model1_english.keys()))
        self.assertEqual("en value 1-1", model1_english["field1"])
        self.assertEqual("en value 1-2", model1_english["field2"])

        model1_german = model1_translations["de"]
        self.assertIsInstance(model1_german, dict)
        self.assertSetEqual(set(["field1", "field2"]), set(model1_german.keys()))
        self.assertEqual("de value 1-1", model1_german["field1"])
        self.assertEqual("de value 1-2", model1_german["field2"])

    def test_get_yaml_translations_translated_missing_reqd_field(self):
        yaml_file = "translationmissingreqdfield.yaml"
        loader = TranslatableModelLoader(base_path=self.base_path)

        # required fields only apply to default language (en) so no error should be raised
        translations = loader.get_yaml_translations(yaml_file, required_fields=["field1"])
        self.assertSetEqual(set(["field1", "field2"]), set(translations["model2"]["en"].keys()))
        self.assertSetEqual(set(["field2"]), set(translations["model2"]["de"].keys()))

    def test_get_yaml_translations_translated_missing_reqd_slug(self):
        yaml_file = "translationmissingreqdslug.yaml"
        loader = TranslatableModelLoader(base_path=self.base_path)

        # required slugs only apply to default language (en) so no error should be raised
        translations = loader.get_yaml_translations(yaml_file, required_slugs=["model1", "model2"])
        self.assertSetEqual(set(["en", "de"]), set(translations["model1"].keys()))
        self.assertSetEqual(set(["en"]), set(translations["model2"].keys()))

    def test_get_markdown_translations_english(self):
        filename = "basic.md"
        loader = TranslatableModelLoader(base_path=self.base_path)
        translations = loader.get_markdown_translations(filename)
        self.assertSetEqual(set(["en"]), set(translations.keys()))
        self.assertIn("Basic Content", translations["en"].html_string)
        self.assertIn("Heading", translations["en"].title)

    def test_get_markdown_translation_english_missing_file_required(self):
        filename = "doesnotexist.md"
        loader = TranslatableModelLoader(base_path=self.base_path)
        with self.assertRaises(CouldNotFindMarkdownFileError):
            loader.get_markdown_translations(filename, required=True)

    def test_get_markdown_translation_english_missing_file_not_required(self):
        filename = "doesnotexist.md"
        loader = TranslatableModelLoader(base_path=self.base_path)
        # Should not raise error if required is False
        loader.get_markdown_translations(filename, required=False)

    def test_get_markdown_translations_translated(self):
        filename = "translation.md"
        loader = TranslatableModelLoader(base_path=self.base_path)
        translations = loader.get_markdown_translations(filename)
        self.assertSetEqual(set(["en", "de"]), set(translations.keys()))

        en = translations["en"]
        self.assertIn("English Content", en.html_string)
        self.assertIn("English Heading", en.title)

        de = translations["de"]
        self.assertIn("German Content", de.html_string)
        self.assertIn("German Heading", de.title)

    def test_populate_translations(self):
        model = MockTranslatableModel(translatable_fields=["field1", "field2"])
        translations = {
            "en": {
                "field1": "english value 1",
                "field2": "english value 2"
            },
            "de": {
                "field1": "german value 1",
                "field2": "german value 2"
            }
        }
        TranslatableModelLoader.populate_translations(model, translations)
        self.assertEqual(model.field1, "english value 1")
        self.assertEqual(model.field2, "english value 2")
        with translation.override("de"):
            self.assertEqual(model.field1, "german value 1")
            self.assertEqual(model.field2, "german value 2")

    def test_mark_translation_availability_all_required_fields_present(self):
        model = MockTranslatableModel(translatable_fields=["title"])
        model.title = "english title"
        with translation.override("de"):
            model.title = "german title"
        with mock.patch('utils.language_utils.get_available_languages', return_value=["en", "de", "fr"]):
            TranslatableModelLoader.mark_translation_availability(model, required_fields=["title"])
        self.assertSetEqual(set(["en", "de"]), set(model.languages))

    def test_mark_translation_availability_required_field_missing(self):
        model = MockTranslatableModel(translatable_fields=["title", "content"])
        model.title = "english title"
        model.content = "english content"
        with translation.override("de"):
            model.title = "german title"

        with mock.patch('utils.language_utils.get_available_languages', return_value=["en", "de", "fr"]):
            TranslatableModelLoader.mark_translation_availability(model, required_fields=["title", "content"])
        self.assertSetEqual(set(["en"]), set(model.languages))

    def test_mark_translation_availability_required_fields_not_given(self):
        model = MockTranslatableModel(translatable_fields=["title", "content"])
        with mock.patch('utils.language_utils.get_available_languages', return_value=["en", "de", "fr"]):
            TranslatableModelLoader.mark_translation_availability(model)
        self.assertSetEqual(set(["en", "de", "fr"]), set(model.languages))

    def test_get_blank_translation_dictionary(self):
        with mock.patch('utils.language_utils.get_available_languages', return_value=["en", "de", "fr"]):
            translation_dict = TranslatableModelLoader.get_blank_translation_dictionary()
            self.assertSetEqual(set(["en", "de", "fr"]), set(translation_dict.keys()))
            self.assertDictEqual(translation_dict["en"], {})
            # Check to make sure it's not a dictionary of references to the same dictionary
            self.assertFalse(translation_dict["en"] is translation_dict["de"])
