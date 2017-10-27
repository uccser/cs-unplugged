"""Provide redirect to static resource file."""

from django.conf import settings
from django.shortcuts import redirect


def resource_pdf_cache(name, generator):
    """Provide redirect to static resource file.

    Args:
        name: Name of resource to be created (str).
        generator: Instance of specific resource generator class.

    Returns:
        HTTP redirect.
    """
    filename = "{} ({})".format(name, generator.subtitle)
    redirect_url = "{}resources/{}.pdf".format(settings.STATIC_URL, filename)
    return redirect(redirect_url)
