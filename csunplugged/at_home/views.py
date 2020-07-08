"""Views for the at home application."""

import json
from django.views import generic
from django.http import JsonResponse
from django.utils.translation import get_language
from django.shortcuts import get_object_or_404
from at_home.models import (
    Activity,
    Challenge,
    ChallengeSubmission,
)


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
    context_object_name = "challenges"
    allow_empty = False

    def get_queryset(self, **kwargs):
        """Return the queryset for the challenges view.

        Returns:
            Queryset of Challenge objects.
        """
        self.activity = Activity.objects.get(slug=self.kwargs['activity_slug'])
        return Challenge.objects.filter(activity=self.activity)

    def get_context_data(self, **kwargs):
        """Provide the context data for the activity view.

        Returns:
            Dictionary of context data.
        """
        context = super(ActivityChallengesView, self).get_context_data(**kwargs)
        context["activity"] = self.activity
        return context


def save_challenge_attempt(request):
    """Save challenge attempt for a question.

    Args:
        request (Request): AJAX request from user.

    Returns:
        JSON response with result.
    """
    result = {
        'success': False,
    }
    if request.is_ajax():
        request_json = json.loads(request.body.decode('utf-8'))
        activity_slug = request_json['activity_slug']
        challenge_number = request_json['challenge_number']
        answer = request_json['answer']
        correct = request_json['correct']
        language = get_language()

        challenge = get_object_or_404(
            Challenge,
            order_number=challenge_number,
            activity__slug=activity_slug,
        )
        ChallengeSubmission.objects.create(
            challenge=challenge,
            language=language,
            answer=answer,
            correct=correct,
        )
        result['success'] = True
    return JsonResponse(result)
