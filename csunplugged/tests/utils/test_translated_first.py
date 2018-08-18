"""Test class for translated_first module."""

from tests.BaseTestWithDB import BaseTestWithDB
from utils.translated_first import translated_first
from tests.utils.translatable_model.models import MockTranslatableModel


class TranslatedFirstTest(BaseTestWithDB):
    """Test class for translated_first module."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_valid_type(self):
        item1 = MockTranslatableModel()
        item1.languages = ["en", "de"]
        item1.save()
        translated_first(MockTranslatableModel.objects.all())

    def test_invalid_type(self):
        self.assertRaises(TypeError, translated_first, [1, 2, 3])

    def test_translated_type(self):
        item1 = MockTranslatableModel()
        item1.languages = ["en"]
        item1.save()
        item2 = MockTranslatableModel()
        item2.languages = ["en"]
        item2.save()
        self.assertEquals(
            translated_first(MockTranslatableModel.objects.all()),
            [item1, item2]
        )

    def test_untranslated_type(self):
        item1 = MockTranslatableModel()
        item1.languages = ["de"]
        item1.save()
        item2 = MockTranslatableModel()
        item2.languages = ["de"]
        item2.save()
        self.assertEquals(
            translated_first(MockTranslatableModel.objects.all()),
            [item1, item2]
        )

    def test_maintain_order(self):
        item1 = MockTranslatableModel(name="z")
        item1.languages = ["en"]
        item1.save()
        item2 = MockTranslatableModel(name="a")
        item2.languages = ["en"]
        item2.save()
        self.assertEquals(
            translated_first(MockTranslatableModel.objects.order_by("name")),
            [item2, item1]
        )

    def test_translated_moved_first(self):
        item1 = MockTranslatableModel()
        item1.languages = ["de"]
        item1.save()
        item2 = MockTranslatableModel()
        item2.languages = ["en"]
        item2.save()
        self.assertEquals(
            translated_first(MockTranslatableModel.objects.all()),
            [item2, item1]
        )

    def test_translated_moved_first_with_ordering(self):
        item1 = MockTranslatableModel(name="z")
        item1.languages = ["de"]
        item1.save()
        item2 = MockTranslatableModel(name="a")
        item2.languages = ["en"]
        item2.save()
        item3 = MockTranslatableModel(name="j")
        item3.languages = ["es"]
        item3.save()
        self.assertEquals(
            translated_first(MockTranslatableModel.objects.order_by("name")),
            [item2, item3, item1]
        )
