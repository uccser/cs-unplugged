"""Provide redirect to static resource file."""

import os
from django.conf import settings
from django.shortcuts import redirect
from django.utils.translation import get_language


def resource_pdf_cache(resource, generator):
    """Provide redirect to static resource file.

    Args:
        resource (Resource): Resource to be created.
        generator: Instance of specific resource generator class.

    Returns:
        HTTP redirect.
    """
    filename = "{} ({}).pdf".format(resource.name, generator.subtitle)
    redirect_url = os.path.join(settings.STATIC_URL, "resources", get_language(), resource.slug, filename)
    return redirect(redirect_url)
