Changelog
##############################################################################

This page lists updates to CS Unplugged.
All notable changes to this project will be documented in this file.

.. note ::

  We base our numbering system from the guidelines at `Semantic Versioning 2.0.0`_,
  however since our project started before it was migrated to GitHub, the first
  major open source release is being labeled as ``2.0.0``.

  Given a version number MAJOR.MINOR.HOTFIX:

  - MAJOR version change when major backend or text modifications are made
    (for example: new topic).
  - MINOR version change when content or functionality is added or updated (for
    example: new videos, new activities, large number of text (typo/grammar) fixes).
  - HOTFIX version change when bug hotfixes are made (for example: fixing a typo).
  - A pre-release version is denoted by appending a hyphen and the alpha label
    followed by the pre-release version.

  As this project contains text content, the updating of content doesn't perfectly
  fit the Semantic Versioning model. However these version numbers can still
  provide a good indication of the changes in each version.

2.0.0-alpha.2
==============================================================================

- **Release date:** 26th June 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Notable changes:**

The inital content for the Unplugged programming topic has been added which
includes the geometry, numeracy, and Kidbots units.

**Changelog:**

- Add unplugged programming topic description.

  - `Hayley van Waas`_ `#469`_

- Add Kidbots unit plan.

  - `Hayley van Waas`_ `#470`_

- Add Kidbots lesson 3 for ages 5 to 7.

  - `Hayley van Waas`_ `#471`_

- Add job badges resource.

  - `Hayley van Waas`_

- Add left right cards resource.

  - `Hayley van Waas`_

- Add arrow cards resource.

  - `Hayley van Waas`_

- Add Kidbots programming exercises.

  - `Hayden Jackson`_ `#249`_

- Add geometry unit plan.

  - `Hayley van Waas`_ `#470`_

- Add geometry lessons 1 and 2 for ages 5 to 7.

  - `Hayley van Waas`_ `#495`_

- Add geometry programming exercises.

  - `Hayden Jackson`_ `#248`_

- Add numeracy unit plan.

  - `Hayley van Waas`_ `#470`_

- Add numeracy programming exercises.

  - `Hayden Jackson`_ `#247`_

- Add numeracy modulo lesson.

  - `Jack Morgan`_ `#397`_

- Add sorting network lesson 1 for ages 5 to 7.

  - `Hayley van Waas`_ `#488`_

- Add binary numbers lesson 3 for ages 5 to 7.

  - `Hayley van Waas`_ `#486`_

- Update modulo clock to have blank option.

  - `Jack Morgan`_ `#427`_

- Add trains straight and circular resources.

  - `Jack Morgan`_ `#428`_

- Add piano keys resource.

  - `Jack Morgan`_ `#429`_

- Add Google analytics.

  - `Jack Morgan`_ `#496`_

- Fix links to deployments in README.

  - `Jack Morgan`_ `#498`_

- Add "Try it out" programming challenge difficulty.

  - `Jack Morgan`_ `#502`_

- Fix typo in how-binary-digits-work-junior lesson (thanks Richard S).

  - `Jack Morgan`_ `#503`_

- Fix Nginx build after Travis image update.

  - `Hayden Jackson`_ `#506`_


2.0.0-alpha.1
==============================================================================

- **Release date:** 20th June 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Notable changes:**

The first major step in releasing a open source version of CS Unplugged.
While some existing content from the classic version of CS Unplugged have yet
to be adapted into the new format and system, we are releasing this version as
a sneak peek for teachers.

The backend system contains the following features:

- Open source system written in Django.

  - Allow translations of other languages (no translations are added yet).
  - Deployable on Google App Engine, and easily customised for other hosts.

- Website designed with Bootstrap 4 for use on all devices.
- Creates PDF resources for use with lessons.
- Basic test suite for checking system functionality.
- Documentation for the system.

The following topics are available in this version:

- Binary numbers:

  - 2 lessons for ages 5 to 7.
  - 3 lessons for ages 8 to 11.
  - 7 curriculum integrations.
  - 24 programming challenges.

- Error detetction and correction:

  - 2 lessons for ages 8 to 11.
  - 5 curriculum integrations.
  - 24 programming challenges.

- Sorting networks:

  - 1 lesson for ages 8 to 10.

.. _Semantic Versioning 2.0.0: http://semver.org/spec/v2.0.0.html
.. _Source downloads are available on GitHub: https://github.com/uccser/cs-unplugged/releases
.. _Hayley van Waas: https://github.com/hayleyavw
.. _#469: https://github.com/uccser/cs-unplugged/issues/469
.. _#470: https://github.com/uccser/cs-unplugged/issues/470
.. _#471: https://github.com/uccser/cs-unplugged/issues/471
.. _Hayden Jackson: https://github.com/ravenmaster001
.. _#249: https://github.com/uccser/cs-unplugged/issues/249
.. _#495: https://github.com/uccser/cs-unplugged/issues/495
.. _#248: https://github.com/uccser/cs-unplugged/issues/248
.. _#247: https://github.com/uccser/cs-unplugged/issues/247
.. _Jack Morgan: https://github.com/JackMorganNZ
.. _#397: https://github.com/uccser/cs-unplugged/issues/397
.. _#488: https://github.com/uccser/cs-unplugged/issues/488
.. _#486: https://github.com/uccser/cs-unplugged/issues/486
.. _#427: https://github.com/uccser/cs-unplugged/issues/427
.. _#428: https://github.com/uccser/cs-unplugged/issues/428
.. _#429: https://github.com/uccser/cs-unplugged/issues/429
.. _#496: https://github.com/uccser/cs-unplugged/issues/496
.. _#498: https://github.com/uccser/cs-unplugged/issues/498
.. _#502: https://github.com/uccser/cs-unplugged/issues/502
.. _#503: https://github.com/uccser/cs-unplugged/issues/503
.. _#506: https://github.com/uccser/cs-unplugged/issues/506
