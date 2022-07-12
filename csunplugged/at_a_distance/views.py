"""Views for the at a distance application."""

import os.path
from django.views import generic
from django.conf import settings
from django.http import JsonResponse
from django.utils.translation import get_language
from at_a_distance.models import Lesson
from at_a_distance.settings import AT_A_DISTANCE_SLIDE_RESOLUTION
from at_a_distance.utils import get_slide_lengths


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

    def get_context_data(self, **kwargs):
        """Provide the context data for the index view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['slides_pdf'] = os.path.join(
            "slides",
            get_language(),
            self.object.slug,
            f"{self.object.slug}-slides.pdf"
        )
        context['notes_pdf'] = os.path.join(
            "slides",
            get_language(),
            self.object.slug,
            f"{self.object.slug}-speaker-notes.pdf"
        )
        return context


class LessonSlidesView(generic.DetailView):
    """View for a specific lesson's slides."""

    model = Lesson
    template_name = "at_a_distance/lesson-slides.html"
    context_object_name = "lesson"
    slug_url_kwarg = "lesson_slug"


class LessonFileGenerationView(generic.DetailView):
    """View for generating a specific lesson's files."""

    model = Lesson
    template_name = "at_a_distance/lesson-slides.html"
    context_object_name = "lesson"
    slug_url_kwarg = "lesson_slug"

    def get_context_data(self, **kwargs):
        """Provide the context data for the index view.

        Returns:
            Dictionary of context data.
        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['fragments'] = 'false'
        context['slide_number'] = 'false'
        return context


class LessonSlideSpeakerNotesView(generic.TemplateView):
    """View for speaker notes window."""

    template_name = "at_a_distance/reveal-speaker-notes-plugin/speaker-notes-window.html"


def slides_file_generation_json(request, **kwargs):
    """Provide JSON data for creating thumbnails.

    Args:
        request: The HTTP request.

    Returns:
        JSON response is sent containing data for thumbnails.
    """
    data = dict()

    if request.GET.get("language", False) == "all":
        languages = settings.DEFAULT_LANGUAGES
    elif request.GET.get("language", False):
        languages = [(request.GET.get("language"), "")]
    else:
        languages = [("en", "")]

    lesson_slugs = list(Lesson.objects.values_list('slug', flat=True))

    # For each language{}
    data["languages"] = dict()
    for language_code, _ in languages:
        data["languages"][language_code] = lesson_slugs

    # Other values
    data["resolution"] = AT_A_DISTANCE_SLIDE_RESOLUTION
    data["slide_counts"] = get_slide_lengths()

    return JsonResponse(data, safe=False)
