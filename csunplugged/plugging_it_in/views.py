"""Views for the plugging_it_in application."""

from django.http import HttpResponse

import json
import requests

from django.shortcuts import get_object_or_404
from django.views import generic
from django.views import View
from django.urls import reverse
from django.conf import settings
from topics.utils.add_lesson_ages_to_objects import add_lesson_ages_to_objects
from utils.translated_first import translated_first
from utils.group_lessons_by_age import group_lessons_by_age
from topics.models import (
    Topic,
    ProgrammingChallenge,
    UnitPlan,
    Lesson
)


class IndexView(generic.ListView):
    """View for the topics application homepage."""

    template_name = "plugging_it_in/index.html"
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

        # Add in a QuerySet of all the demo programming exercises (Temporary)
        demo_challenge_ids = {1, 4, 8, 13, 15, 20}
        context["demo_programming_challenges"] = ProgrammingChallenge.objects.filter(id__in=demo_challenge_ids)
        return context


class LessonsView(generic.DetailView):
    """View of lessons with programming exercises for a particular topic."""

    model = UnitPlan
    template_name = "plugging_it_in/topic.html"
    slug_url_kwarg = "topic_slug"
    context_object_name = "topic"

    def get_object(self, **kwargs):
        """Retrieve object for the lessons view.

        Returns:
            UnitPlan object with lessons, or raises 404 error if not found.
        """
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get("topic_slug", None)
        )

    def get_context_data(self, **kwargs):
        """Provide the context data for the lessons view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(LessonsView, self).get_context_data(**kwargs)
        # Loading object under consistent context names for breadcrumbs
        context["topic"] = self.object.topic
        # Add all the connected lessons
        context["grouped_lessons"] = group_lessons_by_age(self.object.lessons.all(), only_programming_exercises=True)
        return context


class ProgrammingChallengeListView(generic.DetailView):
    """View showing all the programming exercises for a specific lesson."""

    model = Lesson
    template_name = "plugging_it_in/lesson.html"
    slug_url_kwarg = "lesson_slug"

    def get_context_data(self, **kwargs):
        """Provide the context data for the programming challenge list view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(ProgrammingChallengeListView, self).get_context_data(**kwargs)

        context["topic"] = self.object.topic

        context["lesson"] = self.object

        # Add in a QuerySet of all the connected programming exercises for this topic
        context["programming_challenges"] = self.object.retrieve_related_programming_challenges()
        return context


class ProgrammingChallengeView(generic.DetailView):
    """View for a specific programming challenge."""

    model = ProgrammingChallenge
    template_name = "plugging_it_in/programming-challenge.html"
    context_object_name = "programming_challenge"

    def get_object(self, **kwargs):
        """Retrieve object for the programming challenge view.

        Returns:
            ProgrammingChallenge object, or raises 404 error if not found.
        """
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get("topic_slug", None),
            slug=self.kwargs.get("programming_challenge_slug", None)
        )

    def get_context_data(self, **kwargs):
        """Provide the context data for the programming challenge view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(ProgrammingChallengeView, self).get_context_data(**kwargs)

        context["topic"] = self.object.topic
        lessons = self.object.lessons.all()
        for lesson in lessons:
            if lesson.slug == self.kwargs.get("lesson_slug", None):
                context["lesson"] = lesson
                context["programming_challenges"] = lesson.retrieve_related_programming_challenges("Python")
                context["programming_exercises_json"] = json.dumps(
                    list(lesson.retrieve_related_programming_challenges("Python").values()))

        context["implementations"] = self.object.ordered_implementations()
        context["test_cases_json"] = json.dumps(list(self.object.related_test_cases().values()))
        context["test_cases"] = self.object.related_test_cases().values()
        context["jobe_proxy_url"] = reverse('plugging_it_in:jobe_proxy')
        context["saved_attempts"] = self.request.session.get('saved_attempts', {})

        return context


class JobeProxyView(View):
    """Proxy for Jobe Server."""

    def post(self, request, *args, **kwargs):
        """Forward on request to Jobe from the frontend and adds API key if this is needed.

        Returns:
            The response from the Jobe server.
        """
        # Extracting data from the request body
        body_unicode = request.body.decode('utf-8')
        body = json.dumps(json.loads(body_unicode))

        headers = {"Content-type": "application/json; charset=utf-8",
                   "Accept": "application/json"}

        # Set API key for production
        if hasattr(settings, 'JOBE_API_KEY'):
            headers["X-API-KEY"] = settings.JOBE_API_KEY

        response = requests.post(settings.JOBE_SERVER_URL + "/jobe/index.php/restapi/runs/",
                                 data=body, headers=headers)
        return HttpResponse(response.text)


class SaveAttemptView(View):
    """View to save the users challenge attempt."""

    def post(self, request):
        """Save the users attempt to a Django session."""
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        request.session['saved_attempts'] = request.session.get('saved_attempts', {})
        request.session['saved_attempts'][body["challenge"]] = body["attempt"]

        return HttpResponse("Saved the attempt.")
