"""URL routing for the general application."""

from django.conf.urls import url

from . import views

app_name="general"
urlpatterns = [
    url(
        r"^$",
        views.GeneralIndexView.as_view(),
        name="home"
    ),
    url(
        r"^about/$",
        views.GeneralAboutView.as_view(),
        name="about"
    ),
    url(
        r"^what-is-computer-science/$",
        views.WhatIsCSView.as_view(),
        name="what_is_cs"
    ),
    url(
        r"^computational-thinking/$",
        views.ComputationalThinkingView.as_view(),
        name="computational_thinking"
    ),
    url(
        r"^how-do-i-teach-cs-unplugged/$",
        views.HowDoITeachCSUnpluggedView.as_view(),
        name="how_do_i_teach_cs_unplugged"
    ),
    url(
        r"^contact/$",
        views.GeneralContactView.as_view(),
        name="contact"
    ),
    url(
        r"^people/$",
        views.GeneralPeopleView.as_view(),
        name="people"
    ),
    url(
        r"^principles/$",
        views.GeneralPrinciplesView.as_view(),
        name="principles"
    ),
]
