"""Module for testing utilities for resource generators."""

import sys

from resources.utils.resource_parameters import (
    EnumResourceParameter,
    TextResourceParameter,
    IntegerResourceParameter,
    BoolResourceParameter,
)


def run_parameter_smoke_tests(generator, option_name):
    """Run generator.data for a range of test values for the given option.

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
        generator.options[option_name].value = value
        try:
            generator.data()  # Smoke test
        except Exception as e:
            raise Exception("Smoke test of option {} failed for value {}".format(option_name, value)) from e
