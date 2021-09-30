from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator


class ResourceModelTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()

    def test_resource_str(self):
        resource = self.test_data.create_resource(
            "bare",
            "Bare",
            "resources/bare.html",
            "BareResourceGenerator",
        )
        self.assertEqual(resource.__str__(), "Bare")

    def test_resource_model_name(self):
        resource = self.test_data.create_resource(
            "bare",
            "Bare",
            "resources/bare.html",
            "BareResourceGenerator",
        )
        self.assertEqual(resource.MODEL_NAME, "Printable")

    def test_resource_model_get_absolute_url(self):
        resource = self.test_data.create_resource(
            "bare",
            "Bare",
            "resources/bare.html",
            "BareResourceGenerator",
        )
        self.assertEqual(
            resource.get_absolute_url(),
            "/en/resources/bare/"
        )
