from django.http import HttpResponse

from topics.utils.add_lesson_ages_to_objects import add_lesson_ages_to_objects
from django.views import generic
from utils.translated_first import translated_first
from topics.models import (
    Topic
)

class IndexView(generic.ListView):
    """View for the topics application homepage."""

    template_name = "pluggingitin/index.html"
    context_object_name = "topics"

    def get_queryset(self):
        """Get queryset of all topics.

        Returns:
            Queryset of Topic objects ordered by name.
        """
        topics = Topic.objects.order_by("name").prefetch_related(
            "unit_plans",
            "lessons",
            "curriculum_integrations",
            "programming_challenges",
        )
        return translated_first(topics)

    def get_context_data(self, **kwargs):
        """Provide the context data for the index view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        add_lesson_ages_to_objects(self.object_list)
        return context

def index(request):
    return HttpResponse("You are at the plugging it in home page!")
