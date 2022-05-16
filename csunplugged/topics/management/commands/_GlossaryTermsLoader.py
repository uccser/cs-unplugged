"""Custom loader for loading glossary terms."""

from os import listdir
from django.db import transaction

from utils.language_utils import get_default_language
from topics.models import GlossaryTerm
from utils.TranslatableModelLoader import TranslatableModelLoader


class GlossaryTermsLoader(TranslatableModelLoader):
    """Custom loader for loading glossary terms."""

    FILE_EXTENSION = ".md"

    @transaction.atomic
    def load(self):
        """Load the glossary content into the database."""
        glossary_slugs = set()

        for filename in listdir(self.get_localised_dir(get_default_language())):
            if filename.endswith(self.FILE_EXTENSION):
                glossary_slug = filename[:-len(self.FILE_EXTENSION)]
                glossary_slugs.add(glossary_slug)

        for glossary_slug in glossary_slugs:
            term_translations = self.get_blank_translation_dictionary()

            content_filename = "{}.md".format(glossary_slug)
            content_translations = self.get_markdown_translations(content_filename)

            for language, content in content_translations.items():
                term_translations[language]["definition"] = content.html_string
                term_translations[language]["term"] = content.title

            glossary_term, created = GlossaryTerm.objects.update_or_create(
                slug=glossary_slug,
                defaults={},
            )
            self.populate_translations(glossary_term, term_translations)
            self.mark_translation_availability(glossary_term, required_fields=["term", "definition"])
            glossary_term.save()

            if created:
                self.log(f'Added glossary term: {glossary_term}')
            else:
                self.log(f'Updated glossary term: {glossary_term}')

        self.log("All glossary terms loaded!\n")
