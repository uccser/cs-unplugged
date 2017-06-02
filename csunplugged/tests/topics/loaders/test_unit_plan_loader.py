import os.path
from unittest.mock import Mock

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import UnitPlan
from topics.management.commands._UnitPlanLoader import UnitPlanLoader


class UnitPlanLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "unit_plan"
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_basic_config(self):
        config_file = "unit-plan-1/unit-plan-1.yaml"
        factory = Mock()
        topic = self.test_data.create_topic('1')

        up_loader = UnitPlanLoader(factory, config_file, topic, self.BASE_PATH)
        up_loader.load()

        up_objects = UnitPlan.objects.all()

        self.assertQuerysetEqual(
            up_objects,
            ["<UnitPlan: Unit Plan 1>"]
        )
