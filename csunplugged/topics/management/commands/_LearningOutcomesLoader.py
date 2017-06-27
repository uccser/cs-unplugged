"""Custom loader for loading learning outcomes."""

import os.path
from django.db import transaction

from utils.BaseLoader import BaseLoader
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from topics.models import (
    LearningOutcome,
    CurriculumArea,
)


class LearningOutcomesLoader(BaseLoader):
    """Custom loader for loading learning outcomes."""

    def __init__(self, structure_file_path, BASE_PATH):
        """Create the loader for loading learning outcomes.

        Args:
            structure_file_path: File path to YAML file (str).
            BASE_PATH: Base file path (str).
        """
        super().__init__(BASE_PATH)
        self.structure_file_path = structure_file_path
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file_path)[0])

    @transaction.atomic
    def load(self):
        """Load the content for learning outcomes.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        learning_outcomes = self.load_yaml_file(
            os.path.join(
                self.BASE_PATH,
                self.structure_file_path
            )
        )

        for (outcome_slug, outcome_data) in learning_outcomes.items():

            if ("text" not in outcome_data) or (outcome_data["text"] is None):
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["text"],
                    "Learning Outcome"
                )

            # Create outcome objects and save to db
            outcome = LearningOutcome(
                slug=outcome_slug,
                text=outcome_data["text"]
            )
            outcome.save()

            # Add curriculum areas
            curriculum_area_slugs = outcome_data.get("curriculum-areas", [])
            for curriculum_area_slug in curriculum_area_slugs:
                try:
                    curriculum_area = CurriculumArea.objects.get(
                        slug=curriculum_area_slug
                    )
                    outcome.curriculum_areas.add(curriculum_area)
                except:
                    raise KeyNotFoundError(
                        self.structure_file_path,
                        curriculum_area_slug,
                        "Curriculum Areas"
                    )

            self.log("Added learning outcome: {}".format(outcome.__str__()))

        self.log("All learning outcomes loaded!\n")
