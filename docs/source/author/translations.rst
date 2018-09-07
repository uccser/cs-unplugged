Translations
##############################################################################

Getting Started
==============================================================================

It's really easy to start contributing translations using CS Unplugged

1. Read this documentation page, especially the `Translation Notes`_ section.
2. Create an account on `Crowdin <https://crowdin.com/join>`__.
3. Visit the `CS Unplugged Crowdin page <https://translate.csunplugged.org/>`__.
4. Start translating!

.. note::

  The in-context translation has been removed temporarily as translation infrastructure is being updated.
  We aim to `re-add this feature in a future update <https://github.com/uccser/arnold/issues/4>`__.

Crowdin Overview
==============================================================================
We use a localisation management platform called `Crowdin <https://translate.csunplugged.org>`__ for translation of CS Unplugged.
Our project is public, meaning that anyone can create an account and contribute translations.

Crowdin has excellent documentation for translators, and all translators should read the following documents:

- `Crowdin Introduction <https://support.crowdin.com/crowdin-intro/>`_, which provides an overview of the Crowdin platform
- `Online Editor <https://support.crowdin.com/online-editor/>`_, which explains how to use the Crowdin UI to contribute translations.

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
