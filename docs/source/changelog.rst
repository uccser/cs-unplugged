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

2.0.0-alpha.6
==============================================================================

- **Release date:** 21st December 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Summary of changes:**

This release adds support for multiple languages, while also finalising the website design.
New introductory pages and Pixel Painter resource have been added, and the 'Unplugged Programming' topic has been streamlined into the 'Kidbots' topic.
Many other smaller corrections, illustrations, and bugfixes have also been added.

**Changelog:**

- Add support for multiple languages. `#103 <https://github.com/uccser/cs-unplugged/issues/103>`_

  - Automatically upload and download translations from `Crowdin`_. `#618 <https://github.com/uccser/cs-unplugged/issues/618>`_ `#619 <https://github.com/uccser/cs-unplugged/issues/619>`_ `#620 <https://github.com/uccser/cs-unplugged/issues/620>`_ `#621 <https://github.com/uccser/cs-unplugged/issues/621>`_
  - Update website design for bidirectional langauges. `#736 <https://github.com/uccser/cs-unplugged/issues/736>`_
  - Implement dynamic text overlay for resource generation. `#670 <https://github.com/uccser/cs-unplugged/issues/670>`_

- Update website design

  - New navigation bar (with language picker).
  - New homepage design with card design for links. `#698 <https://github.com/uccser/cs-unplugged/issues/698>`_
  - Update topics index to show summary information. `#696 <https://github.com/uccser/cs-unplugged/issues/696>`_
  - Simplify topic page. `#696 <https://github.com/uccser/cs-unplugged/issues/696>`_
  - Simplify unit plan page.
  - New footer design. `#695 <https://github.com/uccser/cs-unplugged/issues/695>`_
  - Update Bootstrap 4 from Alpha 6 to Beta 2.
  - Change header font to Sniglet and body font to Noto Sans.

- Add introductory pages on 'What is Computer Science?' and 'How do I teach CS Unplugged?'.
- Restructure 'Unplugged Programming' to 'Kidbots' and remove duplicate lessons. `#588 <https://github.com/uccser/cs-unplugged/issues/588>`_
- Add Pixel Painter resource.
- Mention arrows resource in text. `#702 <https://github.com/uccser/cs-unplugged/issues/702>`_
- Restructure resource options to be generated from Python module. `#701 <https://github.com/uccser/cs-unplugged/pull/701>`_
- Add animations and illustrations for 'The Great Treasure Hunt (Sorted)' lessons. `#672 <https://github.com/uccser/cs-unplugged/pull/672>`_
- Add animations and illustrations for 'Divide and Conquer' lessons. `#673 <https://github.com/uccser/cs-unplugged/pull/673>`_
- Update Microsoft logo. `#708 <https://github.com/uccser/cs-unplugged/issues/708>`_
- Fix blank dropdown box in 'Investigating variations using the Sorting Network'. `#675 <https://github.com/uccser/cs-unplugged/issues/675>`_
- Simplify 'Error detection and correction' logo.
- Modify ``csu`` helper script and Docker setup for OSX compatability. `#651 <https://github.com/uccser/cs-unplugged/issues/651>`_
- Package updates:

  - Add tinycss 0.4.
  - Add django-modeltranslation 0.12.1.
  - Add lxml 4.1.1.
  - Add uniseg 0.7.1.
  - Add python-bidi 0.4.0.
  - Add arabic-reshaper 2.0.14.
  - Add django-bidi-utils 1.0.
  - Update tqdm to 4.19.5.
  - Update django-debug-toolbar 1.9.1.
  - Update django-extensions 1.9.8.
  - Update coverage to 4.4.2
  - Update Django to 1.11.7 and lock Django to 1.11 versions (long term release). `#679 <https://github.com/uccser/cs-unplugged/issues/679>`_ `#743 <https://github.com/uccser/cs-unplugged/issues/743>`_

2.0.0-alpha.5
==============================================================================

- **Release date:** 30th October 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Notable changes:**

This release improves many backend features, including smarter resource generation,
dynamic resource previews, improved system testing, and bug fixes.

**Changelog:**

- Alter resources to use class based generators. `#636 <https://github.com/uccser/cs-unplugged/issues/636>`_
- Add resource thumbnails on generation page. `#642 <https://github.com/uccser/cs-unplugged/issues/642>`_
- Fix bug where production website is using development static files. `#646 <https://github.com/uccser/cs-unplugged/issues/646>`_
- Fix bug where production static files are not deployed.

2.0.0-alpha.4
==============================================================================

- **Release date:** 17th October 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Notable changes:**

Adds a new searching algorithms topic including lessons, resources, and
curriculum integrations.
New lessons for existing topics have also been added.

**Changelog:**

