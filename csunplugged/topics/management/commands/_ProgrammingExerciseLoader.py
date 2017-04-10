import os.path

from utils.BaseLoader import BaseLoader

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.KeyNotFoundError import KeyNotFoundError

from topics.models import (
    LearningOutcome,
    ProgrammingExerciseDifficulty,
    ProgrammingExerciseLanguage,
    ProgrammingExerciseLanguageImplementation,
)


class ProgrammingExerciseLoader(BaseLoader):
    '''Loader for a programming exercise'''

    def __init__(self, load_log, exercise_slug, exercise_structure, topic, BASE_PATH):
        '''Initiates the loader for a programming exercise

        Args:
            exercise_slug (string): slug for exercise
            exercise_structure (dict): attributes for exercise
            topic: Topic model object
        '''
        super().__init__(BASE_PATH, load_log)
        self.exercise_slug = exercise_slug
        self.exercise_structure = exercise_structure
        self.topic = topic

    def load(self):
        '''Load the content for a programming exercise

        Raises:
            MissingRequiredFieldError:
            CouldNotFindMarkdownFileError:
            EmptyMarkdownFileError:
            KeyNotFoundError:
        '''
        # Retrieve required variables from md file
        try:
            exercise_set_number = self.exercise_structure['exercise-set-number']
            exercise_number = self.exercise_structure['exercise-number']
            exercise_languages = self.exercise_structure['programming-languages']
            exercise_difficulty = self.exercise_structure['difficulty-level']
        except:
            raise MissingRequiredFieldError()

        # Build the path to the programming exercise's folder
        file_path = os.path.join(
            self.BASE_PATH,
            self.exercise_slug,
            '{}.md'
        )

        # Throw and error if the md file cannot be found
        try:
            exercise_content = self.convert_md_file(
                file_path.format('index')
            )
        except:
            raise CouldNotFindMarkdownFileError()

        # Check that content is not empty and that a title was extracted
        if exercise_content.title is None:
            raise MarkdownFileMissingTitleError()
        
        if len(exercise_content.html_string) == 0:
            raise EmptyMarkdownFileError()

        try:
            difficulty_level = ProgrammingExerciseDifficulty.objects.get(
                level=exercise_difficulty
            )
        except:
            raise KeyNotFoundError()

        programming_exercise = self.topic.topic_programming_exercises.create(
            slug=self.exercise_slug,
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

            try:
                expected_result_content = self.convert_md_file(
                    file_path.format(
                        '{}-expected'.format(language)
                    )
                )
            except:
                raise CouldNotFindMarkdownFileError()

            if len(expected_result_content.html_string) == 0:
                raise EmptyMarkdownFileError()

            try:
                hint_content = self.convert_md_file(
                    file_path.format(
                        '{}-hints'.format(language)
                    )
                )
            except:
                raise CouldNotFindMarkdownFileError()

            if len(hint_content.html_string) == 0:
                raise EmptyMarkdownFileError()  

            try:
                solution_content = self.convert_md_file(
                    file_path.format(
                        '{}-solution'.format(language)
                    )
                )
            except:
                raise CouldNotFindMarkdownFileError()
            
            if len(solution_content.html_string) == 0:
                raise EmptyMarkdownFileError()
        
            implementation = ProgrammingExerciseLanguageImplementation.objects.create(
                expected_result=expected_result_content.html_string,
                hints=hint_content.html_string,
                solution=solution_content.html_string,
                language=language_object,
                exercise=programming_exercise,
                topic=self.topic
            )
            implementation.save()

            LOG_TEMPLATE = 'Added Language Implementation: {}'
            self.log(LOG_TEMPLATE.format(implementation.language), 2)

        if 'learning-outcomes' in self.exercise_structure:
            for learning_outcome_slug in self.exercise_structure['learning-outcomes']:
                try:
                    learning_outcome = LearningOutcome.objects.get(
                        slug=learning_outcome_slug
                    )
                    programming_exercise.learning_outcomes.add(learning_outcome)
                except:
                    raise KeyNotFoundError()
