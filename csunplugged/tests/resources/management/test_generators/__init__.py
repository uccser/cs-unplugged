"""Test generators package for management commands tests."""

# Disable unused import warnings for this file
# flake8: noqa: F401

from tests.resources.BareResourceGenerator import (
    BareResourceGenerator,
    BareResourceGeneratorMultiPage,
    BareResourceGeneratorWithCopies,
)
from resources.utils.resource_parameters import TextResourceParameter

class BareResourceGeneratorWithNonEnumerableOptions(BareResourceGenerator):
    """Class to simulate a resource generator with options that can't be enumerated."""

    def get_additional_options(self):
        """Add option that is not an EnumResourceParameter."""
        return {
            "header_text": TextResourceParameter(
                name="header_text",
                description="Header Text",
                placeholder="Example School: Room Four",
                required=False
            ),
        }
