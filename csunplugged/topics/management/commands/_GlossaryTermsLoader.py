"""Custom loader for loading glossary terms."""

from os import listdir
from django.db import transaction

from utils.BaseLoader import BaseLoader
from utils.language_utils import get_available_languages, get_default_language
from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from topics.models import GlossaryTerm


class GlossaryTermsLoader(BaseLoader):
    """Custom loader for loading glossary terms."""

    def __init__(self, **kwargs):
        """Create the loader for loading glossary terms."""
        super().__init__(**kwargs)
        self.FILE_EXTENSION = ".md"

    @transaction.atomic
    def load(self):
        """Load the glossary content into the database."""
        glossary_slugs = set()
        for filename in listdir(self.get_localised_dir(get_default_language())):
            if filename.endswith(self.FILE_EXTENSION):
                glossary_slug = filename[:-len(self.FILE_EXTENSION)]
                glossary_slugs.add(glossary_slug)
                glossary_term = GlossaryTerm(
                    slug=glossary_slug,
                )
                glossary_term.save()

        for glossary_slug in glossary_slugs:
            content_translations = {}
            for language in get_available_languages():
                glossary_term = GlossaryTerm.objects.get(slug=glossary_slug)
                glossary_file_path = self.get_localised_file(
                    language,
                    "{}{}".format(glossary_slug, self.FILE_EXTENSION)
                )
                try:
                    glossary_term_content = self.convert_md_file(
                        glossary_file_path,
                        self.structure_file_path
                    )
                    content_translations[language] = glossary_term_content
                except CouldNotFindMarkdownFileError:
                    if language == get_default_language():
                        raise

            for language in content_translations:
                setattr(glossary_term, "definition_{}".format(language), content_translations[language].html_string)
                setattr(glossary_term, "term_{}".format(language), content_translations[language].title)
                glossary_term.languages.append(language)
            glossary_term.save()
            self.log("Added glossary term: {}".format(glossary_term.__str__()))

        self.log("All glossary terms loaded!\n")
