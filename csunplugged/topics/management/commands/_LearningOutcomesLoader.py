import os.path
from django.db import transaction
from utils.BaseLoader import BaseLoader
from topics.models import LearningOutcome


class LearningOutcomesLoader(BaseLoader):
    '''Loader for learning outcomes content'''

    def __init__(self, learning_outcomes_file, BASE_PATH):
        '''Initiates the learning outcomes loader

        Args:
            learning_outcomes_file: file path (string)
        '''
        super().__init__(BASE_PATH)
        self.learning_outcomes_file = learning_outcomes_file
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(learning_outcomes_file)[0])

    @transaction.atomic
    def load(self):
        '''load the content for learning outcomes'''
        learning_outcomes = self.load_yaml_file(
            os.path.join(
                self.BASE_PATH,
                self.learning_outcomes_file
            )
        )
        
        for (outcome_slug, outcome_text) in learning_outcomes.items():
            # Create outcome objects and save to db
            outcome = LearningOutcome(
                slug=outcome_slug,
                text=outcome_text
            )
            outcome.save()
            self.log('Added Learning Outcome: {}'.format(outcome.__str__()))

        # Print log output
        self.print_load_log()
