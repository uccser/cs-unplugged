Translations
##############################################################################

Getting Started
==============================================================================

In-Context Localisation
==============================================================================

Translation notes
==============================================================================

.. note::

  On Crowdin, markdown files are translated on a per-sentence basis. There may
  be some cases where this is not desirable, and some paragraph level restructuring
  is required to convey a concept in a given language.

  In these cases, it's possible to work around this with tricks such as

  - translating one sentence into the translation box for another.
  - translating a sentence into a blank string.

  These techniques are highly discouraged as they fight against many aspects of
  the Crowdin system including

  - QA checks that ensure translations match the structure of the source strings.
  - Translation memory.
  - In context localisation.
