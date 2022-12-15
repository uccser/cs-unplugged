import os.path

from django.utils import translation

from tests.BaseTestWithDB import BaseTestWithDB
from tests.topics.TopicsTestDataGenerator import TopicsTestDataGenerator

from topics.models import AgeGroup
from topics.management.commands._AgeGroupsLoader import AgeGroupsLoader

from utils.errors.CouldNotFindYAMLFileError import CouldNotFindYAMLFileError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.EmptyYAMLFileError import EmptyYAMLFileError


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
            CouldNotFindYAMLFileError,
            group_loader.load,
        )

    def test_age_groups_loader_empty_configuration_file(self):
        config_file = "empty.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            EmptyYAMLFileError,
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

    def test_age_groups_loader_missing_data(self):
        config_file = "missing-data.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        self.assertRaises(
            MissingRequiredFieldError,
            group_loader.load,
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

    def test_age_groups_loader_missing_translation(self):
        config_file = "description.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        age_group = AgeGroup.objects.get(slug="5-7")
        self.assertSetEqual(set(["en"]), set(age_group.languages))

        # Check description does not fall back to english for missing translation
        with translation.override("de"):
            self.assertEqual("", age_group.description)

    def test_age_groups_loader_translation(self):
        config_file = "translation.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        age_group = AgeGroup.objects.get(slug="5-7")
        self.assertSetEqual(set(["en", "de"]), set(age_group.languages))
        self.assertEqual("English description.", age_group.description)
        with translation.override("de"):
            self.assertEqual("German description.", age_group.description)

    def test_age_groups_same_slugs(self):
        config_file = "same-slugs.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        self.assertQuerysetEqual(
            AgeGroup.objects.filter(slug="8-10"),
            ["<AgeGroup: NumericRange(8, 10, '[)')>"]
        )

    def test_age_groups_insert_middle(self):
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

        config_file = "insert-middle.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        self.assertQuerysetEqual(
            AgeGroup.objects.order_by("ages"),
            [
                "<AgeGroup: NumericRange(5, 7, '[)')>",
                "<AgeGroup: NumericRange(7, 8, '[)')>",
                "<AgeGroup: NumericRange(8, 10, '[)')>",
                "<AgeGroup: NumericRange(11, 14, '[)')>",
            ]
        )

    def test_age_groups_remove_end(self):
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

        config_file = "remove-end.yaml"
        group_loader = AgeGroupsLoader(structure_filename=config_file, base_path=self.base_path)
        group_loader.load()
        self.assertQuerysetEqual(
            AgeGroup.objects.order_by("ages"),
            [
                "<AgeGroup: NumericRange(5, 7, '[)')>",
                "<AgeGroup: NumericRange(8, 10, '[)')>",
            ]
        )
