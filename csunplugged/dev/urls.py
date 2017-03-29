from django.conf.urls import url

from . import views

app_name = 'dev'
urlpatterns = [
    # eg: /topics/
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),
    url(
        r'^(?P<programming_exercise_slug>[-\w]+)/$',
        views.ProgrammingExerciseView.as_view(),
        name='programming_exercise'
    ),
]
