"""URL redirect routing for the at a distance section of the CS Unplugged website."""

from django.urls import path
from at_a_distance import views

app_name = 'at_a_distance'
urlpatterns = [
    # eg: /at-a-distance/
    path(
        '',
        views.IndexView.as_view(),
        name='index'
    ),
    # eg: /at-a-distance/how-to-teach/
    path(
        'delivery-guide/',
        views.DeliveryGuideView.as_view(),
        name='delivery-guide'
    ),
    # eg: /at-a-distance/speaker-notes/
    path(
        'speaker-notes/',
        views.LessonSlideSpeakerNotesView.as_view(),
        name='speaker-notes'
    ),
    path(
        "slides-file-generation-json/",
        views.slides_file_generation_json,
        name='slides_file_generation_json'
    ),
    # eg: /at-a-distance/stroop-effect/
    path(
        '<slug:lesson_slug>/',
        views.LessonView.as_view(),
        name='lesson'
    ),
    # eg: /at-a-distance/stroop-effect/slides/
    path(
        '<slug:lesson_slug>/slides/',
        views.LessonSlidesView.as_view(),
        name='lesson_slides'
    ),
    # eg: /at-a-distance/stroop-effect/slides/
    path(
        '<slug:lesson_slug>/slides-file-generation/',
        views.LessonFileGenerationView.as_view(),
        name='lesson_file_generation'
    ),
]
