"""Custom loader for loading age group."""

from django.db import transaction
from django.utils import translation
from utils.BaseLoader import BaseLoader
from utils.TranslatableModelLoader import TranslatableModelLoader
from utils.language_utils import get_available_languages, get_default_language
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import AgeGroup


class AgeGroupsLoader(TranslatableModelLoader):
    """Loader for age group content."""

    def __init__(self, **kwargs):
        """Create the loader for loading age groups."""
        super().__init__(**kwargs)

    @transaction.atomic
    def load(self):
        """Load the content for age groups.

        Raise:
            MissingRequiredFieldError: when no object can be found with the
                matching attribute.
        """
        age_groups_structure = self.load_yaml_file(self.structure_file_path)
        age_groups_translations = self.get_yaml_translations("age-groups-strings.yaml")

        for (age_group_slug, age_group_data) in age_groups_structure.items():
            if age_group_data is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["min_age", "max_age"],
                    "Age Range"
                )

            translations = age_groups_translations.get(age_group_slug, dict())

            group_min_age = age_group_data.get("min_age", None)
            if group_min_age is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["min_age"],
                    "Age Range"
                )

            group_max_age = age_group_data.get("max_age", None)
            if group_max_age is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["max_age"],
                    "Age Range"
                )

            # Create area objects and save to database
            age_group = AgeGroup(
                slug=age_group_slug,
                ages=(int(group_min_age), int(group_max_age)),
            )
            self.populate_translations(age_group, translations)
            self.mark_translation_availability(age_group, required_fields=['description'])
            age_group.save()

            self.log("Added age group: {}".format(age_group.__str__()))

        self.log("All age groups loaded!\n")
