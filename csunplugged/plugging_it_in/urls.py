"""URL routing for the plugging_it_in application."""

from django.urls import path, re_path
from . import views

app_name = "plugging_it_in"

urlpatterns = [
    re_path(
        r"^$",
        views.IndexView.as_view(),
        name="index"
    ),
    path(
        'about/',
        views.AboutView.as_view(),
        name="about"
    ),
    path(
        'block-based-vs-scratch/',
        views.BlockBasedAndScratchView.as_view(),
        name="block_based_vs_scratch"
    ),
    re_path(
        r"^(?P<topic_slug>[-\w]+)/(?P<lesson_slug>[-\w]+)/$",
        views.ProgrammingChallengeListView.as_view(),
        name="lesson"
    ),
    re_path(
        r"^(?P<topic_slug>[-\w]+)/(?P<lesson_slug>[-\w]+)/(?P<challenge_slug>[-\w]+)/(?P<language_slug>[-\w]+)/$",
        views.ProgrammingChallengeView.as_view(),
        name="programming_challenge"
    ),
    re_path(
        r"^jobe_proxy$",
        views.JobeProxyView.as_view(),
        name="jobe_proxy"
    ),
    re_path(
        r"^save_attempt$",
        views.SaveAttemptView.as_view(),
        name="save_attempt"
    ),
]
