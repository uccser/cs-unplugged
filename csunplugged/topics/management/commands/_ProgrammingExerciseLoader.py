import os.path
from utils.BaseLoader import BaseLoader
from utils.errors.MissingLearningObjective import MissingLearningObjective
from utils.errors.MissingProgrammingDifficulty import MissingProgrammingDifficulty
from utils.errors.MissingLanguageImplementation import MissingLanguageImplementation
from topics.models import (
    LearningOutcome,
    ProgrammingExerciseDifficulty,
    ProgrammingExerciseLanguage,
    ProgrammingExerciseLanguageImplementation,
)


class ProgrammingExerciseLoader(BaseLoader):
    """Loader for a programming exercise"""

    def __init__(self, load_log, exercise_slug, exercise_structure, topic, BASE_PATH):
        """Initiates the loader for a programming exercise

        Args:
            exercise_slug (string): slug for exercise
            exercise_structure (dict): attributes for exercise
            topic: Topic model object

        Raises:
            MissingProgrammingDifficulty: raised when no difficulty level matches a given
                key
            MissingLearningObjective: raised when no learning objective matches a given
                key
        """
        super().__init__(BASE_PATH, load_log)
        self.exercise_slug = exercise_slug
        self.exercise_structure = exercise_structure
        self.topic = topic

    def load(self):
        """load the content for a programming exercise"""
        content = self.convert_md_file(os.path.join(self.BASE_PATH, self.exercise_structure['md-file']))

        programming_exercise = self.topic.topic_programming_exercises.create(
            slug=self.exercise_slug,
            name=content.title,
            exercise_set_number=self.exercise_structure['exercise-set-number'],
            exercise_number=self.exercise_structure['exercise-number'],
            content=content.html_string
        )
        programming_exercise.save()

        LOG_TEMPLATE = 'Added Programming Exercise: {}'
        self.log(LOG_TEMPLATE.format(programming_exercise.name), 1)

        language_solutions = self.exercise_structure['programming-languages']
        for language in language_solutions:
            try:
                language_object = ProgrammingExerciseLanguage.objects.get(
                    slug=language
                )
            except:
                raise MissingLanguageImplementation(
                    'Programming Exercise Loader',
                    language
                )

            expected_result_path = os.path.join(self.BASE_PATH, language_solutions[language]['expected-result'])
            expected_result_content = self.convert_md_file(expected_result_path).html_string

            hint_path = os.path.join(self.BASE_PATH, language_solutions[language]['hints'])
            hint_content = self.convert_md_file(hint_path).html_string

            solution_path = os.path.join(self.BASE_PATH, language_solutions[language]['solution'])
            solution_content = self.convert_md_file(solution_path).html_string

            implementation = ProgrammingExerciseLanguageImplementation.objects.create(
                expected_result=expected_result_content,
                hints=hint_content,
                solution=solution_content,
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
                except:
                    raise MissingLearningObjective(
                        'Programming Exercise Loader',
                        learning_outcome_slug
                    )

                programming_exercise.learning_outcomes.add(learning_outcome)

        if 'difficulty-level' in self.exercise_structure:
            level = self.exercise_structure['difficulty-level']
            try:
                difficulty_level = ProgrammingExerciseDifficulty.objects.get(
                    level=level
                )
            except:
                raise MissingProgrammingDifficulty(
                    'Programming Exercise Loader',
                    level
                )

        programming_exercise.difficulty.add(difficulty_level)
