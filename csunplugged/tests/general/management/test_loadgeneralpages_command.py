"""Module for the testing custom Django loadgeneralpages commands."""

from unittest import mock
from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management
from django.test import tag


@tag("management")
class LoadGeneralPagesCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    @mock.patch(
        "general.management.commands._GeneralPagesLoader.GeneralPagesLoader.load",
        return_value=True
    )
    def test_loadgeneralpages_command(self, general_pages_loader):
        management.call_command("loadgeneralpages")
        self.assertTrue(general_pages_loader.called)
