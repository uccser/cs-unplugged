from utils.BaseLoader import BaseLoader
from utils.language_utils import get_available_languages, get_default_language
from utils.errors.CouldNotFindConfigFileError import CouldNotFindConfigFileError
from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from django.utils import translation
from modeltranslation.utils import fallbacks



class TranslatableModelLoader(BaseLoader):
    def get_yaml_translations(self, filename, field_map=None, required=True):
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
                            field,
                            "???."
                        )
                    if field_map:
                        field = field_map.get(field, field)
                    values_dict[field] = value
                translations.setdefault(model_slug, dict())[language] = values_dict
        return translations

    def get_markdown_translations(self, filename, required=True, **kwargs):
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
        """ Model strings of form {
            lang: { param_name: value1, param2: value }
        }
        """
        for language, values_dict in model_translations_dict.items():
            with translation.override(language):
                for field, value in values_dict.items():
                    setattr(model, field, value)

    def mark_translation_availability(self, model, required_fields=[]):
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
        return { language: dict() for language in get_available_languages() }
