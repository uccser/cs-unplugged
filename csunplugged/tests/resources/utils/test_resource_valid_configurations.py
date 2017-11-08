from django.test import tag
from django.test import SimpleTestCase
from resources.utils.resource_valid_configurations import resource_valid_configurations


@tag("resource")
class ResourceValidConfigurationsTest(SimpleTestCase):

    def test_dictionary_one_key_one_value(self):
        options = {
            "key1": ["value1"]
        }
        self.assertEqual(
            resource_valid_configurations(options),
            [
                {"header_text": "", "key1": "value1"},
                {"header_text": "Example header", "key1": "value1"},
            ]
        )

    def test_dictionary_one_key_two_values(self):
        options = {
            "key1": ["value1", "value2"]
        }
        self.assertEqual(
            resource_valid_configurations(options),
            [
                {"header_text": "", "key1": "value1"},
                {"header_text": "", "key1": "value2"},
                {"header_text": "Example header", "key1": "value1"},
                {"header_text": "Example header", "key1": "value2"},
            ]
        )

    def test_dictionary_two_keys_two_values(self):
        options = {
            "key1": ["value1"],
            "key2": ["value5"]
        }
        self.assertEqual(
            resource_valid_configurations(options),
            [
                {"header_text": "", "key1": "value1", "key2": "value5"},
                {"header_text": "Example header", "key1": "value1", "key2": "value5"},
            ]
        )

    def test_dictionary_two_keys_three_values(self):
        options = {
            "key1": ["value1", "value2"],
            "key2": ["value5"],
        }
        self.assertEqual(
            resource_valid_configurations(options),
            [
                {"header_text": "", "key1": "value1", "key2": "value5"},
                {"header_text": "", "key1": "value2", "key2": "value5"},
                {"header_text": "Example header", "key1": "value1", "key2": "value5"},
                {"header_text": "Example header", "key1": "value2", "key2": "value5"},
            ]
        )

    def test_dictionary_three_keys_many_values(self):
        options = {
            "key1": ["value1", "value2"],
            "key2": ["value5", "value6", "value7"],
            "key3": [True, False],
        }
        self.assertEqual(
            resource_valid_configurations(options),
            [
                {"header_text": "", "key1": "value1", "key2": "value5", "key3": "yes"},
                {"header_text": "", "key1": "value1", "key2": "value5", "key3": "no"},
                {"header_text": "", "key1": "value1", "key2": "value6", "key3": "yes"},
                {"header_text": "", "key1": "value1", "key2": "value6", "key3": "no"},
                {"header_text": "", "key1": "value1", "key2": "value7", "key3": "yes"},
                {"header_text": "", "key1": "value1", "key2": "value7", "key3": "no"},
                {"header_text": "", "key1": "value2", "key2": "value5", "key3": "yes"},
                {"header_text": "", "key1": "value2", "key2": "value5", "key3": "no"},
                {"header_text": "", "key1": "value2", "key2": "value6", "key3": "yes"},
                {"header_text": "", "key1": "value2", "key2": "value6", "key3": "no"},
                {"header_text": "", "key1": "value2", "key2": "value7", "key3": "yes"},
                {"header_text": "", "key1": "value2", "key2": "value7", "key3": "no"},
                {"header_text": "Example header", "key1": "value1", "key2": "value5", "key3": "yes"},
                {"header_text": "Example header", "key1": "value1", "key2": "value5", "key3": "no"},
                {"header_text": "Example header", "key1": "value1", "key2": "value6", "key3": "yes"},
                {"header_text": "Example header", "key1": "value1", "key2": "value6", "key3": "no"},
                {"header_text": "Example header", "key1": "value1", "key2": "value7", "key3": "yes"},
                {"header_text": "Example header", "key1": "value1", "key2": "value7", "key3": "no"},
                {"header_text": "Example header", "key1": "value2", "key2": "value5", "key3": "yes"},
                {"header_text": "Example header", "key1": "value2", "key2": "value5", "key3": "no"},
                {"header_text": "Example header", "key1": "value2", "key2": "value6", "key3": "yes"},
                {"header_text": "Example header", "key1": "value2", "key2": "value6", "key3": "no"},
                {"header_text": "Example header", "key1": "value2", "key2": "value7", "key3": "yes"},
                {"header_text": "Example header", "key1": "value2", "key2": "value7", "key3": "no"},
            ]
        )

    def test_dictionary_one_key_one_value_no_header_text(self):
        options = {
            "key1": ["value1"]
        }
        self.assertEqual(
            resource_valid_configurations(options, header_text=False),
            [
                {"key1": "value1"}
            ]
        )

    def test_dictionary_one_key_two_values_no_header_text(self):
        options = {
            "key1": ["value1", "value2"]
        }
        self.assertEqual(
            resource_valid_configurations(options, header_text=False),
            [
                {"key1": "value1"},
                {"key1": "value2"}
            ]
        )

    def test_dictionary_two_keys_two_values_no_header_text(self):
        options = {
            "key1": ["value1"],
            "key2": ["value5"]
        }
        self.assertEqual(
            resource_valid_configurations(options, header_text=False),
            [
                {"key1": "value1", "key2": "value5"}
            ]
        )

    def test_dictionary_two_keys_three_values_no_header_text(self):
        options = {
            "key1": ["value1", "value2"],
            "key2": ["value5"],
        }
        self.assertEqual(
            resource_valid_configurations(options, header_text=False),
            [
                {"key1": "value1", "key2": "value5"},
                {"key1": "value2", "key2": "value5"}
            ]
        )

    def test_dictionary_three_keys_many_values_no_header_text(self):
        options = {
            "key1": ["value1", "value2"],
            "key2": ["value5", "value6", "value7"],
            "key3": [True, False],
        }
        self.assertEqual(
            resource_valid_configurations(options, header_text=False),
            [
                {"key1": "value1", "key2": "value5", "key3": "yes"},
                {"key1": "value1", "key2": "value5", "key3": "no"},
                {"key1": "value1", "key2": "value6", "key3": "yes"},
                {"key1": "value1", "key2": "value6", "key3": "no"},
                {"key1": "value1", "key2": "value7", "key3": "yes"},
                {"key1": "value1", "key2": "value7", "key3": "no"},
                {"key1": "value2", "key2": "value5", "key3": "yes"},
                {"key1": "value2", "key2": "value5", "key3": "no"},
                {"key1": "value2", "key2": "value6", "key3": "yes"},
                {"key1": "value2", "key2": "value6", "key3": "no"},
                {"key1": "value2", "key2": "value7", "key3": "yes"},
                {"key1": "value2", "key2": "value7", "key3": "no"},
            ]
        )

    def test_dictionary_alphabetical_keys(self):
        options = {
            "a": ["a"],
            "b": ["b"],
            "c": ["c"],
            "d": ["d"]
        }
        self.assertEqual(
            resource_valid_configurations(options, header_text=False),
            [
                {"a": "a", "b": "b", "c": "c", "d": "d"}
            ]
        )
