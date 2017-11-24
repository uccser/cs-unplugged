"""Test class for QueryParameterMissingError error."""

from django.test import SimpleTestCase
from utils.errors.QueryParameterMultipleValuesError import QueryParameterMultipleValuesError


class QueryParameterMultipleValuesErrorTest(SimpleTestCase):
    """Test class for QueryParameterMissingError error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used.
    """

    def test_attributes(self):
        exception = QueryParameterMultipleValuesError("parameter", ["value1", "value2"])
        self.assertEqual(exception.parameter, "parameter")
        self.assertEqual(exception.values, ["value1", "value2"])

    def test_string(self):
        exception = QueryParameterMultipleValuesError("parameter", ["value1", "value2"])
        self.assertEqual(
            exception.__str__(),
            "Parameter 'parameter' must only have one value, but multiple were given (['value1', 'value2'])."
        )
