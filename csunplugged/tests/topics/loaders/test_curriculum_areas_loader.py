import os.path

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TestDataGenerator import TestDataGenerator

from topics.models import CurriculumArea
from topics.management.commands._CurriculumAreasLoader import CurriculumAreasLoader


class CurriculumAreasLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TestDataGenerator()
        self.loader_name = "curriculum_areas"
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        config_file = "basic-config.yaml"

        ca_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        ca_loader.load()

        ca_objects = CurriculumArea.objects.all()

        self.assertQuerysetEqual(
            ca_objects,
            ["<CurriculumArea: Elephants>"]
        )
