"""Module for the testing custom Django commands."""

from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management


class ManagementCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_updatedata_command(self):
        management.call_command("updatedata")

    def test_makeresources_command(self):
        management.call_command("makeresources")
