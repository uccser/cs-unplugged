import os.path
from utils.BaseLoader import BaseLoader
from ._ProgrammingExerciseLoader import ProgrammingExerciseLoader


class ProgrammingExercisesLoader(BaseLoader):
    """Loader for programming exercises"""

    def __init__(self, load_log, structure_file, topic, BASE_PATH):
        """Initiates the loader for programming exercises

        Args:
            structure_file: file path (string)
            topic: Topic model object
        """
        super().__init__(BASE_PATH, load_log)
        self.structure_file = os.path.join(self.BASE_PATH, structure_file)
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file)[0])
        self.topic = topic

    def load(self):
        """Call (single) ProgrammingExerciseLoader for each exercise
        to load into the database
        """
        programming_exercises_structure = self.load_yaml_file(self.structure_file)

        for exercise_slug, exercise_structure in programming_exercises_structure.items():
            ProgrammingExerciseLoader(
                self.load_log,
                exercise_slug,
                exercise_structure,
                self.topic,
                self.BASE_PATH
            ).load()
