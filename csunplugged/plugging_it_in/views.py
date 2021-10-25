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


class BlockBasedAndScratchView(generic.TemplateView):
    """View for the diferrences between the Block-based system and Scratch page that renders from a template."""

    template_name = "plugging_it_in/block-based-vs-scratch.html"


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
        ).prefetch_related('implementations', 'implementations__language')
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
            slug=self.kwargs.get("challenge_slug", None)
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
            language_slug = self.kwargs.get("language_slug", None)
            context["programming_lang"] = language_slug.lower()  # ensure /python or /block-based is lower case

            lesson_slug = self.kwargs.get("lesson_slug", None)
            lesson = Lesson.objects.get(slug=lesson_slug)
            context["lesson"] = lesson

            # Get Python or block-based challenges depending on the language_slug
            # else raise a 404 error
            if (language_slug in ["python", "block-based"]):
                challlenges = lesson.retrieve_related_programming_challenges(language_slug.capitalize())
            else:
                raise Http404("Language does not exist")

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
            # Retrieves python/blockly code for a specific question, depending what context["programming_lang"] is
            lang = context["programming_lang"]
            if language_slug == "python":
                context["previous_text_based_submission"] = context["saved_attempts"][self.object.slug][lang]["code"]
            elif language_slug == "block-based":
                context["previous_block_based_submission"] = context["saved_attempts"][self.object.slug][lang]["code"]
            else:
                return Http404("Language does not exist")
        except KeyError:
            context["previous_text_based_submission"] = ''
            context["previous_block_based_submission"] = ''

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
                 and request.session.get('saved_attempts', {})
                 .get(body["challenge"], {})
                 .get(body["programming_language"], {})
                 .get("status", "")
                 in {'passed', 'failed'})
                and body["attempt"] != ""):

            # if attempting the current challenge for the first time,
            # initialise the challenge as an empty object to avoid KeyError when saving user's attempt
            if (body["challenge"] not in request.session['saved_attempts']):
                request.session['saved_attempts'][body["challenge"]] = {}

            # Saves the python/block-based attempt in different places for the current challenge
            request.session['saved_attempts'][body["challenge"]][body["programming_language"]] = {
                "status": body["status"],
                "code": body["attempt"],
            }
            # Set session as modified to force data updates to be saved
            # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions
            request.session.modified = True
            return HttpResponse("Saved the attempt.")
        else:
            return HttpResponse("Response does not need to be saved.")
