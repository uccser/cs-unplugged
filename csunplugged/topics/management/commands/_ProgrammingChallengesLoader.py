"""Custom loader for loading programming challenges."""

import os.path
from utils.BaseLoader import BaseLoader

from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import (
    LearningOutcome,
    ProgrammingChallengeDifficulty,
    ProgrammingChallengeLanguage,
    ProgrammingChallengeImplementation,
)


class ProgrammingChallengesLoader(BaseLoader):
    """Custom loader for loading programming challenges."""

    def __init__(self, structure_file_path, topic, BASE_PATH):
        """Create the loader for loading programming challenges.

        Args:
            structure_file_path: File path for structure YAML file (string).
            topic: Object of related topic model.
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH)
        self.structure_file_path = os.path.join(self.BASE_PATH, structure_file_path)
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file_path)[0])
        self.topic = topic

    def load(self):
        """Load the content for programming challenges.

        Raise:
            KeyNotFoundError: when no object can be found with the matching attribute.
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        programming_challenges_structure = self.load_yaml_file(self.structure_file_path)

        for (challenge_slug, challenge_structure) in programming_challenges_structure.items():

            if challenge_structure is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["challenge-set-number", "challenge-number",
                        "programming-languages", "difficulty-level"],
                    "Programming Challenge"
                )

            # Retrieve required variables from md file
            challenge_set_number = challenge_structure.get("challenge-set-number", None)
            challenge_number = challenge_structure.get("challenge-number", None)
            challenge_languages = challenge_structure.get("programming-languages", None)
            challenge_difficulty = challenge_structure.get("difficulty-level", None)
            if None in [challenge_set_number, challenge_number, challenge_languages, challenge_difficulty]:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["challenge-set-number", "challenge-number",
                        "programming-languages", "difficulty-level"],
                    "Programming Challenge"
                )

            # Build the path to the programming challenge's folder
            file_path = os.path.join(
                self.BASE_PATH,
                challenge_slug,
                "{}.md"
            )

            challenge_content = self.convert_md_file(
                file_path.format(challenge_slug),
                self.structure_file_path
            )

            challenge_extra_challenge_file = challenge_structure.get("extra-challenge", None)
            if challenge_extra_challenge_file:
                challenge_extra_challenge_content = self.convert_md_file(
                    file_path.format(challenge_extra_challenge_file[:-3]),
                    self.structure_file_path,
                    heading_required=False,
                )
                challenge_extra_challenge = challenge_extra_challenge_content.html_string
            else:
                challenge_extra_challenge = None

            try:
                difficulty_level = ProgrammingChallengeDifficulty.objects.get(
                    level=challenge_difficulty
                )
            except:
                raise KeyNotFoundError(
                    self.structure_file_path,
                    challenge_difficulty,
                    "Programming Challenge Difficulty"
                )

            programming_challenge = self.topic.programming_challenges.create(
                slug=challenge_slug,
                name=challenge_content.title,
                challenge_set_number=challenge_set_number,
                challenge_number=challenge_number,
                content=challenge_content.html_string,
                extra_challenge=challenge_extra_challenge,
                difficulty=difficulty_level
            )
            programming_challenge.save()

            LOG_TEMPLATE = "Added programming challenge: {}"
            self.log(LOG_TEMPLATE.format(programming_challenge.name), 1)

            for language in challenge_languages:
                if language is None:
                    raise MissingRequiredFieldError(
                        self.structure_file_path,
                        ["challenge-set-number", "challenge-number",
                            "programming-languages", "difficulty-level"],
                        "Programming Challenge"
                    )
                try:
                    language_object = ProgrammingChallengeLanguage.objects.get(
                        slug=language
                    )
                except:
                    raise KeyNotFoundError(
                        self.structure_file_path,
                        language,
                        "Programming Challenge Language"
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

                implementation = ProgrammingChallengeImplementation(
                    expected_result=expected_result_content.html_string,
                    hints=None if hint_content is None else hint_content.html_string,
                    solution=solution_content.html_string,
                    language=language_object,
                    challenge=programming_challenge,
                    topic=self.topic
                )
                implementation.save()

                LOG_TEMPLATE = "Added language implementation: {}"
                self.log(LOG_TEMPLATE.format(implementation.language), 2)

            if "learning-outcomes" in challenge_structure:
                learning_outcomes = challenge_structure["learning-outcomes"]
                if learning_outcomes is not None:
                    for learning_outcome_slug in learning_outcomes:
                        try:
                            learning_outcome = LearningOutcome.objects.get(
                                slug=learning_outcome_slug
                            )
                            programming_challenge.learning_outcomes.add(learning_outcome)
                        except:
                            raise KeyNotFoundError(
                                self.structure_file_path,
                                learning_outcome_slug,
                                "Learning Outcome")
