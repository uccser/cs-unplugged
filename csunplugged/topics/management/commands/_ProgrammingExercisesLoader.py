import os.path
from utils.BaseLoader import BaseLoader

from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from utils.errors.NoHeadingFoundInMarkdownFileError import NoHeadingFoundInMarkdownFileError
from utils.errors.KeyNotFoundError import KeyNotFoundError

from topics.models import (
    LearningOutcome,
    ProgrammingExerciseDifficulty,
    ProgrammingExerciseLanguage,
    ProgrammingExerciseLanguageImplementation,
)


class ProgrammingExercisesLoader(BaseLoader):
    '''Loader for programming exercises'''

    def __init__(self, load_log, structure_file_path, topic, BASE_PATH):
        '''Initiates the loader for programming exercises

        Args:
            structure_file_path: file path (string)
            topic: Topic model object
        '''
        super().__init__(BASE_PATH, load_log)
        self.structure_file_path = os.path.join(self.BASE_PATH, structure_file_path)
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file_path)[0])
        self.topic = topic

    def load(self):
        '''Load the content for programming exercises

        Raises:
            MissingRequiredFieldError:
            CouldNotFindMarkdownFileError:
            EmptyMarkdownFileError:
            KeyNotFoundError:
        '''
        
        programming_exercises_structure = self.load_yaml_file(self.structure_file_path)

        for (exercise_slug, exercise_structure) in programming_exercises_structure.items():
            # Retrieve required variables from md file
            exercise_set_number = exercise_structure.get('exercise-set-number', None)
            exercise_number = exercise_structure.get('exercise-number', None)
            exercise_languages = exercise_structure.get('programming-languages', None)
            exercise_difficulty = exercise_structure.get('difficulty-level', None)
            if None in [exercise_set_number, exercise_number, exercise_languages, exercise_difficulty]:
                raise MissingRequiredFieldError(
                    self.programming_exercises_structure,
                    ['exercise-set-number', 'exercise-number',
                        'programming-languages', 'difficulty-level'],
                    'Programming Exercise'
                )

            # Build the path to the programming exercise's folder
            file_path = os.path.join(
                self.BASE_PATH,
                exercise_slug,
                '{}.md'
            )

            exercise_content = self.convert_md_file(
                file_path.format(exercise_slug),
                self.structure_file_path
            )

            try:
                difficulty_level = ProgrammingExerciseDifficulty.objects.get(
                    level=exercise_difficulty
                )
            except:
                raise KeyNotFoundError()

            programming_exercise = self.topic.topic_programming_exercises.create(
                slug=exercise_slug,
                name=exercise_content.title,
                exercise_set_number=exercise_set_number,
                exercise_number=exercise_number,
                content=exercise_content.html_string,
                difficulty=difficulty_level
            )
            programming_exercise.save()

            LOG_TEMPLATE = 'Added Programming Exercise: {}'
            self.log(LOG_TEMPLATE.format(programming_exercise.name), 1)

            for language in exercise_languages:
                try:
                    language_object = ProgrammingExerciseLanguage.objects.get(
                        slug=language
                    )
                except:
                    raise KeyNotFoundError()

                expected_result_content = self.convert_md_file(
                    file_path.format(
                        '{}-expected'.format(language)
                    ),
                    self.structure_file_path,
                    heading_required=False
                )

                # Load example solution
                solution_content = self.convert_md_file(
                    file_path.format(
                        '{}-solution'.format(language)
                    ),
                    self.structure_file_path,
                    heading_required=False
                )

                # Load hint if given
                try:
                    hint_content = self.convert_md_file(
                        file_path.format(
                            '{}-hints'.format(language)
                        ),
                        self.structure_file_path,
                        heading_required=False
                    )
                except CouldNotFindMarkdownFileError:
                    hint_content = None
            
                implementation = ProgrammingExerciseLanguageImplementation(
                    expected_result=expected_result_content.html_string,
                    hints=None if hint_content is None else hint_content.html_string,
                    solution=solution_content.html_string,
                    language=language_object,
                    exercise=programming_exercise,
                    topic=self.topic
                )
                implementation.save()

                LOG_TEMPLATE = 'Added Language Implementation: {}'
                self.log(LOG_TEMPLATE.format(implementation.language), 2)

            if 'learning-outcomes' in exercise_structure:
                for learning_outcome_slug in exercise_structure['learning-outcomes']:
                    try:
                        learning_outcome = LearningOutcome.objects.get(
                            slug=learning_outcome_slug
                        )
                        programming_exercise.learning_outcomes.add(learning_outcome)
                    except:
                        raise KeyNotFoundError()
