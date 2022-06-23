"""Views for the at a distance application."""

import json
from django.views import generic
from at_a_distance.models import Lesson


class IndexView(generic.ListView):
    """View for the at a distance application homepage."""

    template_name = "at_a_distance/index.html"
    model = Lesson
    context_object_name = "lessons"


class LessonView(generic.DetailView):
    """View for a specific lesson."""

    model = Lesson
    template_name = "at_a_distance/lesson.html"
    context_object_name = "lesson"
    slug_url_kwarg = "lesson_slug"


class LessonSlidesView(generic.DetailView):
    """View for a specific lesson's slides."""

    model = Lesson
    template_name = "at_a_distance/lesson-slides.html"
    context_object_name = "lesson"
    slug_url_kwarg = "lesson_slug"


class LessonSlideSpeakerNotesView(generic.TemplateView):
    """View for speaker notes window."""

    template_name = "at_a_distance/reveal-speaker-notes-plugin/speaker-notes-window.html"
