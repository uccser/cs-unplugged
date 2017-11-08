"""Test class for BaseLoader class."""

from django.test import SimpleTestCase
from tests.utils.BareBaseLoader import BareBaseLoader
from utils.errors.InvalidConfigFileError import InvalidConfigFileError
import os.path

TEST_ASSET_PATH = "tests/utils/assets/"


class BaseLoaderTest(SimpleTestCase):
    """Test class for BaseLoader class."""

    def test_load_yaml_file_valid(self):
        loader = BareBaseLoader()
        filename = "yaml-valid.yaml"
        self.assertEqual(
            loader.load_yaml_file(os.path.join(TEST_ASSET_PATH, filename)),
            {"key": "value"}
        )

    def test_load_yaml_file_invalid(self):
        loader = BareBaseLoader()
        filename = "yaml-invalid.yaml"
        self.assertRaises(
            InvalidConfigFileError,
            loader.load_yaml_file,
            os.path.join(TEST_ASSET_PATH, filename)
        )

    def test_load_yaml_file_invalid_not_dict(self):
        loader = BareBaseLoader()
        filename = "yaml-invalid-not-dict.yaml"
        self.assertRaises(
            InvalidConfigFileError,
            loader.load_yaml_file,
            os.path.join(TEST_ASSET_PATH, filename)
        )
