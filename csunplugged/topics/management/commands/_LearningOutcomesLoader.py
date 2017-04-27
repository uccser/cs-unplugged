"""Custom loader for loading learning outcomes."""

import os.path
from django.utils import timezone
from django.db import transaction

from utils.BaseLoader import BaseLoader

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import LearningOutcome


class LearningOutcomesLoader(BaseLoader):
    """Custom loader for loading learning outcomes."""

    def __init__(self, structure_file_path, BASE_PATH):
        """Create the loader for loading programming exercises.

        Args:
            structure_file_path: File path to YAML file (string)
            BASE_PATH: Base file path (string).
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

        for (outcome_slug, outcome_text) in learning_outcomes.items():

            if outcome_text is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["key:value pair"],
                    "Learning Outcome"
                )

            try:
                # Update exisiting learning outcome object
                outcome = LearningOutcome.objects.get(slug=outcome_slug)
                outcome.text = outcome_text
                outcome.save()
                self.log("Updated Learning Outcome: {}".format(outcome.__str__()))
            except LearningOutcome.DoesNotExist:
                # Create a new learning outcome object and save to db
                outcome = LearningOutcome(
                    slug=outcome_slug,
                    text=outcome_text
                )
                outcome.save()
                self.log("Added Learning Outcome: {}".format(outcome.__str__()))

        last_update_time = timezone.now()-timezone.timedelta(seconds=1)
        LearningOutcome.objects.filter(last_modified__lte=last_update_time).delete()
        for lo in LearningOutcome.objects.all():
            print(lo)

        # Print log output
        self.print_load_log()
