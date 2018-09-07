"""Context processor for checking if in deployed environment."""

from django.conf import settings


def deployed(request):
    """Return a dictionary containing boolean if deployed environment.

    Returns:
        Dictionary containing deployed boolean to add to context.
    """
    return {
        "DEPLOYED": settings.DJANGO_PRODUCTION
    }
