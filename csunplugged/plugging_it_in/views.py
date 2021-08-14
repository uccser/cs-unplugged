"""Views for the plugging_it_in application."""

from django.http import HttpResponse
from django.http import Http404

import json
import requests

from django.shortcuts import get_object_or_404
from django.views import generic
from django.views import View
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from utils.translated_first import translated_first
from utils.group_lessons_by_age import group_lessons_by_age

from topics.models import (
    Topic,
    ProgrammingChallenge,
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
        programming_topics = Topic.objects.order_by(
            "name"
        ).exclude(
            programming_challenges__isnull=True
        ).prefetch_related(
            "programming_challenges",
            "lessons",
        )
        return translated_first(programming_topics)

    def get_context_data(self, **kwargs):
        """Provide the context data for the index view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        for topic in self.object_list:
            topic.grouped_lessons = group_lessons_by_age(
                topic.lessons.all(),
                only_programming_exercises=True
            )
        return context


class AboutView(generic.TemplateView):
    """View for the about page that renders from a template."""

    template_name = "plugging_it_in/about.html"


class ProgrammingChallengeListView(generic.DetailView):
    """View showing all the programming exercises for a specific lesson."""

    model = Lesson
    template_name = "plugging_it_in/lesson.html"

    def get_object(self, **kwargs):
        """Retrieve object for the lesson view.

        Returns:
            Lesson object, or raises 404 error if not found.
        """
        return get_object_or_404(
            self.model.objects.select_related(),
            topic__slug=self.kwargs.get("topic_slug", None),
            slug=self.kwargs.get("lesson_slug", None),
        )

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
        context["programming_challenges"] = self.object.retrieve_related_programming_challenges(
        ).prefetch_related('implementations')
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

        try:
            programming_lang_slug = self.kwargs.get("programming_lang_slug", None)
            context["programming_lang"] = programming_lang_slug.lower() # make sure the /python or /block-based is lower case, because this will get checked in the programming.

            lesson_slug = self.kwargs.get("lesson_slug", None)
            lesson = Lesson.objects.get(slug=lesson_slug)
            context["lesson"] = lesson
            
            # Get Python challenges if programming_lang_slug == 'python' else get Block-based challanges
            if (programming_lang_slug == "python"):
                challlenges = lesson.retrieve_related_programming_challenges("Python")
            else:
                challlenges = lesson.retrieve_related_programming_challenges("Block-based")

            context["programming_challenges"] = challlenges
            context["programming_exercises_json"] = json.dumps(list(challlenges.values()))
        except ObjectDoesNotExist:
            raise Http404("Lesson does not exist")

        context["implementations"] = self.object.ordered_implementations()

        related_test_cases = self.object.related_test_cases()
        context["test_cases_json"] = json.dumps(list(related_test_cases.values()))
        context["test_cases"] = related_test_cases
        context["jobe_proxy_url"] = reverse('plugging_it_in:jobe_proxy')
        context["saved_attempts"] = self.request.session.get('saved_attempts', {})
        try:
            # Retrieves either the python or blockly code for a specific question, depending what the value of context["programming_lang"] is
            context["previous_submission"] = context["saved_attempts"][self.object.slug][context["programming_lang"]]['code']
        except KeyError:
            context["previous_submission"] = ''

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

        headers = {
            "Content-type": "application/json; charset=utf-8",
            "Accept": "application/json",
        }

        response = requests.post(
            settings.JOBE_SERVER_URL + "/jobe/index.php/restapi/runs/",
            data=body,
            headers=headers,
        )
        return HttpResponse(response.text)


class SaveAttemptView(View):
    """View to save the users challenge attempt."""

    def post(self, request):
        """Save the users attempt to a Django session."""
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        request.session['saved_attempts'] = request.session.get('saved_attempts', {})

        # To stop a "passed" or "failed" status being overridden by "started"
        if (not (body["status"] == "started"
                 and request.session.get('saved_attempts', {}).get(body["challenge"], {}).get("status", "")
                 in {'passed', 'failed'})
                and body["attempt"] != ""):
            # Saves the python attempt and blockly attempt in different places for the same question.
            request.session['saved_attempts'][body["challenge"]][body["programming_language"]] = {
                "status": body["status"],
                "code": body["attempt"],
                "programming_language": body["programming_language"]
            }
            return HttpResponse("Saved the attempt.")
        else:
            return HttpResponse("Response does not need to be saved.")
