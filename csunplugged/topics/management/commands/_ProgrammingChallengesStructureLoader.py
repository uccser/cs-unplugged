"""Custom loader for loading structure of programming challenges."""

from django.db import transaction
from django.utils import translation
from utils.BaseLoader import BaseLoader
from utils.language_utils import get_available_languages, get_default_language
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import ProgrammingChallengeLanguage, ProgrammingChallengeDifficulty


class ProgrammingChallengesStructureLoader(BaseLoader):
    """Custom loader for loading structure of programming challenges."""

    def __init__(self, **kwargs):
        """Create the loader for loading structure of programming challenges."""
        super().__init__(**kwargs)

    @transaction.atomic
    def load(self):
        """Load the content for structure of programming challenges.

        Raises:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        structure = self.load_yaml_file(self.structure_file_path)
        translation_strings = {}
        prog_language_translation_strings = {}
        difficulties_translation_strings = {}
        for language in get_available_languages():
            try:
                strings_dict = self.load_yaml_file(
                    self.get_localised_file(language, "programming-challenges-structure-strings.yaml")
                )
            except:
                strings_dict = {}
            translation_strings[language] = strings_dict
            # prog_language_translation_strings.setdefault()
            # prog_language_translation_strings[language] = strings_dict.get("languages", dict())
            # difficulties_translation_strings[language] = strings_dict.get("difficulties", dict())

        prog_languages = structure.get("languages", None)
        difficulty_levels = structure.get("difficulties", None)
        if None in [prog_languages, difficulty_levels]:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ["lanugages", "difficulties"],
                "Programming Challenge Structure"
            )

        for (prog_language, prog_language_data) in prog_languages.items():

            if prog_language_data is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["name", "number"],
                    "Programming Challenge Language"
                )

            # Check for required fields
            prog_language_name = prog_language_data.get("name", None)
            prog_language_number = prog_language_data.get("number", None)
            if prog_language_name is None or prog_language_number is None:
                raise MissingRequiredFieldError(
                    self.structure_file_path,
                    ["name", "number"],
                    "Programming Challenge Language"
                )

            # Check if icon is given
            if "icon" in prog_language_data:
                prog_language_icon = prog_language_data["icon"]
            else:
                prog_language_icon = None

            new_prog_language = ProgrammingChallengeLanguage(
                slug=prog_language,
                # name=prog_language_name,
                number=prog_language_number,
                icon=prog_language_icon
            )
            for language in translation_strings:
                name = translation_strings[language].get("languages", {}).get(prog_language)
                if name:
                    with translation.override(language):
                        new_prog_language.name = name
                    new_prog_language.languages.append(language)
            new_prog_language.save()

            self.log("Added programming langauge: {}".format(new_prog_language.__str__()))

        for difficulty in difficulty_levels:

            # if difficulty_data is None:
            #     raise MissingRequiredFieldError(
            #         self.structure_file_path,
            #         ["name"],
            #         "Programming Challenge Difficulty"
            #     )

            # difficulty_name = difficulty_data.get("name", None)
            # if difficulty_name is None:
            #     raise MissingRequiredFieldError(
            #         self.structure_file_path,
            #         ["name"],
            #         "Programming Challenge Difficulty"
            #     )

            new_difficulty = ProgrammingChallengeDifficulty(
                level=difficulty,
                # name=difficulty_name
            )
            for language in translation_strings:
                name = translation_strings[language].get("difficulties", {}).get(difficulty)
                if name:
                    with translation.override(language):
                        new_difficulty.name = name
                    new_difficulty.languages.append(language)
            new_difficulty.save()

            self.log("Added programming difficulty level: {}".format(new_difficulty.__str__()))

        self.log("")
