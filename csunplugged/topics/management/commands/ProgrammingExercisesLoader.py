from django.db import transaction
from .BaseLoader import BaseLoader
from topics.models import LearningOutcome, ProgrammingExerciseDifficulty

class ProgrammingExercisesLoader(BaseLoader):
    """Loader for programming exercises"""

    def __init__(self, load_log, structure_file, topic):
        """Initiates the loader for programming exercises

        Args:
            structure_file: file path (string)
            topic: Topic model object
        """
        super().__init__(load_log)
        self.structure_file = structure_file
        self.topic = topic

    def load(self):
        """load the content for programming exercises"""
        if self.structure_file:
            structure = self.load_yaml_file(self.structure_file)

            # For each programming exercise
            for exercise in structure:
                content = self.convert_md_file(exercise['md-file'])

                # TODO: The following block will be rewritten for #49
                scratch_hints_file = exercise['scratch']['hints']
                scratch_hints = self.convert_md_file(scratch_hints_file)
                scratch_solution_file = exercise['scratch']['solution']
                scratch_solution = self.convert_md_file(scratch_solution_file)
                python_hints_file = exercise['python']['hints']
                python_hints = self.convert_md_file(python_hints_file)
                python_solution_file = exercise['python']['solution']
                python_solution = self.convert_md_file(python_solution_file)

                programming_exercise = self.topic.topic_programming_exercises.create(  # noqa: E501
                    slug=exercise['slug'],
                    name=content.title,
                    exercise_number=exercise['exercise-number'],
                    content=content.html_string,
                    scratch_hints=scratch_hints.html_string,
                    scratch_solution=scratch_solution.html_string,
                    python_hints=python_hints.html_string,
                    python_solution=python_solution.html_string,
                    difficulty=ProgrammingExerciseDifficulty.objects.get(
                    level=exercise['difficulty-level']
                    )
                )
                programming_exercise.save()

                for learning_outcome_slug in exercise['learning-outcomes']:
                    learning_outcome = LearningOutcome.objects.get(
                        slug=learning_outcome_slug
                    )
                    programming_exercise.learning_outcomes.add(learning_outcome)  # noqa: E501

                LOG_TEMPLATE = 'Added Programming Exercise: {}'
                self.log(LOG_TEMPLATE.format(programming_exercise.name), 1)
