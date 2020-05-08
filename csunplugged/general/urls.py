"""URL routing for the general application."""

from django.urls import path

from . import views

app_name = 'general'
urlpatterns = [
    path(
        '',
        views.GeneralIndexView.as_view(),
        name="home"
    ),
    path(
        'about/',
        views.GeneralAboutView.as_view(),
        name="about"
    ),
    path(
        'what-is-computer-science/',
        views.WhatIsCSView.as_view(),
        name="what_is_cs"
    ),
    path(
        'computational-thinking/',
        views.ComputationalThinkingView.as_view(),
        name="computational_thinking"
    ),
    path(
        'how-do-i-teach-cs-unplugged/',
        views.HowDoITeachCSUnpluggedView.as_view(),
        name="how_do_i_teach_cs_unplugged"
    ),
    path(
        'contact/',
        views.GeneralContactView.as_view(),
        name="contact"
    ),
    path(
        'people/',
        views.GeneralPeopleView.as_view(),
        name="people"
    ),
    path(
        'principles/',
        views.GeneralPrinciplesView.as_view(),
        name="principles"
    ),
]
