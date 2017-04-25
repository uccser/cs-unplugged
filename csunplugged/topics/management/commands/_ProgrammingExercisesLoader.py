"""Custom loader for loading programming exercises."""

import os.path
from utils.BaseLoader import BaseLoader

from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from utils.errors.NoHeadingFoundInMarkdownFileError import NoHeadingFoundInMarkdownFileError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import (
    LearningOutcome,
    ProgrammingExerciseDifficulty,
    ProgrammingExerciseLanguage,
    ProgrammingExerciseLanguageImplementation,
)


class ProgrammingExercisesLoader(BaseLoader):
    """Custom loader for loading programming exercises."""

    def __init__(self, load_log, structure_file_path, topic, BASE_PATH):
        """Create the loader for loading programming exercises.

        Args:
            load_log: List of log messages (list).
            structure_file_path: File path for structure YAML file (string).
            topic: Object of related topic model.
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH, load_log)
        self.structure_file_path = os.path.join(self.BASE_PATH, structure_file_path)
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file_path)[0])
        self.topic = topic

    def load(self):
        """Load the content for programming exercises

        Raises:
            MissingRequiredFieldError:
            CouldNotFindMarkdownFileError:
            KeyNotFoundError:
        """
        programming_exercises_structure = self.load_yaml_file(self.structure_file_path)

        for (exercise_slug, exercise_structure) in programming_exercises_structure.items():

            if exercise_structure is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["exercise-set-number", "exercise-number",
                        "programming-languages", "difficulty-level"],
                    "Programming Exercise"
                )

            # Retrieve required variables from md file
            exercise_set_number = exercise_structure.get("exercise-set-number", None)
            exercise_number = exercise_structure.get("exercise-number", None)
            exercise_languages = exercise_structure.get("programming-languages", None)
            exercise_difficulty = exercise_structure.get("difficulty-level", None)
            if None in [exercise_set_number, exercise_number, exercise_languages, exercise_difficulty]:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["exercise-set-number", "exercise-number",
                        "programming-languages", "difficulty-level"],
                    "Programming Exercise"
                )

            # Build the path to the programming exercise"s folder
            file_path = os.path.join(
                self.BASE_PATH,
=======
        """Load the content for programming exercises."""
        programming_exercises_structure = self.load_yaml_file(self.structure_file)

        for exercise_slug, exercise_structure in programming_exercises_structure.items():
            ProgrammingExerciseLoader(
                self.load_log,
>>>>>>> develop
                exercise_slug,
                "{}.md"
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
                raise KeyNotFoundError(
                    self.structure_file_path,
                    exercise_difficulty,
                    "Programming Exercise Difficulty"
                )

            programming_exercise = self.topic.topic_programming_exercises.create(
                slug=exercise_slug,
                name=exercise_content.title,
                exercise_set_number=exercise_set_number,
                exercise_number=exercise_number,
                content=exercise_content.html_string
            )
            programming_exercise.difficulty.add(difficulty_level)
            programming_exercise.save()

            LOG_TEMPLATE = "Added Programming Exercise: {}"
            self.log(LOG_TEMPLATE.format(programming_exercise.name), 1)

            for language in exercise_languages:
                if language is None:
                    raise MissingRequiredFieldError(
                        self.structure_file_path,
                        ["exercise-set-number", "exercise-number",
                            "programming-languages", "difficulty-level"],
                        "Programming Exercise"
                    )
                try:
                    language_object = ProgrammingExerciseLanguage.objects.get(
                        slug=language
                    )
                except:
                    raise KeyNotFoundError(
                        self.structure_file_path,
                        language,
                        "Programming Exercise Language"
                        )

                expected_result_content = self.convert_md_file(
                    file_path.format(
                        "{}-expected".format(language)
                    ),
                    self.structure_file_path,
                    heading_required=False
                )

                # Load example solution
                solution_content = self.convert_md_file(
                    file_path.format(
                        "{}-solution".format(language)
                    ),
                    self.structure_file_path,
                    heading_required=False
                )

                # Load hint if given
                try:
                    hint_content = self.convert_md_file(
                        file_path.format(
                            "{}-hints".format(language)
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

                LOG_TEMPLATE = "Added Language Implementation: {}"
                self.log(LOG_TEMPLATE.format(implementation.language), 2)

            if "learning-outcomes" in exercise_structure:
                learning_outcomes = exercise_structure["learning-outcomes"]
                if learning_outcomes is not None:
                    for learning_outcome_slug in learning_outcomes:
                        try:
                            learning_outcome = LearningOutcome.objects.get(
                                slug=learning_outcome_slug
                            )
                            programming_exercise.learning_outcomes.add(learning_outcome)
                        except:
                            raise KeyNotFoundError(
                                self.structure_file_path,
                                learning_outcome_slug,
                                "Learning Outcome")
