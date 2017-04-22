# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode

- Use console backend for emails

- Add Django Debug Toolbar
- Add django-extensions as app
"""

import socket
import os
from .base import *  # noqa: F403

# DATABASE CONFIGURATION
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# DEBUG
# ----------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)  # noqa: F405
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa: F405

# SECRET CONFIGURATION
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='l@@)w&&%&u37+sjz^lsx^+29y_333oid3ygxzucar^8o(axo*f')  # noqa: F405

# Mail settings
# ----------------------------------------------------------------------------

EMAIL_PORT = 1025

EMAIL_HOST = 'localhost'
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')  # noqa: F405


# CACHING
# ----------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ----------------------------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]  # noqa: F405
INSTALLED_APPS += ['debug_toolbar', ]  # noqa: F405

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]
# tricks to have debug toolbar when developing with docker
if os.environ.get('USE_DOCKER') == 'yes':
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + '1']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# django-extensions
# ----------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions', ]

# TESTING
# ----------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# Your local stuff: Below this line define 3rd party library settings
# ----------------------------------------------------------------------------
