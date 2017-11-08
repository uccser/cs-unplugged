import os.path
from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator
from topics.models import CurriculumIntegration
from topics.management.commands._CurriculumIntegrationsLoader import CurriculumIntegrationsLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError


class CurriculumIntegrationsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "curriculum_integrations"

    def test_basic_config(self):
        config_file = os.path.join(self.loader_name, "basic-config.yaml")

        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")

        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        ci_loader.load()

        ci_objects = CurriculumIntegration.objects.all()

        self.assertQuerysetEqual(
            ci_objects,
            ["<CurriculumIntegration: Integration 1>"]
        )

    def test_missing_number(self):
        config_file = os.path.join(self.loader_name, "missing-number.yaml")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )

    def test_missing_areas(self):
        config_file = os.path.join(self.loader_name, "missing-areas.yaml")
        topic = self.test_data.create_topic("1")
        ci_loader = CurriculumIntegrationsLoader(config_file, topic, self.test_data.LOADER_ASSET_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            ci_loader.load
        )
