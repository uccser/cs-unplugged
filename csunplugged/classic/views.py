"""View for the classic module."""

from urllib.parse import urljoin
from django.shortcuts import redirect


def redirect_to_classic_unplugged(request):
    """Redirect request to classic.csunplugged.org domain.

    Returns a 302 permenant redirect HTTP response.
    """
    url = urljoin("http://classic.csunplugged.org", request.path)
    return redirect(url, permanent=True)
