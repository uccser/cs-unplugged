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
