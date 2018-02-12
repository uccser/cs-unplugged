"""Module for the overriden Django Haystack rebuild_index command."""

from haystack.management.commands import rebuild_index
from haystack.query import SearchQuerySet
from search.forms import all_items
from resources.models import Resource
from classic.models import ClassicPage
from topics.models import (
    Topic,
    UnitPlan,
    Lesson,
    ProgrammingChallenge,
    CurriculumIntegration,
)


class Command(rebuild_index.Command):
    """Command class for the custom Django rebuild_index command."""

    help = "Rebuild search index and check empty query returns all items."

    def handle(self, *args, **options):
        """Automatically called when the rebuild_index command is given."""
        total_objects = Resource.objects.count()
        total_objects += Topic.objects.count()
        total_objects += UnitPlan.objects.count()
        total_objects += Lesson.objects.count()
        total_objects += ProgrammingChallenge.objects.count()
        total_objects += CurriculumIntegration.objects.count()
        total_objects += ClassicPage.objects.count()
        super(Command, self).handle(*args, **options)
        total_results = len(all_items(SearchQuerySet()))
        if total_objects == total_results:
            print("Search index loaded.")
        else:   # pragma: no cover
            raise Exception("Search all_items() method does not return all items.")
