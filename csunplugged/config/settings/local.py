# -*- coding: utf-8 -*-
"""
Django settings for local development environment.

- Run in Debug mode
- Add custom dev application
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
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
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

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
STATIC_URL = "/static/"

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
    ".canterbury.ac.nz",
    "localhost",
    "cs-unplugged.localhost",
    "127.0.0.1",
    "[::1]",
]


def show_django_debug_toolbar(request):
    """Show Django Debug Toolbar in every request when running locally.

    Args:
        request: The request object.
    """
    return True


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


# Your local stuff: Below this line define 3rd party library settings
# ----------------------------------------------------------------------------
INSTALLED_APPS += ["dev.apps.DevConfig"]  # noqa: F405
