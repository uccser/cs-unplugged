"""Module for testing utilities for resource generators."""

import sys
from tests.BaseTest import BaseTest
from PIL.Image import Image

from resources.utils.resource_parameters import (
    EnumResourceParameter,
    TextResourceParameter,
    IntegerResourceParameter,
    BoolResourceParameter,
)

VALID_DATA_TYPES = {
    "html": str,
    "image": Image,
    "resource-number-hunt": list,
}


class BaseGeneratorTest(BaseTest):
    """Base class for generator tests."""

    def assert_data_valid(self, data):
        """Test that the result from a generator.data() call is valid."""
        # Check data result is valid
        self.assertIsInstance(data, (dict, list))
        if isinstance(data, dict):
            pages = [data]
        else:
            pages = data

        for page in pages:
            self.assertIsInstance(page, dict)
            self.assertIn("type", page)
            self.assertIn("data", page)
            data_type = page["type"]
            self.assertIn(data_type, VALID_DATA_TYPES)
            self.assertIsInstance(page["data"], VALID_DATA_TYPES[data_type])
            if "thumbnail" in page:
                self.assertIs(page["thumbnail"], True)

    def run_parameter_smoke_tests(self, generator, option_name):
        """Test generator.data for a range of test values for the given option.

        The values run depend on the option type:
            EnumResourceParameter: All valid values
            TextResourceParameter: Empty string, and non-empty string
            IntegerResourceParameter: min and maximum values, or very large
                positive/negative numbers if range bounds not given
            BoolResourceParameter: True and false
        """
        option = generator.options[option_name]
        if isinstance(option, EnumResourceParameter):
            test_values = option.valid_values
        elif isinstance(option, TextResourceParameter):
            test_values = ["", "test value"]
        elif isinstance(option, IntegerResourceParameter):
            test_values = [
                option.min_val or -sys.maxsize,
                option.max_val or sys.maxsize
            ]
        elif isinstance(option, BoolResourceParameter):
            test_values = [True, False]
        for value in test_values:
            option = generator.options[option_name]
            option.value = option.process_value(value)
            try:
                data = generator.data()  # Smoke test
            except Exception as e:
                raise Exception("Smoke test of option {} failed for value {}".format(option_name, value)) from e
            self.assert_data_valid(data)
