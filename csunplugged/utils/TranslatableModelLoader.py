"""Module for TranslatableModelLoader abstract base class."""

from utils.BaseLoader import BaseLoader
from utils.language_utils import get_available_languages, get_default_language
from utils.errors.CouldNotFindConfigFileError import CouldNotFindConfigFileError
from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from utils.errors.InvalidConfigValueError import InvalidConfigValueError
from django.utils import translation
from modeltranslation.utils import fallbacks


class TranslatableModelLoader(BaseLoader):
    """Abstract base class for loaders of translatable models."""

    def get_yaml_translations(self, filename, field_map=None, required=True):
        """Get a dictionary of translations for the given filename.

        Yaml files must be structured as follows:
            <object-slug>:
                <field>: <translated value for field 2>
                <field2>: <translated value for field 2>
            <object-slug-2>
                ...

        Args:
            filename: (str) path to yaml file from the working directory of the loader
            field_map: (dict) optional mapping of field names in yaml file to
                field names in the resulting dictionary
            required: (bool) if true, an exception is raised if the file is not
                present in the English directory

        Returns:
            Dictonary of translations, structured as follows:
                {
                    <model-slug>: {
                        <language>: {
                            <field-name>:<value>
                        }
                    }
                }

        Raises:
            CouldNotFindConfigFileError: the requested file could not be found in
                the /en directory, raised only if required=True.
            InvalidConfigValueError: one of the 'translated strings' in the file
                was not a string.
        """
        translations = {}
        for language in get_available_languages():
            translations_filename = self.get_localised_file(language, filename)
            try:
                yaml = self.load_yaml_file(translations_filename)
            except CouldNotFindConfigFileError:
                if required and language == get_default_language():
                    raise
                yaml = {}
            for model_slug, model_fields in yaml.items():
                values_dict = {}
                for field, value in model_fields.items():
                    if not isinstance(value, str):
                        raise InvalidConfigValueError(
                            filename,
                            '{}->{}'.format(model_slug, field),
                            "String"
                        )
                    if field_map:
                        field = field_map.get(field, field)
                    values_dict[field] = value
                translations.setdefault(model_slug, dict())[language] = values_dict
        return translations

    def get_markdown_translations(self, filename, required=True, **kwargs):
        """Get dictionary of translations of the requested markdown file.

        Args:
            filename: (str) path to yaml file from the working directory of the loader
            required: (bool) raise an exception if the requested file is not present
                in the /en directory tree
            kwargs: (dict) kwargs passed through to convert_md_file

        Returns:
            dict mapping language codes to VertoResult objects

        Raises:
            CouldNotFindMarkdownFileError if the requested file could not be found
                in the /en directory tree
        """
        content_translations = {}
        for language in get_available_languages():
            try:
                content_translations[language] = self.convert_md_file(
                    self.get_localised_file(
                        language,
                        filename,
                    ),
                    self.structure_file_path,
                    **kwargs
                )
            except CouldNotFindMarkdownFileError:
                if required and language == get_default_language():
                    raise
        return content_translations

    def populate_translations(self, model, model_translations_dict):
        """Populate the translation fields of the given model.

        Args:
            model: TranslatableModel instance
            model_translations_dict: dictionary of form
                {
                    <language_code>: {
                        <field_name>:<value>,
                        <field_name>:<value>,...
                    },...
                }
        """
        for language, values_dict in model_translations_dict.items():
            with translation.override(language):
                for field, value in values_dict.items():
                    setattr(model, field, value)

    def mark_translation_availability(self, model, required_fields=[]):
        """Populate the available_languages field of a translatable model.

        Args:
            model: TranslatableModel instance
            required_fields: (list) list of field names that are required to be
                populated for the model to be considered available in that language.
        """
        available_languages = []
        for language in get_available_languages():
            with translation.override(language):
                with fallbacks(False):
                    if all(
                        [getattr(model, field) for field in required_fields]
                    ):
                        available_languages.append(language)
        model.languages = available_languages

    def get_blank_translation_dictionary(self):
        """Return a dictionary of blank dictionaries, keyed by all available language."""
        return {language: dict() for language in get_available_languages()}
