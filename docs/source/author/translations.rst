Translations
##############################################################################

We use a localisation management platform called `Crowdin <https://translate.csunplugged.org/>`__ for translation of CS Unplugged.
Our project is public, meaning that anyone can create an account and contribute translations.

.. note::

  By becoming a translator you agree to uphold our :doc:`Code of Conduct <code_of_conduct>`.

Getting Started
==============================================================================

It's really easy to start contributing translations using CS Unplugged:

1. Read this documentation page, especially the `Translation Notes`_ section.
2. Create an account on `Crowdin <https://crowdin.com/join>`__.
3. Visit the CS Unplugged `development site <http://cs-unplugged-dev.appspot.com/>`_.
4. Switch to translation mode using the language drop down.
5. Log in with your Crowdin credentials and select a target language.
6. Start translating!

Crowdin Overview
==============================================================================

Crowdin has excellent documentation for translators, and all translators should read the following documents:

- `Crowdin Introduction <https://support.crowdin.com/crowdin-intro/>`_, which provides an overview of the Crowdin platform
- `Online Editor <https://support.crowdin.com/online-editor/>`_, which explains how to use the Crowdin UI to contribute translations.
  Note that this page is written about the full online editor on Crowdin.com, but most of the information is also relevant to the `in-context editor <In-Context Localisation_>`_ that we use.


Translation Phases
==============================================================================
There are 3 phases translation phases used to ensure high quality translation of CS Unplugged content:

1. Translation
2. Proofread
3. Technical Review

In the inital translation phase, anyone (who has created an account with Crowdin) can contribute translations.
These translations are then reviewed by a designated proofreader who will check the translations for accuracy and consistency.
To request to become a proofreader, please `contact <https://support.crowdin.com/joining-translation-project/#contacting-a-project-manager>`_ one of the Crowdin project managers.

.. note::
  While not enforced by Crowdin, proofreaders should not approve their own translations.
  Instead, they should be reviewed by a different proofreader.

Finally, a technical review will be performed by a member of the CS Unplugged technical team.
In this review, technical components such as Verto tags and document structure will be checked.

In-Context Localisation
==============================================================================
We utilise Crowdin's in-context localisation feature to allow content translation directly on the development website.
This lets translators see their translations appear as it will look on the final website, in real time.

.. note::

  Verto tags are an exception to this rule.

  The verto tag text is rendered as raw text onto the front end, to allow translators to modify the tag if required.
  These raw text tags will never be visible in the final release, as they are parsed and removed during verto processing.

  For technical reasons, any changes in the translation of a verto tag will not be rendered in-context translation mode, and will only be visible after the translated file is downloaded for release.
  See :ref:`inContextTranslations` for more details.

To use in-context translation features, simply visit the CS Unplugged `development site <http://cs-unplugged-dev.appspot.com/>`_, and use the language selector to select ``Translation Mode``.

.. note::
  For bi-directional languages such as Hebrew and Arabic, translators should instead select ``Translation Mode (Bi-Directional)`` using the language selector.

In cases where in-context translation mode is not available, it is also possible to use the standard Crowdin UI.
To access this, visit the CS Unplugged project page on `Crowdin <https://crowdin.com/project/cs-unplugged>`_.

Translation notes
==============================================================================

.. note::

  On Crowdin, Markdown files are translated on a per-sentence basis. There may
  be some cases where this is not desirable, and some paragraph level restructuring
  is required to convey a concept in a given language.

  In these cases, it could be possible to work around this with tricks such as

  - translating one sentence into the translation box for another.
  - translating a sentence into a blank string.

  These techniques are highly discouraged as they fight against many aspects of
  the Crowdin system including

  - QA checks that ensure translations match the structure of the source strings.
  - Translation memory.
  - In context localisation.

- Special Verto tags which are within curly braces ``{`` ``}`` should not be translated, except for text after ``alt`` in an ``image`` tag.
  For example the text:

  .. code-block:: none

    {image file-path="img/topics/binary-cards.png" alt="Diagram showing 2 binary cards"}

  The only text to translate is 'Diagram showing 2 binary cards'.

- Text within Scratch tags should be translated using Scratchblocks syntax.

If you are unsure how to translate a line, please leave it for another translator.
