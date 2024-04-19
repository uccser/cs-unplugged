# -*- coding: utf-8 -*-
"""
Django settings for local development environment.

- Run in Debug mode
- Add Django Debug Toolbar
- Add django-extensions
- Use console backend for emails
"""

from .base import *  # noqa: F403

# DATABASE CONFIGURATION
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),  # noqa: F405
        "USER": env("POSTGRES_USER"),  # noqa: F405
        "PASSWORD": env("POSTGRES_PASSWORD"),  # noqa: F405
        "HOST": env("POSTGRES_HOST"),  # noqa: F405
        "PORT": env("POSTGRES_PORT"),  # noqa: F405
        "ATOMIC_REQUESTS": True,
    }
}

# DEBUG
# ----------------------------------------------------------------------------
DEBUG = env.bool("DJANGO_DEBUG", default=True)  # noqa: F405
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # noqa: F405

# SECRET CONFIGURATION
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default="DJANGO_SECRET_KEY_FOR_LOCAL_DEVELOPMENT")  # noqa: F405

# Mail settings
# ----------------------------------------------------------------------------

EMAIL_PORT = 1025

EMAIL_HOST = "localhost"
EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")  # noqa: F405


# CACHING
# ----------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": ""
    }
}

# django-debug-toolbar
# ----------------------------------------------------------------------------
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware", ]  # noqa: F405
INSTALLED_APPS += ["debug_toolbar", ]  # noqa: F405

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2", ]

ALLOWED_HOSTS = [
    "cs-unplugged.localhost",
    "localhost",
    "django",
]


def show_django_debug_toolbar(request):
    """Show toolbar in request unless parameter is given.

    Args:
        request: The request object.
    """
    return "hide-debug-toolbar" not in request.GET


DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
    "SHOW_TOOLBAR_CALLBACK": show_django_debug_toolbar,
}

# django-extensions
# ----------------------------------------------------------------------------
INSTALLED_APPS += ["django_extensions", ]

# TESTING
# ----------------------------------------------------------------------------
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# LOGGING
# ------------------------------------------------------------------------------
# Based off https://lincolnloop.com/blog/django-logging-right-way/
# Suppress these loggers in local development for less noise in logs
logging.getLogger('gunicorn.access').handlers = []  # noqa F405
logging.getLogger('gunicorn.error').handlers = []  # noqa F405


# CSRF
# ------------------------------------------------------------------------------
CSRF_TRUSTED_ORIGINS = [
    "https://www.csunplugged.org",
    "https://cs-unplugged-dev.csse.canterbury.ac.nz",
    "https://cs-unplugged.localhost",
]
