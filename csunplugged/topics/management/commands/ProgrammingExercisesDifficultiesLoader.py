from django.db import transaction
from topics.management.commands.BaseLoader import BaseLoader
from topics.models import ProgrammingExerciseDifficulty

class ProgrammingExercisesDifficultiesLoader(BaseLoader):
    """Loader for programming exercises difficulties"""

    def __init__(self, difficulty_file):
        """Initiates the loader for programming exercises difficulties

        Args:
            difficulty_file: file path (string)
        """
        super().__init__()
        self.difficulty_structure_file = difficulty_file

    @transaction.atomic
    def load(self):
        """load the content for programming exerises difficulties"""
        difficulties = self.load_yaml_file(self.difficulty_structure_file)

        for difficulty_data in difficulties:
            difficulty = ProgrammingExerciseDifficulty(
                level=difficulty_data['level'],
                name=difficulty_data['name']
            )
            difficulty.save()
            self.log('Added Difficulty Level: {}'.format(difficulty.__str__()))

        # Print log output
        self.print_load_log()
