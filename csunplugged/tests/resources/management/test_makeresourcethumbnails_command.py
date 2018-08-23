"""Module for the testing custom Django resource commands."""

from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management
from django.test import tag, override_settings
from tests.resources.ResourcesTestDataGenerator import ResourcesTestDataGenerator


@tag("management")
@override_settings(RESOURCE_GENERATORS_PACKAGE="tests.resources.management.test_generators")
class MakeResourceThumnbailsCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = ResourcesTestDataGenerator()
        self.language = "en"
        self.THUMBNAIL_PATH = "build/img/resources/{}/thumbnails/{}/{}"

    def test_makeresourcethumbnails_command_single_resource(self):
        self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGenerator",
        )
        # TODO: Fix these tests, they shouldn't be writing files into the build directory
        management.call_command("makeresourcethumbnails")
        open(self.THUMBNAIL_PATH.format("resource1", self.language, "resource1-paper_size-a4.png"))
        open(self.THUMBNAIL_PATH.format("resource1", self.language, "resource1-paper_size-letter.png"))

    def test_makeresourcethumbnails_command_multiple_resources(self):
        self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGenerator",
        )
        self.test_data.create_resource(
            "resource2",
            "Resource 2",
            "Description of resource 2",
            "BareResourceGenerator",
        )
        # TODO: Fix these tests, they shouldn't be writing files into the build directory
        management.call_command("makeresourcethumbnails")
        open(self.THUMBNAIL_PATH.format("resource1", self.language, "resource1-paper_size-a4.png"))
        open(self.THUMBNAIL_PATH.format("resource1", self.language, "resource1-paper_size-letter.png"))
        open(self.THUMBNAIL_PATH.format("resource2", self.language, "resource2-paper_size-a4.png"))
        open(self.THUMBNAIL_PATH.format("resource2", self.language, "resource2-paper_size-letter.png"))

    def test_makeresourcethumbnails_command_resource_generator_has_non_enum_options(self):
        self.test_data.create_resource(
            "resource1",
            "Resource 1",
            "Description of resource 1",
            "BareResourceGeneratorWithNonEnumerableOptions",
        )
        with self.assertRaises(TypeError):
            management.call_command("makeresourcethumbnails")
