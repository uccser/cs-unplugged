"""Module for checking glossary links found within Markdown conversions."""

from django.core.exceptions import DoesNotExist
from utils.errors.CouldNotFindGlossaryTerm import CouldNotFindGlossaryTerm
from topics.models import GlossaryTerm


def check_converter_glossary_links(glossary_links, md_file_path):
    """Process glossary links found by Markdown converter.

    Args:
        glossary_links: Dictionary of glossary links (dict).
    """
    for term in glossary_links.keys():
        try:
            GlossaryTerm.objects.get(slug=term)
        except DoesNotExist:
            raise CouldNotFindGlossaryTerm(term, md_file_path)