- Add searching algorithms topic. `#548 <https://github.com/uccser/cs-unplugged/issues/548>`_
- Add Unplugged Programming: Kidbots lesson 1 for ages 5 - 7. `#549 <https://github.com/uccser/cs-unplugged/issues/549>`_
- Add Unplugged Programming: Kidbots lesson 2 for ages 5 - 7. `#550 <https://github.com/uccser/cs-unplugged/issues/550>`_
- Add Unplugged Programming: Numeracy lesson 1 for ages 5 - 7. `#551 <https://github.com/uccser/cs-unplugged/issues/551>`_
- Add Sorting Network lesson 2 for ages 5 - 7. `#595 <https://github.com/uccser/cs-unplugged/issues/595>`_
- Add curriculum integrations for searching algorithms. `#589 <https://github.com/uccser/cs-unplugged/issues/589>`_
- Add 12 and 13 digit barcode checksum poster resources. `#545 <https://github.com/uccser/cs-unplugged/issues/545>`_ `#546 <https://github.com/uccser/cs-unplugged/issues/546>`_
- Add searching card resource. `#547 <https://github.com/uccser/cs-unplugged/issues/547>`_
- Update treasure hunt resource to include optional instruction sheet and colour version.
- Display alpha version number in header. `#559 <https://github.com/uccser/cs-unplugged/issues/559>`_
- Force HTTPS connection. `#497 <https://github.com/uccser/cs-unplugged/issues/497>`_
- Convert "Butterfly" and "Red Riding Hood" into sorting cards resource variants. `#534 <https://github.com/uccser/cs-unplugged/issues/534>`_ `#535 <https://github.com/uccser/cs-unplugged/issues/535>`_
- Update resources to new resource module specification.
- Allow raw HTML as source for resource generation.
- Use UCCSER Docker images for stability. `#231 <https://github.com/uccser/cs-unplugged/issues/231>`_
- Improve readability and efficiency of CSU helper script.
- Update Kidbots images to animations.
- Add video for Product Code Check Digits lesson.
- Update automated deployment infrastructure. `#587 <https://github.com/uccser/cs-unplugged/issues/587>`_ `#590 <https://github.com/uccser/cs-unplugged/issues/590>`_
- Add hover state for coloured panels. `#591 <https://github.com/uccser/cs-unplugged/issues/591>`_
- Fix bug where sorting network cards render incorrectly. `#596 <https://github.com/uccser/cs-unplugged/issues/596>`_
- Fix typo in 12-digit product code instructions. `#599 <https://github.com/uccser/cs-unplugged/issues/599>`_
- Open PDF resource download in new tab. `#431 <https://github.com/uccser/cs-unplugged/issues/431>`_
- Fix bug in Google analytics. `#539 <https://github.com/uccser/cs-unplugged/issues/539>`_

2.0.0-alpha.3
==============================================================================

- **Release date:** 27th June 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Notable changes:**

This release adds several lessons, curriculum integrations, and programming challenges.
It also fixes many visual bugs and inconsistencies.

**Changelog:**

- Add Error correction and detection lesson 1 for ages 5 to 7. `#487 <https://github.com/uccser/cs-unplugged/issues/487>`_
- Move Computational Thinking links of Unplugged programming unit plans to separate files. `#512 <https://github.com/uccser/cs-unplugged/issues/512>`_
- Add Kidbots lesson 1 for ages 8 to 10. `#514 <https://github.com/uccser/cs-unplugged/issues/514>`_
- Increase size of content images. `#516 <https://github.com/uccser/cs-unplugged/issues/516>`_
- Fix images with wrong file extension. `#517 <https://github.com/uccser/cs-unplugged/issues/517>`_
- Add visual separators between units on topic page. `#519 <https://github.com/uccser/cs-unplugged/issues/519>`_
- Consistently name and capitalise unit plans. `#520 <https://github.com/uccser/cs-unplugged/issues/520>`_
- Add Sorting networks curriculum integration "Retelling a story". `#521 <https://github.com/uccser/cs-unplugged/issues/521>`_
- Add Sorting networks curriculum integration "Growing into a butterfly". `#522 <https://github.com/uccser/cs-unplugged/issues/522>`_
- Always display curriculum areas for learning outcomes on a new line. `#523 <https://github.com/uccser/cs-unplugged/issues/523>`_
- Center navbar menu text on mobile devices. `#524 <https://github.com/uccser/cs-unplugged/issues/524>`_
- Add modulo programming exercises. `#525 <https://github.com/uccser/cs-unplugged/issues/525>`_
- Set lesson tables to always be consistent width. `#526 <https://github.com/uccser/cs-unplugged/issues/526>`_
- Don't show curriculum integrations shortcut in topic sidebar if no integrations are available. `#533 <https://github.com/uccser/cs-unplugged/issues/533>`_

2.0.0-alpha.2
==============================================================================

- **Release date:** 26th June 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Notable changes:**

The inital content for the Unplugged programming topic has been added which
includes the geometry, numeracy, and Kidbots units.

**Changelog:**

- Add unplugged programming topic description. `#469`_
- Add Kidbots unit plan. `#470`_
- Add Kidbots lesson 3 for ages 5 to 7. `#471`_
- Add job badges resource.
- Add left right cards resource.
- Add arrow cards resource.
- Add Kidbots programming exercises. `#249`_
- Add geometry unit plan. `#470`_
- Add geometry lessons 1 and 2 for ages 5 to 7. `#495`_
- Add geometry programming exercises. `#248`_
- Add numeracy unit plan. `#470`_
- Add numeracy programming exercises. `#247`_
- Add numeracy modulo lesson. `#397`_
- Add sorting network lesson 1 for ages 5 to 7. `#488`_
- Add binary numbers lesson 3 for ages 5 to 7. `#486`_
- Update modulo clock to have blank option. `#427`_
- Add trains straight and circular resources. `#428`_
- Add piano keys resource. `#429`_
- Add Google analytics. `#496`_
- Fix links to deployments in README. `#498`_
- Add "Try it out" programming challenge difficulty. `#502`_
- Fix typo in how-binary-digits-work-junior lesson (thanks Richard S).`#503`_
- Fix Nginx build after Travis image update. `#506`_

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
.. _#469: https://github.com/uccser/cs-unplugged/issues/469
.. _#470: https://github.com/uccser/cs-unplugged/issues/470
.. _#471: https://github.com/uccser/cs-unplugged/issues/471
.. _#249: https://github.com/uccser/cs-unplugged/issues/249
.. _#495: https://github.com/uccser/cs-unplugged/issues/495
.. _#248: https://github.com/uccser/cs-unplugged/issues/248
.. _#247: https://github.com/uccser/cs-unplugged/issues/247
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
.. _Crowdin: https://crowdin.com/project/cs-unplugged
