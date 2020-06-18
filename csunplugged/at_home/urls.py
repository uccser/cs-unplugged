"""URL redirect routing for the at home section of the CS Unplugged website."""

from django.urls import path
from at_home import views

app_name = 'at_home'
urlpatterns = [
    # eg: /at-home/
    path(
        '',
        views.IndexView.as_view(),
        name='index'
    ),
    # eg: /at-home/binary-challenge/
    path(
        '<slug:activity_slug>/',
        views.ActivityView.as_view(),
        name='activity'
    ),
    # eg: /at-home/binary-challenge/challenges/
    path(
        '<slug:activity_slug>/challenges/',
        views.ActivityChallengesView.as_view(),
        name='activity_challenges'
    ),
    path(
        'ajax/save_challenge_attempt/',
        views.save_challenge_attempt,
        name='save_challenge_attempt'
    ),
]
