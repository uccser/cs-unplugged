"""Views for the at home application."""

from django.views import generic
from at_home.models import Activity


class IndexView(generic.ListView):
    """View for the at home application homepage."""

    template_name = "at_home/index.html"
    model = Activity
    context_object_name = "activities"


class ActivityView(generic.DetailView):
    """View for a specific activity."""

    model = Activity
    template_name = "at_home/activity.html"
    context_object_name = "activity"
    slug_url_kwarg = "activity_slug"
