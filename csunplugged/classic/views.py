"""View for the classic module."""

from urllib.parse import urljoin
from django.shortcuts import redirect


def redirect_to_classic_unplugged(request):
    """Redirect request to classic.csunplugged.org domain.

    Returns a 301 permenant redirect HTTP response.
    """
    url = urljoin("http://classic.csunplugged.org", request.path)
    return redirect(url, permanent=True)

def redirect_to_homepage(request):
    """Redirect request to homepage.

    Returns a 301 permenant redirect HTTP response.
    """
    return redirect("general:home", permanent=True)

def redirect_to_contact(request):
    """Redirect request to contact page.

    Returns a 301 permenant redirect HTTP response.
    """
    return redirect("general:contact", permanent=True)
