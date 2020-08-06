"""URL routing for the plugging_it_in application."""

from django.conf.urls import url

from . import views

app_name = "plugging_it_in"

urlpatterns = [
    url(
        r"^$",
        views.IndexView.as_view(),
        name="index"
    ),
    url(
        r"^(?P<topic_slug>[-\w]+)/$",
        views.LessonsView.as_view(),
        name="topic"
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
]
