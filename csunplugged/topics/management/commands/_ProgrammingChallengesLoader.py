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

    def __init__(self, structure_file_path, topic, BASE_PATH, INNER_PATH):
        """Create the loader for loading programming challenges.

        Args:
            structure_file_path: File path for structure YAML file (str).
            topic: Object of related topic model (Topic).
            BASE_PATH: Base file path (str).
        """
        super().__init__(BASE_PATH)
        self.structure_file_path = os.path.join(self.BASE_PATH, self.STRUCTURE_DIR, INNER_PATH, structure_file_path)
        self.INNER_PATH = os.path.join(INNER_PATH, os.path.split(structure_file_path)[0])
        #TODO This calculating of the structure_file_path before the __init__ call is not very nice and
        # should be integrated with INNER_PATH
        self.topic = topic

    def load(self):
        """Load the content for programming challenges.

        Raises:
            CouldNotFindMarkdownFileError: when no file can be found with the provided filename.
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

            available_translations = challenge_structure.get('available_translations', ["en", "de"])
            content_translations = {}
            extra_challenge_translations = {}
            for language in available_translations:
                # Build the path to the programming challenge's folder
                file_path = os.path.join(
                    self.BASE_PATH,
                    language,
                    self.INNER_PATH,
                    challenge_slug,
                    "{}.md"
                )

                challenge_content = self.convert_md_file(
                    file_path.format(challenge_slug),
                    self.structure_file_path
                )
                content_translations[language] = challenge_content

                challenge_extra_challenge_file = challenge_structure.get("extra-challenge", None)
                if challenge_extra_challenge_file:
                    challenge_extra_challenge_content = self.convert_md_file(
                        file_path.format(challenge_extra_challenge_file[:-3]),
                        self.structure_file_path,
                        heading_required=False,
                    )
                    extra_challenge_translations[language] = challenge_extra_challenge_content.html_string

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
                # name=challenge_content.title,
                challenge_set_number=challenge_set_number,
                challenge_number=challenge_number,
                # content=challenge_content.html_string,
                # extra_challenge=challenge_extra_challenge,
                difficulty=difficulty_level
            )
            for language in content_translations:
                setattr(programming_challenge, "content_{}".format(language), content_translations[language].html_string)
                setattr(programming_challenge, "name_{}".format(language), content_translations[language].title)
            for language in extra_challenge_translations:
                setattr(programming_challenge, "extra_challenge_{}".format(language), extra_challenge_translations[language])

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
                expected_result_translations = {}
                solution_translations = {}
                hint_translations = {}

                for translation_language in available_translations:
                    file_path = os.path.join(
                        self.BASE_PATH,
                        translation_language,
                        self.INNER_PATH,
                        challenge_slug,
                        "{}.md"
                    )
                    expected_result_content = self.convert_md_file(
                        file_path.format(
                            "{}-expected".format(language)
                        ),
                        self.structure_file_path,
                        heading_required=False
                    )
                    expected_result_translations[translation_language] = expected_result_content.html_string

                    # Load example solution
                    solution_content = self.convert_md_file(
                        file_path.format(
                            "{}-solution".format(language)
                        ),
                        self.structure_file_path,
                        heading_required=False
                    )
                    solution_translations[translation_language] = solution_content.html_string

                    # Load hint if given
                    try:
                        hint_content = self.convert_md_file(
                            file_path.format(
                                "{}-hints".format(language)
                            ),
                            self.structure_file_path,
                            heading_required=False
                        )
                        hint_translations[translation_language] = hint_content.html_string
                    except CouldNotFindMarkdownFileError:
                        hint_content = None

                implementation = ProgrammingChallengeImplementation(
                    # expected_result=expected_result_content.html_string,
                    # hints=None if hint_content is None else hint_content.html_string,
                    # solution=solution_content.html_string,
                    language=language_object,
                    challenge=programming_challenge,
                    topic=self.topic
                )
                for translation_language in solution_translations:
                    setattr(implementation, "solution_{}".format(translation_language), solution_translations[translation_language])
                for translation_language in hint_translations:
                    setattr(implementation, "hint_{}".format(translation_language), hint_translations[translation_language])
                for translation_language in expected_result_translations:
                    setattr(implementation, "expected_result_{}".format(translation_language), expected_result_translations[translation_language])
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
