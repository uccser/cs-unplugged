from django.test import tag, override_settings
from django.utils import translation
from tests.BaseTestWithDB import BaseTestWithDB
from resources.utils.get_thumbnail import (
    get_thumbnail_filename,
    get_thumbnail_base,
    get_thumbnail_static_path_for_resource,
)
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator


@tag("resource")
class GetThumbnailTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()

    def test_thumbnail_filename(self):
        options = {
            "a": "b",
            "c_d": "e_f",
        }
        self.assertEqual(
            get_thumbnail_filename("resource", options),
            "resource-a-b-c_d-e_f.png"
        )

    def test_thumbnail_filename_no_slug(self):
        options = {
            "a": "b",
        }
        self.assertEqual(
            get_thumbnail_filename("", options),
            "-a-b.png"
        )

    def test_thumbnail_filename_no_options(self):
        self.assertEqual(
            get_thumbnail_filename("resource", {}),
            "resource.png"
        )

    def test_thumbnail_filename_option_boolean_true(self):
        options = {
            "a": True,
        }
        self.assertEqual(
            get_thumbnail_filename("resource", options),
            "resource-a-yes.png"
        )

    def test_thumbnail_filename_option_boolean_false(self):
        options = {
            "a": False,
        }
        self.assertEqual(
            get_thumbnail_filename("resource", options),
            "resource-a-no.png"
        )

    def test_get_thumbnail_base_local_development(self):
        self.assertEqual(
            get_thumbnail_base("resource"),
            "/static/img/resources/resource/thumbnails/en/"
        )

    @override_settings(DEPLOYED=True)
    @override_settings(STATIC_URL="https://static.csunplugged.org/")
    def test_get_thumbnail_base_production_en(self):
        self.assertEqual(
            get_thumbnail_base("resource"),
            "https://static.csunplugged.org/img/resources/resource/thumbnails/en/"
        )

    @override_settings(DEPLOYED=True)
    @override_settings(STATIC_URL="https://static.csunplugged.org/")
    def test_get_thumbnail_base_production_de(self):
        with translation.override("de"):
            self.assertEqual(
                get_thumbnail_base("resource"),
                "https://static.csunplugged.org/img/resources/resource/thumbnails/de/"
            )

    def test_get_thumbnail_static_path_for_resource_local_development(self):
        resource = self.test_data.create_resource(
            "resource",
            "Resource",
            "Description of resource",
            "GridResourceGenerator",
        )
        self.assertEqual(
            get_thumbnail_static_path_for_resource(resource),
            "/static/img/resources/resource/thumbnails/en/resource-paper_size-a4.png"
        )

    @override_settings(DEPLOYED=True)
    @override_settings(STATIC_URL="https://static.csunplugged.org/")
    def test_get_thumbnail_static_path_for_resource_production_en(self):
        resource = self.test_data.create_resource(
            "resource",
            "Resource",
            "Description of resource",
            "GridResourceGenerator",
        )
        self.assertEqual(
            get_thumbnail_static_path_for_resource(resource),
            "https://static.csunplugged.org/img/resources/resource/thumbnails/en/resource-paper_size-a4.png"
        )

    @override_settings(DEPLOYED=True)
    @override_settings(STATIC_URL="https://static.csunplugged.org/")
    def test_get_thumbnail_static_path_for_resource_production_de(self):
        with translation.override("de"):
            resource = self.test_data.create_resource(
                "resource",
                "Resource",
                "Description of resource",
                "GridResourceGenerator",
            )
            self.assertEqual(
                get_thumbnail_static_path_for_resource(resource),
                "https://static.csunplugged.org/img/resources/resource/thumbnails/de/resource-paper_size-a4.png"
            )
