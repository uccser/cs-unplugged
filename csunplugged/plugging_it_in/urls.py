"""URL routing for the plugging_it_in application."""

from django.urls import path
from django.conf.urls import url
from . import views

app_name = "plugging_it_in"

urlpatterns = [
    url(
        r"^$",
        views.IndexView.as_view(),
        name="index"
    ),
    path(
        'about/',
        views.AboutView.as_view(),
        name="about"
    ),
    url(
        r"^(?P<topic_slug>[-\w]+)/(?P<lesson_slug>[-\w]+)/$",
        views.ProgrammingChallengeListView.as_view(),
        name="lesson"
    ),
    url(
        r"^(?P<topic_slug>[-\w]+)/(?P<lesson_slug>[-\w]+)/(?P<programming_challenge_slug>[-\w]+)/$",
        views.ProgrammingChallengeView.as_view(),
        name="programming_challenge"
    ),
    url(
        r"^jobe_proxy$",
        views.JobeProxyView.as_view(),
        name="jobe_proxy"
    ),
    url(
        r"^save_attempt$",
        views.SaveAttemptView.as_view(),
        name="save_attempt"
    ),
]
