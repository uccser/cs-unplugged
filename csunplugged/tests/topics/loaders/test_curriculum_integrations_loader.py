from tests.BaseTestWithDB import BaseTestWithDB

from topics.models import CurriculumIntegration
from topics.management.commands._CurriculumIntegrationsLoader import CurriculumIntegrationsLoader


class CurriculumIntegrationsLoader(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.BASE_PATH = "tests/topics/loaders/assets/curriculum_integrations/"

    def test_basic_config(self):
        config_file = "basic_config.yaml"

        ci_loader = CurriculumIntegrationLoader(config_file, self.BASE_PATH)
        ci_loader.load()

        ci_objects = CurriculumIntegration.objects.all()

        self.assertQuerysetEqual(
            lo_objects,
            ['<CurriculumIntegration: cats>']
        )
