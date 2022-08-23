"""Module for the custom Django rebuild_search_indexes command."""

from django.core import management
from django.db import transaction
from search.utils import get_search_index_updater
from search.settings import SEARCH_CLASSES_AND_BOOSTS


class Command(management.base.BaseCommand):
    """Required command class for the custom Django rebuild_search_indexes command."""

    help = "Rebuild search indexes in database."

    def handle(self, *args, **options):
        """Automatically called when the command is given."""
        for model_data in SEARCH_CLASSES_AND_BOOSTS:
            model = model_data['class']
            for instance in model.objects.all():
                transaction.on_commit(get_search_index_updater(instance))
