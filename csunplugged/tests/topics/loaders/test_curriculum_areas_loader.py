from tests.BaseTestWithDB import BaseTestWithDB

from topics.models import CurriculumArea
from topics.management.commands._CurriculumAreasLoader import CurriculumAreasLoader


class CurriculumAreasLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.BASE_PATH = "tests/topics/loaders/assets/curriculum_areas/"

    def test_basic_config(self):
        config_file = "basic_config.yaml"

        ca_loader = CurriculumAreasLoader(config_file, self.BASE_PATH)
        ca_loader.load()

        ca_objects = CurriculumArea.objects.all()

        self.assertQuerysetEqual(
            ca_objects,
            ['<CurriculumArea: Elephants>']
        )
