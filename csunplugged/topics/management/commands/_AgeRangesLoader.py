"""Custom loader for loading age ranges."""

import os.path

from django.db import transaction

from utils.BaseLoader import BaseLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import AgeRange


class AgeRangesLoader(BaseLoader):
    """Loader for age range content."""

    def __init__(self, structure_file_path, BASE_PATH):
        """Create the loader for loading age ranges.

        Args:
            structure_file_path: File path to YAML file (string)
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH)
        self.structure_file_path = structure_file_path
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file_path)[0])

    @transaction.atomic
    def load(self):
        """Load the content for age ranges.

        Raise:
            MissingRequiredFieldError: when no object can be found with the
                                       matching attribute.
        """
        age_ranges_structure = self.load_yaml_file(
            os.path.join(
                self.BASE_PATH,
                self.structure_file_path
            )
        )

        for (age_range_slug, age_range_data) in age_ranges_structure.items():

            if age_range_data is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["min_age", "max_age"],
                    "Age Range"
                )

            range_min_age = age_range_data.get("min_age", None)
            if range_min_age is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["min_age"],
                    "Age Range"
                )

            range_max_age = age_range_data.get("max_age", None)
            if range_max_age is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["max_age"],
                    "Age Range"
                )

            range_description = age_range_data.get("description", None)

            # Create area objects and save to database
            age_range = AgeRange(
                slug=age_range_slug,
                ages=(int(range_min_age), int(range_max_age)),
                description=range_description,
            )
            age_range.save()

            self.log("Added age range: {}".format(age_range.__str__()))

        self.log("All age ranges loaded!\n")
