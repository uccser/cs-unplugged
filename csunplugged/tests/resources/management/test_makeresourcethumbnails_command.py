"""Module for the testing custom Django resource commands."""

from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management
from django.test import tag
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator


@tag("management")
class MakeResourceThumnbailsCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"
        self.THUMBNAIL_PATH = "build/img/resources/{}/thumbnails/{}"

    def test_makeresourcethumbnails_command_single_resource(self):
        self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        # TODO: Fix these tests, they shouldn't be writing files into the build directory
        management.call_command("makeresourcethumbnails")
        open(self.THUMBNAIL_PATH.format("resource-grid", "resource-grid-paper_size-a4.png"))
        open(self.THUMBNAIL_PATH.format("resource-grid", "resource-grid-paper_size-letter.png"))


    def test_makeresourcethumbnails_command_multiple_resources(self):
        self.test_data.create_resource(
            "grid",
            "Grid",
            "resources/grid.html",
            "GridResourceGenerator",
        )
        self.test_data.create_resource(
            "arrows",
            "Arrows",
            "resources/arrows.html",
            "ArrowsResourceGenerator",
        )
        # TODO: Fix these tests, they shouldn't be writing files into the build directory
        management.call_command("makeresourcethumbnails")
        open(self.THUMBNAIL_PATH.format("resource-grid", "resource-grid-paper_size-a4.png"))
        open(self.THUMBNAIL_PATH.format("resource-grid", "resource-grid-paper_size-letter.png"))
        open(self.THUMBNAIL_PATH.format("resource-arrows", "resource-arrows-paper_size-a4.png"))
        open(self.THUMBNAIL_PATH.format("resource-arrows", "resource-arrows-paper_size-letter.png"))
