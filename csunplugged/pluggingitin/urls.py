from django.conf.urls import url

from . import views

app_name = "pluggingitin"

urlpatterns = [
    url(
        r"^$",
        views.IndexView.as_view(),
        name="index"
    ),
    url(
        r"^(?P<topic_slug>[-\w]+)/$",
        views.TopicView.as_view(),
        name="topic"
    ),
    url(
        r"^(?P<topic_slug>[-\w]+)/(?P<programming_challenge_slug>[-\w]+)/$",  # noqa: E501
        views.ProgrammingChallengeView.as_view(),
        name="programming_challenge"
    ),
]
