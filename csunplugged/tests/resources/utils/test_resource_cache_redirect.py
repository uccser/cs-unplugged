from tests.BaseTestWithDB import BaseTestWithDB
from django.test import tag
from django.http import QueryDict
from resources.utils.resource_pdf_cache import resource_pdf_cache
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator
from resources.utils.get_resource_generator import get_resource_generator
from http import HTTPStatus


@tag("resource")
class CacheRedirectTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()

    def test_resources_cache_valid_resource(self):
        resource = self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        query = QueryDict("paper_size=a4")
        generator = get_resource_generator(resource.generator_module, query)
        response = resource_pdf_cache(resource, generator)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(
            response.url,
            "/static/resources/en/grid/Grid%20(a4).pdf"
        )
