"""View for the classic module."""

from urllib.parse import urljoin
from django.shortcuts import redirect


def redirect_to_classic_unplugged(request, **kwargs):
    """Redirect request to classic.csunplugged.org domain.

    Returns a 301 permanent redirect HTTP response.
    """
    url = urljoin("https://classic.csunplugged.org", request.path)
    return redirect(url, permanent=True)


def redirect_to_homepage(request):
    """Redirect request to homepage.

    Returns a 301 permanent redirect HTTP response.
    """
    return redirect("general:home", permanent=True)


def redirect_to_contact(request):
    """Redirect request to contact page.

    Returns a 301 permanent redirect HTTP response.
    """
    return redirect("general:contact", permanent=True)


def redirect_to_changelog(request):
    """Redirect request to contact page.

    Returns a 301 permanent redirect HTTP response.
    """
    return redirect("https://cs-unplugged.readthedocs.io/changelog.html", permanent=True)


def redirect_to_modems_unplugged(request):
    """Redirect request to specific modems page.

    Returns a 301 permanent redirect HTTP response.
    """
    return redirect(
        "https://classic.csunplugged.org/activities/community-activities/modems-unplugged/",
        permanent=True,
    )


def redirect_to_community_activities(request):
    """Redirect request to community activities page.

    Returns a 301 permanent redirect HTTP response.
    """
    return redirect(
        "https://classic.csunplugged.org/activities/community-activities/",
        permanent=True,
    )
