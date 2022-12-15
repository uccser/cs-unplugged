import os.path
from django.utils import translation
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from utils.errors.InvalidYAMLValueError import InvalidYAMLValueError
from topics.models import ClassroomResource
from topics.management.commands._ClassroomResourcesLoader import ClassroomResourcesLoader


class ClassroomResourcesLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "classroom_resources"
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        config_file = "basic-config.yaml"

        cr_loader = ClassroomResourcesLoader(structure_filename=config_file, base_path=self.base_path)
        cr_loader.load()

        cr_objects = ClassroomResource.objects.all()

        self.assertEqual(2, len(cr_objects))
        cr_1 = ClassroomResource.objects.get(slug="resource-1")
        cr_2 = ClassroomResource.objects.get(slug="resource-2")

        self.assertEqual("Description of resource 1", cr_1.description)
        self.assertEqual("Description of resource 2", cr_2.description)

    def test_missing_description(self):
        config_file = "missing-description.yaml"
        cr_loader = ClassroomResourcesLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(InvalidYAMLValueError, cr_loader.load)

    def test_translation(self):
        config_file = "translation.yaml"

        cr_loader = ClassroomResourcesLoader(structure_filename=config_file, base_path=self.base_path)
        cr_loader.load()

        translated = ClassroomResource.objects.get(slug="translated")
        self.assertSetEqual(set(["en", "de"]), set(translated.languages))

        self.assertEqual("English Description 1", translated.description)
        with translation.override("de"):
            self.assertEqual("German Description 1", translated.description)

    def test_missing_translation(self):
        config_file = "translation.yaml"

        cr_loader = ClassroomResourcesLoader(structure_filename=config_file, base_path=self.base_path)
        cr_loader.load()

        untranslated = ClassroomResource.objects.get(slug="untranslated")
        self.assertSetEqual(set(["en"]), set(untranslated.languages))

        self.assertEqual("English Description 2", untranslated.description)

        # Check description does not fall back to english for missing translation
        with translation.override("de"):
            self.assertEqual("", untranslated.description)

    def test_insert_middle(self):
        config_file = "basic-config.yaml"

        cr_loader = ClassroomResourcesLoader(structure_filename=config_file, base_path=self.base_path)
        cr_loader.load()

        cr_objects = ClassroomResource.objects.all()
        self.assertQuerysetEqual(
            list(cr_objects),
            [
                '<ClassroomResource: Description of resource 1>',
                '<ClassroomResource: Description of resource 2>'
            ],
        )

        self.assertEqual(2, len(cr_objects))

        config_file = "insert-middle.yaml"

        cr_loader = ClassroomResourcesLoader(structure_filename=config_file, base_path=self.base_path)
        cr_loader.load()

        cr_objects = ClassroomResource.objects.all()

        self.assertEqual(3, len(cr_objects))
        self.assertQuerysetEqual(
            list(cr_objects),
            [
                '<ClassroomResource: Description of resource 1>',
                '<ClassroomResource: Description of resource 3>',
                '<ClassroomResource: Description of resource 2>'
            ],
        )

    def test_delete_end(self):
        config_file = "basic-config.yaml"

        cr_loader = ClassroomResourcesLoader(structure_filename=config_file, base_path=self.base_path)
        cr_loader.load()

        cr_objects = ClassroomResource.objects.all()
        self.assertQuerysetEqual(
            list(cr_objects),
            [
                '<ClassroomResource: Description of resource 1>',
                '<ClassroomResource: Description of resource 2>'
            ],
        )

        self.assertEqual(2, len(cr_objects))

        config_file = "delete-end.yaml"

        cr_loader = ClassroomResourcesLoader(structure_filename=config_file, base_path=self.base_path)
        cr_loader.load()

        cr_objects = ClassroomResource.objects.all()

        self.assertEqual(1, len(cr_objects))
        self.assertQuerysetEqual(
            list(cr_objects),
            [
                '<ClassroomResource: Description of resource 1>',
            ],
        )
