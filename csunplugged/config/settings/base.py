# -*- coding: utf-8 -*-
"""
Base Django settings for CS Unplugged project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import environ
import os.path
import logging.config

# Add custom languages not provided by Django
import django.conf.locale
from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _

# cs-unplugged/csunplugged/config/settings/base.py - 3 = csunplugged/
ROOT_DIR = environ.Path(__file__) - 3

# Load operating system environment variables and then prepare to use them
env = environ.Env()

# Wipe default Django logging
LOGGING_CONFIG = None

# APP CONFIGURATION
# ----------------------------------------------------------------------------
DJANGO_APPS = [
    # Default Django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",

    # Useful template tags
    "django.contrib.humanize",

    # Admin
    "django.contrib.admin",
]

THIRD_PARTY_APPS = [
    "django_bootstrap_breadcrumbs",
    "haystack",
    "widget_tweaks",
    "modeltranslation",
    "bidiutils",
]

# Apps specific for this project go here.
LOCAL_APPS = [
    "general.apps.GeneralConfig",
    "topics.apps.TopicsConfig",
    "plugging_it_in.apps.PluggingitinConfig",
    "resources.apps.ResourcesConfig",
    "search.apps.SearchConfig",
    "classic.apps.ClassicConfig",
    "at_home.apps.AtHomeConfig",
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

# MIDDLEWARE CONFIGURATION
# ----------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# DEBUG
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# FIXTURE CONFIGURATION
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(ROOT_DIR.path("fixtures")),
)

# EMAIL CONFIGURATION
# -----------------------------------------------------------------------------
# EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND",
#                     default="django.core.mail.backends.smtp.EmailBackend")

# MANAGER CONFIGURATION
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
# ADMINS = [
#     ("University of Canterbury Computer Science Research Group",
#      "csse-education@canterbury.ac.nz"),
# ]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
# MANAGERS = ADMINS

# GENERAL CONFIGURATION
# ----------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "UTC"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en"

INCONTEXT_L10N_PSEUDOLANGUAGE = "xx-lr"
INCONTEXT_L10N_PSEUDOLANGUAGE_BIDI = "yy-rl"
INCONTEXT_L10N_PSEUDOLANGUAGES = (
    INCONTEXT_L10N_PSEUDOLANGUAGE,
    INCONTEXT_L10N_PSEUDOLANGUAGE_BIDI
)

DEFAULT_LANGUAGES = (
    ("en", "English"),
    ("de", "Deutsche"),
    ("es", "Español"),
    ("mi", "Te Reo Māori"),
    ("zh-hans", "简体中文"),
)
# Keep original values of languages for resource generation
LANGUAGES = DEFAULT_LANGUAGES

EXTRA_LANG_INFO = {
    'mi': {
        'bidi': False,
        'code': 'mi',
        'name': "Te Reo Māori",
        'name_local': "Te Reo Māori",
    }
}

if env.bool("INCLUDE_INCONTEXT_L10N", False):
    EXTRA_LANGUAGES = [
        (INCONTEXT_L10N_PSEUDOLANGUAGE, "Translation mode"),
        (INCONTEXT_L10N_PSEUDOLANGUAGE_BIDI, "Translation mode (Bi-directional)"),
    ]

    EXTRA_LANG_INFO.update({
        INCONTEXT_L10N_PSEUDOLANGUAGE: {
            'bidi': False,
            'code': INCONTEXT_L10N_PSEUDOLANGUAGE,
            'name': "Translation mode",
            'name_local': _("Translation mode"),
        },
        INCONTEXT_L10N_PSEUDOLANGUAGE_BIDI: {
            'bidi': True,
            'code': INCONTEXT_L10N_PSEUDOLANGUAGE_BIDI,
            'name': "Translation mode (Bi-directional)",
            'name_local': _("Translation mode (Bi-directional)"),
        }
    })

    # Add new languages to the list of all django languages
    global_settings.LANGUAGES = global_settings.LANGUAGES + EXTRA_LANGUAGES
    global_settings.LANGUAGES_BIDI = (global_settings.LANGUAGES_BIDI +
                                      [INCONTEXT_L10N_PSEUDOLANGUAGE_BIDI.split('-')[0]])
    # Add new languages to the list of languages used for this project
    LANGUAGES += tuple(EXTRA_LANGUAGES)
    LANGUAGES_BIDI = global_settings.LANGUAGES_BIDI

django.conf.locale.LANG_INFO.update(EXTRA_LANG_INFO)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = ["locale"]

# TEMPLATE CONFIGURATION
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [
            str(ROOT_DIR.path("templates")),
        ],
        "OPTIONS": {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            "debug": DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "config.context_processors.version_number.version_number",
                "config.context_processors.deployed.deployed",
                "bidiutils.context_processors.bidi",
            ],
            "libraries": {
                "render_html_field": "config.templatetags.render_html_field",
                "translate_url": "config.templatetags.translate_url",
                "query_replace": "config.templatetags.query_replace",
                'custom_tags':'config.templatetags.custom_tags'
            },
        },
    },
]

# LOGGING
# ------------------------------------------------------------------------------
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console', ],
        },
        'csunplugged': {
            'level': 'INFO',
            'handlers': ['console', ],
            # required to avoid double logging with root logger
            'propagate': False,
        },
    },
})

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(str(ROOT_DIR.path("staticfiles")), "")

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
BUILD_ROOT = os.path.join(str(ROOT_DIR.path("build")), "")
STATIC_URL = "/staticfiles/"

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    BUILD_ROOT,
]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR("media"))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# SEARCH CONFIGURATION
# ------------------------------------------------------------------------------
# See: http://django-haystack.readthedocs.io/en/v2.6.0/settings.html
HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": str(ROOT_DIR.path("whoosh_index")),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

# OTHER SETTINGS
# ------------------------------------------------------------------------------
DJANGO_PRODUCTION = env.bool("DJANGO_PRODUCTION")
TOPICS_CONTENT_BASE_PATH = os.path.join(str(ROOT_DIR.path("topics")), "content")
RESOURCES_CONTENT_BASE_PATH = os.path.join(str(ROOT_DIR.path("resources")), "content")
RESOURCE_GENERATION_LOCATION = os.path.join(str(ROOT_DIR.path("staticfiles")), "resources")
RESOURCE_GENERATORS_PACKAGE = "resources.generators"
RESOURCE_COPY_AMOUNT = 20
SCRATCH_GENERATION_LOCATION = str(ROOT_DIR.path("temp"))
CUSTOM_VERTO_TEMPLATES = os.path.join(str(ROOT_DIR.path("utils")), "custom_converter_templates", "")
MODELTRANSLATION_CUSTOM_FIELDS = ("JSONField",)
CLASSIC_PAGES_CONTENT_BASE_PATH = os.path.join(str(ROOT_DIR.path("classic")), "content")
GENERAL_PAGES_CONTENT_BASE_PATH = os.path.join(str(ROOT_DIR.path("general")), "content")
ACTIVITIES_CONTENT_BASE_PATH = os.path.join(str(ROOT_DIR.path("at_home")), "content")
BREADCRUMBS_TEMPLATE = "django_bootstrap_breadcrumbs/bootstrap4.html"
