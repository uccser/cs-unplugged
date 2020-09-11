"""Custom loader for loading structure of programming challenges."""

import os
from django.db import transaction
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.TranslatableModelLoader import TranslatableModelLoader
from topics.models import ProgrammingChallengeLanguage, ProgrammingChallengeDifficulty


class ProgrammingChallengesStructureLoader(TranslatableModelLoader):
    """Custom loader for loading structure of programming challenges."""

    @transaction.atomic
    def load(self):
        """Load the content for structure of programming challenges.

        Raises:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        structure = self.load_yaml_file(self.structure_file_path)

        prog_languages = structure.get("languages", None)
        difficulty_levels = structure.get("difficulties", None)
        if None in [prog_languages, difficulty_levels]:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ["lanugages", "difficulties"],
                "Programming Challenge Structure"
            )

        # Add "-languages" to the structure filename
        prog_languages_translation_filename = "{}-languages.yaml".format(
            os.path.splitext(self.structure_filename)[0]
        )
        prog_languages_translations = self.get_yaml_translations(
            prog_languages_translation_filename,
            required_slugs=prog_languages.keys(),
            required_fields=["name"]
        )

        for (prog_language, prog_language_data) in prog_languages.items():

            if prog_language_data is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["number"],
                    "Programming Challenge Language"
                )

            # Check for required fields
            prog_language_number = prog_language_data.get("number", None)
            if prog_language_number is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["number"],
                    "Programming Challenge Language"
                )

            # Check if icon is given
            if "icon" in prog_language_data:
                prog_language_icon = prog_language_data["icon"]
            else:
                prog_language_icon = None

            if prog_language == "python":
                prog_reminders_filename = "programming-reminders-{0}.md".format(prog_language)
                prog_reminders_filepath = os.path.abspath(
                   "plugging_it_in/content/en/programming-reminders/" + prog_reminders_filename
                )
                programming_reminders_translations = self.get_markdown_translations(
                    prog_reminders_filepath
                )
                for language, content in programming_reminders_translations.items():
                    prog_languages_translations[language]["programming_reminders"] = content.html_string

            new_prog_language = ProgrammingChallengeLanguage(
                slug=prog_language,
                number=prog_language_number,
                icon=prog_language_icon
            )

            translations = prog_languages_translations.get(prog_language, dict())
            self.populate_translations(new_prog_language, translations)
            self.mark_translation_availability(new_prog_language, required_fields=["name"])
            new_prog_language.save()

            self.log("Added programming language: {}".format(new_prog_language.__str__()))

        # Add "-languages" to the structure filename
        difficulties_translation_filename = "{}-difficulties.yaml".format(
            os.path.splitext(self.structure_filename)[0]
        )
        difficulties_translations = self.get_yaml_translations(
            difficulties_translation_filename,
            required_slugs=difficulty_levels,
            required_fields=["name"],
        )

        for level, difficulty_slug in enumerate(difficulty_levels):

            new_difficulty = ProgrammingChallengeDifficulty(
                level=level,
            )

            translations = difficulties_translations.get(difficulty_slug, dict())
            self.populate_translations(new_difficulty, translations)
            self.mark_translation_availability(new_difficulty, required_fields=["name"])
            new_difficulty.save()

            self.log("Added programming difficulty level: {}".format(new_difficulty.__str__()))

        self.log("")
