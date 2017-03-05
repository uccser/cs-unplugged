from django.db import transaction
from topics.management.commands.BaseLoader import BaseLoader
from topics.models import LearningOutcome, ProgrammingExerciseDifficulty

class ProgrammingExercisesLoader(BaseLoader):
    """Loader for programming exercises"""

    def __init__(self, load_log, programming_exercises_structure_file, topic):
        """Initiates the loader for programming exercises

        Args:
            programming_exercises_structure_file: file path (string)
            topic: Topic model object
        """
        super().__init__(load_log)
        self.programming_exercises_structure_file = programming_exercises_structure_file
        self.topic = topic

    def load(self):
        """load the content for programming exercises"""
        if self.programming_exercises_structure_file:
            structure = self.load_yaml_file(self.programming_exercises_structure_file)

            for programming_exercise_data in structure:
                programming_exercise_content = self.convert_md_file(programming_exercise_data['md-file'])

                programming_exercise = self.topic.topic_programming_exercises.create(
                    slug=programming_exercise_data['slug'],
                    name=programming_exercise_content.title,
                    exercise_number=programming_exercise_data['exercise-number'],
                    content=programming_exercise_content.html_string,
                    scratch_hints=self.convert_md_file(programming_exercise_data['scratch']['hints']).html_string,
                    scratch_solution=self.convert_md_file(programming_exercise_data['scratch']['solution']).html_string,
                    python_hints=self.convert_md_file(programming_exercise_data['python']['hints']).html_string,
                    python_solution=self.convert_md_file(programming_exercise_data['python']['solution']).html_string,
                    difficulty=ProgrammingExerciseDifficulty.objects.get(
                        level=programming_exercise_data['difficulty-level']
                    )
                )
                programming_exercise.save()

                for learning_outcome_slug in programming_exercise_data['learning-outcomes']:
                    learning_outcome = LearningOutcome.objects.get(
                        slug=learning_outcome_slug
                    )
                    programming_exercise.learning_outcomes.add(learning_outcome)

                self.log('Added Programming Exercise: {}'.format(programming_exercise.name), 1)
