"""Test class for QueryParameterInvalidError error."""

from django.test import SimpleTestCase
from utils.errors.QueryParameterInvalidError import QueryParameterInvalidError


class QueryParameterInvalidErrorTest(SimpleTestCase):
    """Test class for QueryParameterInvalidError error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used.
    """

    def test_attributes(self):
        exception = QueryParameterInvalidError("parameter", "value")
        self.assertEqual(exception.parameter, "parameter")
        self.assertEqual(exception.value, "value")

    def test_string(self):
        exception = QueryParameterInvalidError("parameter", "value")
        self.assertEqual(
            exception.__str__(),
            "Value 'value' for parameter 'parameter' is not valid."
        )
