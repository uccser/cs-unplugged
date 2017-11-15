"""Test class for QueryParameterMissingError error."""

from django.test import SimpleTestCase
from utils.errors.QueryParameterMissingError import QueryParameterMissingError


class QueryParameterMissingErrorTest(SimpleTestCase):
    """Test class for QueryParameterMissingError error.

    Note: Tests to check if these were raised appropriately
          are located where this exception is used.
    """

    def test_attributes(self):
        exception = QueryParameterMissingError("parameter")
        self.assertEqual(exception.parameter, "parameter")

    def test_string(self):
        exception = QueryParameterMissingError("parameter")
        self.assertEqual(
            exception.__str__(),
            "Parameter 'parameter' not specified."
        )
