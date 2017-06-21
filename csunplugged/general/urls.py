"""URL routing for the general application."""

from django.conf.urls import url

from . import views

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
        r"^computational-thinking/$",
        views.ComputationalThinkingView.as_view(),
        name="computational_thinking"
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
