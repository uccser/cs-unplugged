"""Custom loader for loading programming challenges."""

import os.path
from django.core.exceptions import ObjectDoesNotExist
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.TranslatableModelLoader import TranslatableModelLoader

from plugging_it_in.models import (
    TestCase
)

from topics.models import (
    LearningOutcome,
    ProgrammingChallengeDifficulty,
    ProgrammingChallengeLanguage,
    ProgrammingChallengeImplementation,
)


class ProgrammingChallengesLoader(TranslatableModelLoader):
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

            challenge_translations = self.get_blank_translation_dictionary()

            # Retrieve required variables from md file
            challenge_set_number = challenge_structure.get("challenge-set-number", None)
            challenge_number = challenge_structure.get("challenge-number", None)
            challenge_prog_languages = challenge_structure.get("programming-languages", None)
            challenge_difficulty = challenge_structure.get("difficulty-level", None)
            if None in [challenge_set_number, challenge_number, challenge_prog_languages, challenge_difficulty]:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["challenge-set-number", "challenge-number",
                        "programming-languages", "difficulty-level"],
                    "Programming Challenge"
                )

            content_filename = "{0}.md".format(challenge_slug)
            content_translations = self.get_markdown_translations(
                os.path.join(challenge_slug, content_filename)
            )

            for language, content in content_translations.items():
                challenge_translations[language]["content"] = content.html_string
                challenge_translations[language]["name"] = content.title

            testing_examples_translations = self.get_markdown_translations(
                os.path.join(challenge_slug, "testing-examples.md"),
                heading_required=True,
                required=True
            )
            for language, content in testing_examples_translations.items():
                challenge_translations[language]["testing_examples"] = content.html_string

            challenge_extra_challenge_file = challenge_structure.get("extra-challenge", None)
            if challenge_extra_challenge_file:
                extra_challenge_translations = self.get_markdown_translations(
                    os.path.join(challenge_slug, challenge_extra_challenge_file),
                    heading_required=False,
                )
                for language, content in extra_challenge_translations.items():
                    challenge_translations[language]["extra_challenge"] = content.html_string

            try:
                difficulty_level = ProgrammingChallengeDifficulty.objects.get(
                    level=challenge_difficulty
                )
            except ObjectDoesNotExist:
                raise KeyNotFoundError(
                    self.structure_file_path,
                    challenge_difficulty,
                    "Programming Challenge Difficulty"
                )

            programming_challenge = self.topic.programming_challenges.create(
                slug=challenge_slug,
                challenge_set_number=challenge_set_number,
                challenge_number=challenge_number,
                difficulty=difficulty_level
            )
            self.populate_translations(programming_challenge, challenge_translations)
            self.mark_translation_availability(
                programming_challenge,
                required_fields=["name", "content", "testing_examples"]
            )

            programming_challenge.save()

            LOG_TEMPLATE = "Added programming challenge: {}"
            self.log(LOG_TEMPLATE.format(programming_challenge.name), 1)

            for prog_language in challenge_prog_languages:
                if prog_language is None:
                    raise MissingRequiredFieldError(
                        self.structure_file_path,
                        ["challenge-set-number", "challenge-number",
                            "programming-languages", "difficulty-level"],
                        "Programming Challenge"
                    )
                try:
                    prog_language_object = ProgrammingChallengeLanguage.objects.get(
                        slug=prog_language
                    )
                except ObjectDoesNotExist:
                    raise KeyNotFoundError(
                        self.structure_file_path,
                        prog_language,
                        "Programming Challenge Language"
                    )

                implementation_translations = self.get_blank_translation_dictionary()

                filename_template = os.path.join(
                    challenge_slug,
                    "{}-{{}}.md".format(prog_language)
                )

                expected_result_translations = self.get_markdown_translations(
                    filename_template.format("expected"),
                    heading_required=False
                )
                for language, content in expected_result_translations.items():
                    implementation_translations[language]["expected_result"] = content.html_string

                solution_translations = self.get_markdown_translations(
                    filename_template.format("solution"),
                    heading_required=False
                )
                for language, content in solution_translations.items():
                    implementation_translations[language]["solution"] = content.html_string

                hints_translations = self.get_markdown_translations(
                    filename_template.format("hints"),
                    heading_required=False,
                    required=False
                )
                for language, content in hints_translations.items():
                    implementation_translations[language]["hints"] = content.html_string

                implementation = ProgrammingChallengeImplementation(
                    language=prog_language_object,
                    challenge=programming_challenge,
                    topic=self.topic
                )

                self.populate_translations(implementation, implementation_translations)
                self.mark_translation_availability(implementation, required_fields=["solution", "expected_result"])

                implementation.save()

                LOG_TEMPLATE = "Added language implementation: {}"
                self.log(LOG_TEMPLATE.format(implementation.language), 2)

            test_cases = challenge_structure.get("test-cases", None)
            if (test_cases is not None):
                for (testcase_id, testcase_type) in test_cases.items():
                    test_case_translations = self.get_blank_translation_dictionary()

                    testcase_filename_template = os.path.join(
                        challenge_slug,
                        'test-cases',
                        "test-case-{}-{{}}.txt".format(testcase_id)
                    )

                    testcase_input = open(self.get_localised_file(
                        "en", testcase_filename_template.format(testcase_type)), encoding='UTF-8').read()

                    testcase_output = open(self.get_localised_file(
                        "en", testcase_filename_template.format("output")), encoding='UTF-8').read()

                    test_case = TestCase(
                        number=testcase_id,
                        test_input=testcase_input,
                        expected_output=testcase_output,
                        question_type=testcase_type,
                        challenge=programming_challenge
                    )

                    required_fields = ['test_input', 'expected_output', 'question_type']

                    self.populate_translations(test_case, test_case_translations)
                    self.mark_translation_availability(test_case, required_fields=required_fields)
                    test_case.save()

                    LOG_TEMPLATE = "Added Programming Challenge Test Case: {}"
                    self.log(LOG_TEMPLATE.format(testcase_id), 2)

            if "learning-outcomes" in challenge_structure:
                learning_outcomes = challenge_structure["learning-outcomes"]
                if learning_outcomes is not None:
                    for learning_outcome_slug in learning_outcomes:
                        try:
                            learning_outcome = LearningOutcome.objects.get(
                                slug=learning_outcome_slug
                            )
                            programming_challenge.learning_outcomes.add(learning_outcome)
                        except ObjectDoesNotExist:
                            raise KeyNotFoundError(
                                self.structure_file_path,
                                learning_outcome_slug,
                                "Learning Outcome")
