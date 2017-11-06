from http import HTTPStatus
from django.test import tag
from django.urls import reverse
from tests.BaseTestWithDB import BaseTestWithDB
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from resources.utils.get_resource_generator import get_resource_generator
from resources.utils.resource_valid_test_configurations import resource_valid_test_configurations
from utils.create_query_string import query_string


@tag("resource")
class PixelPainterResourceViewTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"

    def test_grid_resource_form_view(self):
        resource = self.test_data.create_resource(
            "pixel-painter",
            "Pixel Painter",
            "resources/pixel-painter.html",
            "PixelPainterResourceGenerator",
        )
        kwargs = {
            "resource_slug": resource.slug,
        }
        url = reverse("resources:resource", kwargs=kwargs)
        response = self.client.get(url)
        self.assertEqual(HTTPStatus.OK, response.status_code)
