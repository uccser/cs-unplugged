import os.path
from django.db import transaction
from utils.BaseLoader import BaseLoader
from topics.models import LearningOutcome


class LearningOutcomesLoader(BaseLoader):
    '''Loader for learning outcomes content'''

    def __init__(self, structure_file_path, BASE_PATH):
        '''Initiates the learning outcomes loader

        Args:
            structure_file_path: file path (string)
        '''
        super().__init__(BASE_PATH)
        self.structure_file_path = structure_file_path
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file_path)[0])

    @transaction.atomic
    def load(self):
        '''load the content for learning outcomes'''
        learning_outcomes = self.load_yaml_file(
            os.path.join(
                self.BASE_PATH,
                self.structure_file_path
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
