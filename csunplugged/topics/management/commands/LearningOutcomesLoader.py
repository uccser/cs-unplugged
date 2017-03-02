import yaml
import os
from django.db import transaction
from topics.management.commands.BaseLoader import BaseLoader
from topics.models import CurriculumLink, LearningOutcome

class LearningOutcomesLoader(BaseLoader):

    def __init__(self, learning_outcomes_file):
        super().__init__()
        self.learning_outcomes_file = learning_outcomes_file

    @transaction.atomic
    def load(self):
        learning_outcomes = yaml.load(open(os.path.join(self.BASE_PATH, self.learning_outcomes_file), encoding='UTF-8').read())
        for (outcome_slug, outcome_text) in learning_outcomes.items():
            outcome = LearningOutcome(
                slug=outcome_slug,
                text=outcome_text
            )
            outcome.save()
            self.load_log.append(('Added Learning Outcome: {}'.format(outcome.__str__()), 0))

        # Print log output
        self.print_load_log()
