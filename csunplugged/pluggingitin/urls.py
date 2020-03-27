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
]
