import os.path
from django.db import transaction

from utils.BaseLoader import BaseLoader

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import ProgrammingExerciseLanguage, ProgrammingExerciseDifficulty


class ProgrammingExercisesStructureLoader(BaseLoader):
    '''Loader for programming exercises difficulties'''

    def __init__(self, structure_file_path, BASE_PATH):
        '''Initiates the loader for programming exercises difficulties

        Args:
            structure_file_path: file path (string)
        '''
        super().__init__(BASE_PATH)
        self.structure_file_path = structure_file_path
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file_path)[0])

    @transaction.atomic
    def load(self):
        '''Load the content for programming exerises difficulties

        Raises:
            MissingRequiredFieldError:
        '''
        structure = self.load_yaml_file(
            os.path.join(
                self.BASE_PATH,
                self.structure_file_path
            )
        )

        languages = structure.get('languages', None)
        difficulty_levels = structure.get('difficulties', None)
        if None in [languages, difficulty_levels]:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ['lanugages', 'difficulties'],
                'Programming Exercise Structure'
            )

        for (language, language_data) in languages.items():

            # Check for required fields
            language_name = language_data.get('name', None)
            if language_name is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ['name'],
                    'Programming Exercise Language'
                )

            # Check if icon is given
            if 'icon' in language_data:
                language_icon = language_data['icon']
            else:
                language_icon = None

            new_language = ProgrammingExerciseLanguage(
                slug=language,
                name=language_name,
                icon=language_icon
            )

            new_language.save()

            self.log('Added Langauge: {}'.format(new_language.__str__()))

        for (difficulty, difficulty_data) in difficulty_levels.items():
            difficulty_name = difficulty_data.get('name', None)
            if difficulty_name is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ['name'],
                    'Programming Exercise Difficulty'
                )

            new_difficulty = ProgrammingExerciseDifficulty(
                level=difficulty,
                name=difficulty_name
            )
            new_difficulty.save()

            self.log('Added Difficulty Level: {}'.format(new_difficulty.__str__()))

        # Print log output
        self.print_load_log()
