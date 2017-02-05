from django.conf.urls import url

from . import views

app_name = 'topics'
urlpatterns = [
    # eg: /topics/
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),
    # eg: /topics/binary-numbers/
    url(
        r'^(?P<topic_slug>[-\w]+)/$',
        views.TopicView.as_view(),
        name='topic'
    ),
    # eg: /topics/binary-numbers/activities
    url(
        r'^(?P<topic_slug>[-\w]+)/activities/$',
        views.ActivityList.as_view(),
        name='activity_list'
    ),
    # eg: /topics/binary-numbers/activities/binary-bracelets
    url(
        r'^(?P<topic_slug>[-\w]+)/activities/(?P<activity_slug>[-\w]+)/$',
        views.ActivityView.as_view(),
        name='activity'
    ),

    # TODO: The following need to be implemented

    # eg: /topics/binary-numbers/other-resources
    # url(
    #     r'^(?P<topic_slug>[-\w]+)/other-resources/$',
    #     views.OtherResourcesList.as_view(),
    #     name='other_resources_list'
    # ),
    # # eg: /topics/binary-numbers/unit-plan
    # url(
    #     r'^(?P<topic_slug>[-\w]+)/(?P<unit_plan_slug>[-\w]+)/$',
    #     views.UnitPlanView.as_view(),
    #     name='unit_plan'
    # ),
    # # eg: /topics/binary-numbers/unit-plan/5-7
    # # TODO: Should this page just be a query of the given ages?
    # url(
    #     r'^(?P<topic_slug>[-\w]+)/(?P<unit_plan_slug>[-\w]+)/(?P<age_bracket>\d{1,2}-\d{1,2})/$',
    #     # Currently redirect to unit plan
    #     views.UnitPlanView.as_view(),
    #     name='age_bracket'
    # ),
    # # eg: /topics/binary-numbers/unit-plan/5-7/lesson-1
    # url(
    #     r'^(?P<topic_slug>[-\w]+)/(?P<unit_plan_slug>[-\w]+)/lesson/(?P<age_bracket>\d{1,2}-\d{1,2})/(?P<lesson_slug>[-\w]+)/$',
    #     views.LessonView.as_view(),
    #     name='lesson'
    # ),
    # # eg: /topics/binary-numbers/unit-plan/lesson-1
    # url(
    #     r'^(?P<topic_slug>[-\w]+)/programming/$',
    #     views.ProgrammingExercisesList.as_view(),
    #     name='programming_exercises_list'
    # ),
    # url(
    #     r'^(?P<topic_slug>[-\w]+)/programming/(?P<programming_exercise_slug>[-\w]+)$',
    #     views.ProgrammingExercisesView.as_view(),
    #     name='programming_exercise'
    # ),
]
