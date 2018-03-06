"""Module for the testing custom Django loadclassicpages commands."""

from unittest import mock
from tests.BaseTestWithDB import BaseTestWithDB
from django.core import management
from django.test import tag


@tag("management")
class LoadClassicPagesCommandTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    @mock.patch(
        "classic.management.commands._ClassicPagesLoader.ClassicPagesLoader.load",
        return_value=True
    )
    def test_loadclassicpages_command(self, classic_pages_loader):
        management.call_command("loadclassicpages")
        self.assertTrue(classic_pages_loader.called)
