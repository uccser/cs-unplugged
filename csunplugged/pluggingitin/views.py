from django.http import HttpResponse

from topics.utils.add_lesson_ages_to_objects import add_lesson_ages_to_objects
from django.views import generic
from utils.translated_first import translated_first
from topics.models import (
    Topic,
    ProgrammingChallenge
)

class IndexView(generic.ListView):
    """View for the topics application homepage."""

    template_name = "pluggingitin/index.html"
    context_object_name = "programming_topics"

    def get_queryset(self):
        """Get queryset of all topics.

        Returns:
            Queryset of Topic objects ordered by name.
        """
        programming_topics = Topic.objects.order_by("name").prefetch_related(
            "programming_challenges",
        )
        return translated_first(programming_topics)

    def get_context_data(self, **kwargs):
        """Provide the context data for the index view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        add_lesson_ages_to_objects(self.object_list)
        return context


class TopicView(generic.DetailView):
    """View for a specific topic."""

    model = Topic
    template_name = "pluggingitin/topic.html"
    slug_url_kwarg = "topic_slug"

    def get_context_data(self, **kwargs):
        """Provide the context data for the topic view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(TopicView, self).get_context_data(**kwargs)

        # Add in a QuerySet of all the connected programming exercises for this topic
        context["programming_challenges"] = ProgrammingChallenge.objects.filter(topic=self.object)
        return context

