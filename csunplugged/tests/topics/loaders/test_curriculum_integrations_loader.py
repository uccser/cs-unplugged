from unittest.mock import Mock

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics import create_topics_test_data as test_data

from topics.models import CurriculumIntegration
from topics.management.commands._CurriculumIntegrationsLoader import CurriculumIntegrationsLoader


class CurriculumIntegrationsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_log = Mock()
        self.BASE_PATH = "tests/topics/loaders/assets/curriculum_integrations/"

    def test_basic_config(self):
        config_file = "basic_config.yaml"

        test_data.create_test_curriculum_area('1')
        topic = test_data.create_test_topic('1')

        ci_loader = CurriculumIntegrationsLoader(self.load_log, config_file, topic, self.BASE_PATH)
        ci_loader.load()

        ci_objects = CurriculumIntegration.objects.all()

        self.assertQuerysetEqual(
            ci_objects,
            ['<CurriculumIntegration: Area 51>']
        )
