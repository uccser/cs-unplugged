# -*- coding: utf-8 -*-
"""
Production settings
"""

from .base import *  # noqa: F403


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANGO_SECRET_KEY not in os.environ
SECRET_KEY = env('DJANGO_SECRET_KEY')  # noqa: F405

# SECURITY WARNING: App Engine's security features ensure that it is safe to
# have ALLOWED_HOSTS = ['*'] when the app is deployed. If you deploy a Django
# app not on App Engine, make sure to set an appropriate host here.
# See https://docs.djangoproject.com/en/1.10/ref/settings/
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'polls',
        'USER': env('GOOGLE_CLOUD_SQL_USERNAME'),
        'PASSWORD': env('GOOGLE_CLOUD_SQL_PASSWORD'),
        'HOST': '/cloudsql/' + env('GOOGLE_CLOUD_SQL_CONNECTION_NAME'),
    }
}
