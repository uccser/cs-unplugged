import os.path

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import AgeRange
from topics.management.commands._AgeRangesLoader import AgeRangesLoader

from utils.errors.CouldNotFindConfigFileError import CouldNotFindConfigFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.EmptyConfigFileError import EmptyConfigFileError


class AgeRangesLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "age_ranges"
        self.BASE_PATH = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_age_ranges_loader_basic_config(self):
        config_file = "basic-config.yaml"
        range_loader = AgeRangesLoader(config_file, self.BASE_PATH)
        range_loader.load()
        self.assertQuerysetEqual(
            AgeRange.objects.all(),
            ["<AgeRange: NumericRange(8, 10, '[)')>"]
        )

    def test_age_ranges_loader_missing_configuration_file(self):
        config_file = "missing.yaml"
        range_loader = AgeRangesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            CouldNotFindConfigFileError,
            range_loader.load,
        )

    def test_age_ranges_loader_empty_configuration_file(self):
        config_file = "empty.yaml"
        range_loader = AgeRangesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            EmptyConfigFileError,
            range_loader.load,
        )

    def test_age_ranges_loader_correct_slug_value(self):
        config_file = "basic-config.yaml"
        range_loader = AgeRangesLoader(config_file, self.BASE_PATH)
        range_loader.load()
        self.assertEquals(
            AgeRange.objects.get(slug="8-10").slug,
            "8-10",
        )

    def test_age_ranges_loader_correct_min_age_value(self):
        config_file = "basic-config.yaml"
        range_loader = AgeRangesLoader(config_file, self.BASE_PATH)
        range_loader.load()
        self.assertEquals(
            AgeRange.objects.get(slug="8-10").ages.lower,
            8,
        )

    def test_age_ranges_loader_missing_min_age_value(self):
        config_file = "missing-min-age.yaml"
        range_loader = AgeRangesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            range_loader.load,
        )

    def test_age_ranges_loader_correct_max_age_value(self):
        config_file = "basic-config.yaml"
        range_loader = AgeRangesLoader(config_file, self.BASE_PATH)
        range_loader.load()
        self.assertEquals(
            AgeRange.objects.get(slug="8-10").ages.upper,
            10,
        )

    def test_age_ranges_loader_missing_max_age_value(self):
        config_file = "missing-max-age.yaml"
        range_loader = AgeRangesLoader(config_file, self.BASE_PATH)
        self.assertRaises(
            MissingRequiredFieldError,
            range_loader.load,
        )

    def test_age_ranges_loader_correct_description_value(self):
        config_file = "description.yaml"
        range_loader = AgeRangesLoader(config_file, self.BASE_PATH)
        range_loader.load()
        self.assertEquals(
            AgeRange.objects.get(slug="5-7").description,
            "Sample description.",
        )

    def test_age_ranges_loader_missing_description_value(self):
        config_file = "basic-config.yaml"
        range_loader = AgeRangesLoader(config_file, self.BASE_PATH)
        range_loader.load()
        self.assertIsNone(AgeRange.objects.get(slug="8-10").description)

    def test_age_ranges_loader_multiple_configuration(self):
        config_file = "multiple.yaml"
        range_loader = AgeRangesLoader(config_file, self.BASE_PATH)
        range_loader.load()
        self.assertQuerysetEqual(
            AgeRange.objects.order_by("ages"),
            [
                "<AgeRange: NumericRange(5, 7, '[)')>",
                "<AgeRange: NumericRange(8, 10, '[)')>",
                "<AgeRange: NumericRange(11, 14, '[)')>",
            ]
        )
