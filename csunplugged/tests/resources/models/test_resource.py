from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator


class ResourceModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()

    def test_resource_str(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        self.assertEqual(resource.__str__(), "Grid")

    def test_resource_model_name(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        self.assertEqual(resource.MODEL_NAME, "Printable")

    def test_resource_model_get_absolute_url(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        self.assertEqual(
            resource.get_absolute_url(),
            "/en/resources/grid/"
        )
