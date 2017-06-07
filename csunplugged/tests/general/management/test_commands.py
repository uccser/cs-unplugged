"""Module for the testing custom Django commands."""

from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management


class ManagementCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_commands(self):
        management.call_command("updatedata")
