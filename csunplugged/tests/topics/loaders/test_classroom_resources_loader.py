import os.path

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from utils.errors.InvalidConfigValueError import InvalidConfigValueError

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
        self.assertRaises(InvalidConfigValueError, cr_loader.load)
