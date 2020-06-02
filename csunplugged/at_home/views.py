"""Views for the at home application."""

from django.views import generic
from at_home.models import Activity, Challenge


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


class ActivityChallengesView(generic.ListView):
    """View for challenges of a specific activity."""

    model = Challenge
    template_name = "at_home/activity_challenges.html"
    context_object_name = "challenge"
    slug_url_kwarg = "activity_slug"
    allow_empty = False

    def get_queryset(self, **kwargs):
        activity = Activity.objects.get(slug=self.kwargs['activity_slug'])
        return Challenge.objects.filter(activity=activity)

    def get_context_data(self, **kwargs):
        """Provide the context data for the activity view.

        Returns:
            Dictionary of context data.
        """
        context = super(ActivityChallengesView, self).get_context_data(**kwargs)
        activity = Activity.objects.get(slug=self.kwargs['activity_slug'])
        challenges = Challenge.objects.filter(activity=activity)
        context["activity"] = activity
        context["challenges"] = challenges
        context["challenge_answers"] = dict()
        return context
