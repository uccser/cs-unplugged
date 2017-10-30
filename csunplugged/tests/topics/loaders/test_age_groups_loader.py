import os.path

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import AgeGroup
from topics.management.commands._AgeGroupsLoader import AgeGroupsLoader

from utils.errors.CouldNotFindConfigFileError import CouldNotFindConfigFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.EmptyConfigFileError import EmptyConfigFileError


class AgeGroupsLoaderTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_data = TopicsTestDataGenerator()
        self.loader_name = "age_groups"
        self.base_path = os.path.join(self.test_data.LOADER_ASSET_PATH, self.loader_name)

    def test_age_groups_loader_basic_config(self):
        config_file = "basic-config.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        self.assertQuerysetEqual(
            AgeGroup.objects.all(),
            ["<AgeGroup: NumericRange(8, 10, '[)')>"]
        )

    def test_age_groups_loader_missing_configuration_file(self):
        config_file = "missing.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            CouldNotFindConfigFileError,
            group_loader.load,
        )

    def test_age_groups_loader_empty_configuration_file(self):
        config_file = "empty.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            EmptyConfigFileError,
            group_loader.load,
        )

    def test_age_groups_loader_correct_slug_value(self):
        config_file = "basic-config.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        self.assertEquals(
            AgeGroup.objects.get(slug="8-10").slug,
            "8-10",
        )

    def test_age_groups_loader_correct_min_age_value(self):
        config_file = "basic-config.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        self.assertEquals(
            AgeGroup.objects.get(slug="8-10").ages.lower,
            8,
        )

    def test_age_groups_loader_missing_min_age_value(self):
        config_file = "missing-min-age.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            group_loader.load,
        )

    def test_age_groups_loader_correct_max_age_value(self):
        config_file = "basic-config.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        self.assertEquals(
            AgeGroup.objects.get(slug="8-10").ages.upper,
            10,
        )

    def test_age_groups_loader_missing_max_age_value(self):
        config_file = "missing-max-age.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            group_loader.load,
        )

    def test_age_groups_loader_correct_description_value(self):
        config_file = "description.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        self.assertEquals(
            AgeGroup.objects.get(slug="5-7").description,
            "Sample description.",
        )

    def test_age_groups_loader_missing_description_value(self):
        config_file = "basic-config.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        self.assertEqual("", AgeGroup.objects.get(slug="8-10").description)

    def test_age_groups_loader_multiple_configuration(self):
        config_file = "multiple.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        self.assertQuerysetEqual(
            AgeGroup.objects.order_by("ages"),
            [
                "<AgeGroup: NumericRange(5, 7, '[)')>",
                "<AgeGroup: NumericRange(8, 10, '[)')>",
                "<AgeGroup: NumericRange(11, 14, '[)')>",
            ]
        )
