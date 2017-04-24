"""URL routing for the dev application."""

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
    url(
        r'^(?P<programming_exercise_slug>[-\w]+)/(?P<programming_language_slug>[-\w]+)-solution$',  # noqa: E501
        views.ProgrammingExerciseLanguageSolutionView.as_view(),
        name='programming_exercise_language_solution'
    ),
    url(
        r'^integrations/(?P<integration_slug>[-\w]+)/$',
        views.CurriculumIntegrationView.as_view(),
        name='integration'
    ),
]
