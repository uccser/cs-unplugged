from django.db import transaction
from .BaseLoader import BaseLoader
from topics.models import ProgrammingExerciseLanguage, ProgrammingExerciseDifficulty


class ProgrammingExercisesStructureLoader(BaseLoader):
    """Loader for programming exercises difficulties"""

    def __init__(self, structure_file):
        """Initiates the loader for programming exercises difficulties

        Args:
            structure_file: file path (string)
        """
        super().__init__()
        self.structure_file = structure_file

    @transaction.atomic
    def load(self):
        """load the content for programming exerises difficulties"""
        info = self.load_yaml_file(self.structure_file)

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
