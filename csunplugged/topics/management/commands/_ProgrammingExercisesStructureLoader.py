"""Custom loader for loading structure of programming exercises."""

import os.path
from django.db import transaction
from utils.BaseLoader import BaseLoader
from topics.models import ProgrammingExerciseLanguage, ProgrammingExerciseDifficulty


class ProgrammingExercisesStructureLoader(BaseLoader):
    """Custom loader for loading structure of programming exercises."""

    def __init__(self, structure_file, BASE_PATH):
        """Create the loader for loading structure of programming exercises.

        Args:
            structure_file: File path for structure YAML file (string).
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH)
        self.structure_file = structure_file
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file)[0])

    @transaction.atomic
    def load(self):
        """Load the content for structure of programming exercises."""
        info = self.load_yaml_file(os.path.join(self.BASE_PATH, self.structure_file))

        languages = info['languages']
        for language_data in languages:
            language = ProgrammingExerciseLanguage(
                slug=language_data,
                name=languages[language_data]['name'],
                icon=languages[language_data]['icon']
            )
            language.save()
            self.log('Added Langauge: {}'.format(language.__str__()))

        for difficulty_data in info['difficulties']:
            difficulty = ProgrammingExerciseDifficulty(
                level=difficulty_data['level'],
                name=difficulty_data['name']
            )
            difficulty.save()
            self.log('Added Difficulty Level: {}'.format(difficulty.__str__()))

        # Print log output
        self.print_load_log()
