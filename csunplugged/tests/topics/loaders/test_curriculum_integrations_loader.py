import os.path

from django.utils import translation

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import CurriculumIntegration
from topics.management.commands._CurriculumIntegrationsLoader import CurriculumIntegrationsLoader


class CurriculumIntegrationsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, "curriculum_integrations")

    def test_basic_config(self):
        config_file = "basic-config.yaml"

        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")

        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        ci_loader.load()

        ci_objects = CurriculumIntegration.objects.all()

        self.assertEqual(1, len(ci_objects))

        ci = ci_objects[0]
        self.assertSetEqual(set(["en"]), set(ci.languages))
        self.assertEqual("English Heading", ci.name)
        self.assertIn("English curriculum integration content", ci.content)

    def test_translation(self):
        config_file = "translation.yaml"

        self.test_data.create_curriculum_area("1")
        topic = self.test_data.create_topic("1")

        ci_loader = CurriculumIntegrationsLoader(topic, base_path=self.base_path, structure_filename=config_file)
        ci_loader.load()

        ci_objects = CurriculumIntegration.objects.all()

        self.assertEqual(1, len(ci_objects))

        ci = ci_objects[0]
        self.assertSetEqual(set(["en", "de"]), set(ci.languages))

        self.assertEqual("English Heading", ci.name)
        self.assertIn("English curriculum integration content", ci.content)

        with translation.override("de"):
            self.assertEqual("German Heading", ci.name)
            self.assertIn("German curriculum integration content", ci.content)
