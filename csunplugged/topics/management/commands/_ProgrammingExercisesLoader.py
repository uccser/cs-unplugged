"""Custom loader for loading programming exercises."""

import os.path
from utils.BaseLoader import BaseLoader
from ._ProgrammingExerciseLoader import ProgrammingExerciseLoader


class ProgrammingExercisesLoader(BaseLoader):
    """Custom loader for loading programming exercises."""

    def __init__(self, load_log, structure_file, topic, BASE_PATH):
        """Create the loader for loading programming exercises.

        Args:
            load_log: List of log messages (list).
            structure_file: File path for structure YAML file (string).
            topic: Object of related topic model.
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH, load_log)
        self.structure_file = os.path.join(self.BASE_PATH, structure_file)
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file)[0])
        self.topic = topic

    def load(self):
        """Load the content for programming exercises."""
        programming_exercises_structure = self.load_yaml_file(self.structure_file)

        for exercise_slug, exercise_structure in programming_exercises_structure.items():
            ProgrammingExerciseLoader(
                self.load_log,
                exercise_slug,
                exercise_structure,
                self.topic,
                self.BASE_PATH
            ).load()
