"""Custom loader for loading programming challenges."""

import os.path
from utils.BaseLoader import BaseLoader
from utils.language_utils import get_available_languages, get_default_language

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

    def __init__(self, topic, **kwargs):
        """Create the loader for loading programming challenges.

        Args:
            topic: Object of related topic model (Topic).
        """
        super().__init__(**kwargs)
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

            content_translations = {}
            extra_challenge_translations = {}
            for language in get_available_languages():
                # Build the path to the programming challenge's folder
                file_path = self.get_localised_file(
                    language,
                    os.path.join(challenge_slug, "{}.md")
                )

                try:
                    challenge_content = self.convert_md_file(
                        file_path.format(challenge_slug),
                        self.structure_file_path
                    )
                    content_translations[language] = challenge_content
                except CouldNotFindMarkdownFileError:
                    if language == get_default_language():
                        raise

                challenge_extra_challenge_file = challenge_structure.get("extra-challenge", None)
                if challenge_extra_challenge_file:
                    try:
                        challenge_extra_challenge_content = self.convert_md_file(
                            file_path.format(challenge_extra_challenge_file[:-3]),
                            self.structure_file_path,
                            heading_required=False,
                        )
                        extra_challenge_translations[language] = challenge_extra_challenge_content.html_string
                    except CouldNotFindMarkdownFileError:
                        if language == get_default_language():
                            raise

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
                languages=list(content_translations.keys()),
                challenge_set_number=challenge_set_number,
                challenge_number=challenge_number,
                difficulty=difficulty_level
            )
            for language in content_translations:
                setattr(
                    programming_challenge,
                    "content_{}".format(language),
                    content_translations[language].html_string
                )
                setattr(
                    programming_challenge,
                    "name_{}".format(language),
                    content_translations[language].title
                )
            for language in extra_challenge_translations:
                setattr(
                    programming_challenge,
                    "extra_challenge_{}".format(language),
                    extra_challenge_translations[language]
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
                expected_result_translations = {}
                solution_translations = {}
                hint_translations = {}

                for translation_language in get_available_languages():
                    file_path = self.get_localised_file(
                        language,
                        os.path.join(challenge_slug, "{}.md")
                    )
                    try:
                        expected_result_content = self.convert_md_file(
                            file_path.format(
                                "{}-expected".format(language)
                            ),
                            self.structure_file_path,
                            heading_required=False
                        )
                        expected_result_translations[translation_language] = expected_result_content.html_string
                    except CouldNotFindMarkdownFileError:
                        if language == get_default_language():
                            raise

                    # Load example solution
                    try:
                        solution_content = self.convert_md_file(
                            file_path.format(
                                "{}-solution".format(language)
                            ),
                            self.structure_file_path,
                            heading_required=False
                        )
                        solution_translations[translation_language] = solution_content.html_string
                    except CouldNotFindMarkdownFileError:
                        if language == get_default_language():
                            raise

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
                        pass

                implementation = ProgrammingChallengeImplementation(
                    languages=list(solution_translations.keys()),
                    language=language_object,
                    challenge=programming_challenge,
                    topic=self.topic
                )
                for translation_language in solution_translations:
                    setattr(
                        implementation,
                        "solution_{}".format(translation_language),
                        solution_translations[translation_language]
                    )
                for translation_language in hint_translations:
                    setattr(
                        implementation,
                        "hint_{}".format(translation_language),
                        hint_translations[translation_language]
                    )
                for translation_language in expected_result_translations:
                    setattr(
                        implementation,
                        "expected_result_{}".format(translation_language),
                        expected_result_translations[translation_language]
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
