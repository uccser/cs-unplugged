Translation Infrastructure
##############################################################################

Crowdin
==============================================================================
We use a localisation management platform called Crowdin for translation of CS Unplugged.

https://crowdin.com/project/cs-unplugged

The project is public, so anyone can create an account and contribute translations.

Currently, the following languages are available for translation:

  - Hebrew
  - Maori
  - Polish

These languages serve as a test bed for internationalisation of CS Unplugged.
Further languages will be added over time once the developers are satisfied
that the system is robust



Translatable Files
==============================================================================
There are 3 types of files that contain translatable content:

- Content markdown files
- Content yaml files containg translatable model strings
- ``django.po`` file containing translatable system strings

Translatable source files must always reside under an ``en`` directory tree.
Translated files are downloaded into a directory named with the language's
locale code, and with the same structure as the source tree.

.. note::
  The locale code differs from the language code in format - where a language
  code is of form ``ab-cd``, the locale code will be ``ab_CD``. Directories must be named
  using the locale code recognised by django for that language.

  For more information, see

  - https://docs.djangoproject.com/en/1.11/topics/i18n/
  - https://github.com/django/django/tree/master/django/conf/locale
  - https://github.com/django/django/blob/master/django/utils/translation/trans_real.py#L59

The configuration specifying which files should be uploaded for translation is
stored in the file ``crowdin_content.yaml`` in the repository root. For details
about the structure of this file, see https://support.crowdin.com/configuration-file/

.. note::
  The crowdin placeholder ``osx_locale`` matches the django locale code
  in almost all cases, and should be used for every entry in the config file.
  In any cases where the osx_locale code does not match the django locale code,
  use the ``language_mapping`` option.

  See:

  - https://api.crowdin.com/api/supported-languages
  - https://support.crowdin.com/configuration-file/#language-mapping

  Due to the various automated components in the translation pipeline, the
  following restrictions are imposed on the config file:

  - The ``%osx_locale%`` and ``%original_file_name%`` placeholders must be used.
  - No other placeholders may be used.
  - If a language_mapping is provided for ``osx_locale``, it must be the same for
    all ``files`` entries.



Review Process
==============================================================================
For a translation of any given string to make it to production release, it must
pass the following stages of review:

1. (Crowdin) Translation Proofread - Review by a second translator with 'proofreader' status in the target language.
2. (Crowdin) Tech Review - Review by a member of the CS Unplugged technical team to catch technical errors (i.e. with Verto tags, links, markdown syntax etc).
3. (GitHub) PR Review - Final review of completed translation files being merged into develop. Automated testing on travis will also occur at this stage.

The first two review phases are enforced by a custom workflow on Crowdin.
See their documentation at https://support.crowdin.com/advanced-workflows/


In-Context Translation
==============================================================================
We have utilised Crowdin's 'In-Context' localisation feature to allow content
translation directly on the website, by switching to a special Translation Mode
'pseudo-language'.

In-context translation is only enable on the development version of the website,
at http://cs-unplugged-dev.appspot.com.

For technical details on how in-context localisation works, see Crowdin's
documentations: https://support.crowdin.com/in-context-localization/

.. note::
  The pseudo-language used on Crowdin is ``en-UD`` (English Upside-down)
  The ``Translation Mode`` language used in django is ``xx-lr``. A custom
  ``language_mapping`` entry in the configuration file is used to achieve this
  mapping.

  Additionally, a ``Translation Mode (Bi-Directional)`` language (``yy-rl``)
  is available on django, to support translation into RTL languages. The directory trees
  for this language are always symlinks to ``xx-lr``, but the website is rendered
  using a RTL layout. This enables translators to see how their RTL translations
  will look when relased. This language is not involved in the process of downloading
  translations from crowdin, which only uses ``xx-lr``.

Talk about caveats here? About block tags etc?


Translation Pipeline
==============================================================================

.. image:: ../_static/img/translation_pipeline_overview.png

Crowdin Bot
==============================================================================

In order to manage the complex translation pipeline, an autmoation agent (``crowdin-bot``)
is used to perform the following tasks.

- Updating source .po file with new translatable system strings
- Pushing source files to crowdin for translation
- Downloading updated metadata for in-context translation mode on dev deployment
- Downloading completed translations for release

Crowdin bot is implemented as a number of cron jobs running on a Compute Engine VM.
Each of the above tasks runs periodically as a cron job, independently from one another.
The frequency of each task can be varied by modifying the crontab entry in ``setup-instance.py``
Currently each task is run once per day, each staggered by 1 hour starting from midnight NZDT.

Updating message files - ``crowdin-bot-update-messages.sh``
------------------------------------------------------------------------------

Uploading source files to Crowdin - ``crowdin-bot-push-source.sh``
------------------------------------------------------------------------------

Downloading in-context translation files - ``crowdin-bot-pull-incontext.sh``
------------------------------------------------------------------------------

Downloading completed translations - ``crowdin-bot-pull-translations.sh``
------------------------------------------------------------------------------

Python package
------------------------------------------------------------------------------

Deployment
------------------------------------------------------------------------------

Monitoring
------------------------------------------------------------------------------
Logging + future plans for status monitoring
