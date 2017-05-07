"""Custom loader for loading glossary terms."""

import os.path
from os import listdir
from django.db import transaction

from utils.BaseLoader import BaseLoader
from topics.models import GlossaryTerm


class GlossaryTermsLoader(BaseLoader):
    """Custom loader for loading glossary terms."""

    def __init__(self, glossary_folder_path, structure_file_path, BASE_PATH):
        """Create the loader for loading glossary terms.

        Args:
            glossary_folder_path: Folder path to definition files (string).
            structure_file_path: Path to the config file, used for errors.
            BASE_PATH: Base file path (string).
        """
        super().__init__(BASE_PATH)
        self.structure_file_path = structure_file_path
        self.BASE_PATH = os.path.join(self.BASE_PATH, glossary_folder_path)
        self.FILE_EXTENSION = ".md"

    @transaction.atomic
    def load(self):
        """Load the glossary content into the database."""
        glossary_slugs = set()
        for filename in listdir(self.BASE_PATH):
            if filename.endswith(self.FILE_EXTENSION):
                glossary_slug = filename[:-len(self.FILE_EXTENSION)]
                glossary_slugs.add(glossary_slug)
                glossary_term = GlossaryTerm(
                    slug=glossary_slug,
                )
                glossary_term.save()

        for glossary_slug in glossary_slugs:
                glossary_term = GlossaryTerm.objects.get(slug=glossary_slug)
                glossary_file_path = os.path.join(
                    self.BASE_PATH,
                    glossary_slug + self.FILE_EXTENSION
                )
                glossary_term_content = self.convert_md_file(
                    glossary_file_path,
                    self.structure_file_path
                )
                glossary_term.term = glossary_term_content.title
                glossary_term.definition = glossary_term_content.html_string
                glossary_term.save()
                self.log("Added Glossary Term: {}".format(glossary_term.__str__()))

        # Print log output
        self.print_load_log()
