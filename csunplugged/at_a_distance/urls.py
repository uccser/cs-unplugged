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
    # eg: /at-a-distance/stroop-effect/
    path(
        '<slug:lesson_slug>/',
        views.LessonView.as_view(),
        name='lesson'
    ),
]
