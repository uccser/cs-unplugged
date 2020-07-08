"""Module for the testing custom Django commands."""

from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management
from django.test import tag


@tag("management")
class ManagementCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_updatedata_command(self):
        management.call_command("updatedata")

    def test_updatedata_command_lite_load(self):
        management.call_command("updatedata", lite_load=True)
