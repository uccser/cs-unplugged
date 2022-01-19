Changelog
##############################################################################

This page lists updates to CS Unplugged.
All notable changes to this project will be documented in this file.

.. note ::

  We base our numbering system from the guidelines at `Semantic Versioning 2.0.0`_,
  for versions ``4.0.0-alpha.1`` onwards.

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

6.5.0
==============================================================================

**Release date:** 19th December 2022

**Changelog:**

- Add block based programming language for Plugging It In.
- Update information on Online Courses page.
- Add new Classic CS Unplugged logo.
- Fix grammar in several lessons.
- Expand 'BST' acronym in learning outcomes.
- Add Django system check to required checks in testing and deployment pipeline.
- Set Traefik redirect middleware to have a unique name.
- Dependency updates:
  - Update autoprefixer from 10.3.6 to 10.3.7.
  - Update codemirror from 5.63.1 to 5.63.3.
  - Update postcss 8.3.8 to 8.3.9.
  - Update sass 1.42.1 to 1.43.1.
  - Update django from 3.2.7 to 3.2.8.
  - Update PyYAML from 5.4 to 6.0.
  - Update flake8 from 3.9.2 to 4.0.1.
  - Update coverage from 5.5 to 6.0.2.

6.4.0
==============================================================================

**Release date:** 17th November 2021

**Changelog:**

- Add 'Online Courses (MOOCs)' area of the website:
  - Added first course with links to supporting resources.
  - Update notice on homepage to link to new course.
- Add new Classic CS Unplugged logo.
- Fix grammar in several lessons.
- Expand 'BST' acronym in learning outcomes.
- Add Django system check to required checks in testing and deployment pipeline.
- Set Traefik redirect middleware to have a unique name.
- Dependency updates:
  - Update autoprefixer from 10.3.6 to 10.3.7.
  - Update codemirror from 5.63.1 to 5.63.3.
  - Update postcss 8.3.8 to 8.3.9.
  - Update sass 1.42.1 to 1.43.1.
  - Update django from 3.2.7 to 3.2.8.
  - Update PyYAML from 5.4 to 6.0.
  - Update flake8 from 3.9.2 to 4.0.1.
  - Update coverage from 5.5 to 6.0.2.

6.3.0
==============================================================================

**Release date:** 4th October 2021

**Changelog:**

- New topic "Data structures for searching":

  - Includes binary search trees lesson, aimed at ages 11 to 14. `#1559 <https://github.com/uccser/cs-unplugged/pull/1559>`__

- Add Māori subtitles for videos.
- Move website from Google Cloud Platform to Docker Swarm hosted at the University of Canterbury.  `#1616 <https://github.com/uccser/cs-unplugged/pull/1616>`__

  - Modifies website infrastructure to use Docker Swarm, running all website components as services.
  - Static files are now served by Django.
  - Use GitHub actions for automated workflows. This includes testing, deployment, and internationalisation jobs.
  - Simplify static file pipeline, runs as separate Docker service.

- Scratch blocks are updated from Scratch 2 to Scratch 3.
- Fix bug when plural was displayed when there is only one object.
- Update links to Classic CS Unplugged.
- Add open/close icon to detail panels.
- Simplify flags for makeresources management command.
- Switch to GitHub dependency manager.
- Dependency changes:

  - Add ansi-colors 4.1.1.
  - Add browser-sync 2.27.5.
  - Add cssnano 5.0.8.
  - Add del 4.1.1.
  - Add django-haystack[elasticsearch] 3.1.1.
  - Add elasticsearch 5.5.3.
  - Add fancy-log 1.3.3.
  - Add gulp-concat 2.6.1.
  - Add gulp-error-handle 1.0.1.
  - Add gulp-imagemin 7.0.0.
  - Add pixrem 5.0.0.
  - Add postcss 8.3.8.
  - Add sass 1.42.1.
  - Add whitenoise 5.3.0.
  - Update autoprefixer from 9.5.1 to 10.3.6.
  - Update bootstrap from 4.4.1 to 4.6.0.
  - Update browserify from 16.2.3 to 17.0.0.
  - Update codemirror from 5.52.2 to 5.63.1.
  - Update coverage from 5.3.1 to 5.5.
  - Update crowdin/github-action from 1.0.18 to 1.4.0.
  - Update django from 2.2.12 to 3.2.6.
  - Update django-debug-toolbar from 3.1.1 to 3.2.2.
  - Update django-enviro from 0.4.5 to 0.7.0.
  - Update django-extensions from 3.0.9 to 3.1.3.
  - Update django-modeltranslation from 0.16.1 to 0.17.3.
  - Update flake8 from 3.8.4 to 3.9.2.
  - Update gulp-filter from 5.1.0 to 7.0.0.
  - Update gulp-if from 2.0.2 to 3.0.0.
  - Update gulp-postcss from 8.0.0 to 9.0.1.
  - Update gulp-sass from 4.0.2 to 5.0.0.
  - Update gulp-sourcemaps from 2.6.5 to 3.0.0.
  - Update gulp-tap from 1.0.1 to 2.0.0.
  - Update gulp-terser from 1.1.7 to 2.1.0.
  - Update gunicorn from 19.9.0 to 20.1.0.
  - Update intro.js from 2.9.3 to 4.2.2.
  - Update jquery from 3.4.1 to 3.6.0.
  - Update multiple-select 1.2.1 to 1.5.2.
  - Update Pillow from 8.1.0 to 8.3.2.
  - Update popper.js from 1.15.0 to 1.16.1.
  - Update postcss-flexbugs-fixes from 4.1.0 to 5.0.2.
  - Update psycopg2 from 2.7.6.1 to 2.9.1.
  - Update pydocstyle from 5.1.1 to 6.1.1.
  - Update PyYAML from 5.3.1 to 5.4.
  - Update requests from 2.25.1 to 2.26.0.
  - Update scratchblocks from 3.1.2 to UCCSER variant.
  - Update sphinx from 3.4.3 to 4.2.0.
  - Update sphinx-rtd-theme from 0.5.1 to 1.0.0.
  - Update tqdm from 4.51.0 to 4.62.3.
  - Update uniseg from 0.7.1 to 0.7.1.post2.
  - Update verto from 0.10.0 to 1.0.1.
  - Update weasyprint from 52.2 to 52.4.
  - Update yargs from 13.2.4 to 17.2.1.
  - Update yattag from 1.12.2 to 1.14.0.
  - Remove django-haystack.
  - Remove gulp-jshint.
  - Remove gulp-notify.
  - Remove gulp-rename.
  - Remove gulp-util.
  - Remove gulplog.
  - Remove jshint-stylish.
  - Remove jshint.
  - Remove request.
  - Remove run-sequence.
  - Remove sticky-state.
  - Remove through2.
  - Remove wheel.
  - Remove Whoosh.

6.2.1
==============================================================================

- **Release date:** 17th February 2021
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/>`__

**Changelog:**

- Fix bug where not all printable PDFs were generated.
- Update test suite to cover basic infrastructure tasks.

6.2.0
==============================================================================

- **Release date:** 16th February 2021
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/>`__

**Changelog:**

- Add initial French language content:
    - Four lessons for Binary Numbers topic.
    - All printables.
    - All glossary definitions.

- Update contributors list.
- Switch to Crowdin GitHub Action for updating translation files.
- Switch to using Dependabot for tracking dependency updates.

- Dependency updates:

    - Update coverage from 5.2.1 to 5.3.1.
    - Update django-debug-toolbar from 2.2 to 3.1.1.
    - Update django-extensions from 3.0.8 to 3.0.9.
    - Update django-haystack from 2.8.1 to 3.0.
    - Update django-modeltranslation from 0.15.2 to 0.16.1.
    - Update flake8 from 3.8.3 to 3.8.4.
    - Update Pillow from 7.2.0 to 8.1.0.
    - Update requests from 2.24.0 to 2.25.1.
    - Update sphinx from 3.2.1 to 3.4.3.
    - Update sphinx-rtd-theme from 0.5.0 to 0.5.1.
    - Update tqdm from 4.48.2 to 4.51.0.

6.1.3
==============================================================================

- **Release date:** 8th December 2020
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/>`__

**Changelog:**

- Remove the following folders when deploying to production:
    - csunplugged/build
    - csunplugged/temp
    - csunplugged/staticfiles

6.1.2
==============================================================================

- **Release date:** 8th December 2020
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/>`__

**Changelog:**

- Ignore the csunplugged/build/img folder in Google Cloud.

6.1.1
==============================================================================

- **Release date:** 8th December 2020
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/>`__

**Changelog:**

- Add 3 'At home' activities:
    - Guess my number
    - Find my card
    - Guess the sentence

- Dependency updates:

    - Update lxml from 4.5.2 to 4.6.2.

6.0.1
==============================================================================

- **Release date:** 15th October 2020
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/>`__

**Changelog:**

- Fix bug that allowed a user to insert working HTML into their copy of a Plugging it in challenge template.

6.0.0
==============================================================================

- **Release date:** 8th October 2020
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/>`__

**Summary of changes:**

This release adds the 'Plugging it in' area of the website.

**Changelog:**

- Add 'Plugging it in' area of the website:
    - Includes 21 programming challenges in Python for Binary Numbers.
    - Includes 9 programming challenges in Python for Kidbots.
    - Saves a users code attempt and their status on the question.
    - User code tested on the JOBE server.
    - Scratch questions are not supported.
    - User triggered walk-through on programming challenge page.
- Add learning outcome and solution content to programming challenges table in the educators area.
- Replace content under the Python dropdown on programming challenge pages in CSU with a link to the same challenge in Plugging it in.
- Order glossary terms alphabetically for all languages.
- Solutions provided on the standard CSU site now pass the tests for the respective programming challenge on the CSU Plugging it in site.
- Host videos on Vimeo instead of YouTube.
- Re-number product code check digits programming challenges.
- Edit the formatting of subtitle files for Vimeo.
- Put testing examples for programming challenges into a separate markdown file.
- Add Google Tag Manager.
- Minor content fixes.

- Dependency updates:

    - Update coverage from 5.1 to 5.2.1.
    - Update django-modeltranslation from 0.14.1 to 0.15.2.
    - Update django-extensions from 2.2.9 to 3.0.8.
    - Update flake8 from 3.8.2 to 3.8.3.
    - Update lxml from 4.5.1 to 4.5.2.
    - Update Pillow from 7.1.2 to 7.2.0.
    - Update pydocstyle from 5.0.2 to 5.1.1.
    - Update requests from 2.23.0 to 2.24.0.
    - Update sphinx from 3.0.4 to 3.2.1.
    - Update sphinx-rtd-theme from 0.4.3 to 0.5.0.
    - Update tqdm from 4.46.1 to 4.48.2.
    - Update wheel from 0.34.2 to 0.35.1.

5.1.1
==============================================================================

- **Release date:** 8th July 2020
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/>`__

**Changelog:**

- Correction of font colour for digits in Product Code unit.

5.1.0
==============================================================================

- **Release date:** 1st July 2020
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/>`__

**Changelog:**

- Add video to the end of the 'What is Computer Science?' page.
- Show 'plugging it in' pages everywhere except on production.

5.0.1
==============================================================================

- **Release date:** 11th June 2020
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/>`__

**Changelog:**

- Fix bug in 'unlocking the secret in product codes' challenge number 4.
- Add introduction video to the mind reading magic challenge.
- Remove outdated demonstration video from mind reading magic more information section.
- Minor content fixes.

5.0.0
==============================================================================

- **Release date:** 3rd June 2020
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/>`__

**Summary of changes:**

This release adds the 'At Home' area of the website, and restructures the homepage for future areas.

**Changelog:**

- Add 'At Home' area of the website:
    - Includes 5 activities.
    - Includes challenges that are tested locally, with answered stored anonymously on the database for analysis.
    - Enables admin application to allow reading of challenge submissions.
- Update homepage to organise links for educators, home use, and students.
- Update base Docker images to use Debian 10, Python 3.8.3, and Django 2.2.12.
- Set static files to be uploaded using multiprocessing.

- Dependency updates:

    - Add requests 2.23.0.
    - Update coverage from 5.0 to 5.1.
    - Update django-bootstrap-breadcrumbs from 0.9.1 to 0.9.2.
    - Update django-debug-toolbar from 2.1 to 2.2.
    - Update django-extensions from 2.2.5 to 2.2.9.
    - Update django-widget-tweaks from 1.4.5 to 1.4.8.
    - Update flake8 from 3.7.9 to 3.8.2.
    - Update lxml from 4.4.2 to 4.5.1.
    - Update Pillow from 6.2.1 to 7.1.2.
    - Update pydocstyle from 5.0.1 to 5.0.2.
    - Update PyYAML from 5.2 to 5.3.1.
    - Update sphinx from 2.3.0 to 3.0.4.
    - Update tqdm from 4.40.2 to 4.46.1.
    - Update wheel from 0.33.6 to 0.34.2.

4.4.0
==============================================================================

- **Release date:** 1st April 2020
- **Downloads:** `Source downloads are available on GitHub`_

**Summary of changes:**

This release add a new CS Unplugged at home section.

**Changelog:**

- Add 'At home' application, with basic activities before new content is released.
- Darken colours to improve readability of white text on backgrounds.
- Update logo to increase the size of the 'CS' and lessened the rounded corners to improve readability.
- Separate core HTML structure in templates to allow subsites to exist.
- Update static pipeline to use NPM, based off other UCCSER repositories.
- Add 'dev' helper script to align with other UCCSER repositories.

4.3.0
==============================================================================

- **Release date:** 20th December 2019
- **Downloads:** `Source downloads are available on GitHub <https://github.com/uccser/cs-unplugged/releases/tag/4.3.0>`__

**Summary of changes:**

This release adds the image representation topic, along with new lessons for the Māori language.

**Changelog:**

- Add Image Representation topic, which includes one lesson for ages 5 to 10. `#1225 <https://github.com/uccser/cs-unplugged/pull/1225>`__
- Add Māori content:
  - Two Kidbot (Ngā Karetao Tamariki) lessons.
  - Two Error Detection and Correction (Te rapu me te whakatikatika i ngā hapa) lessons.
  - Glossary definitions.
- Improve links to Computational Thinking and CS Unplugged page. `#1203 <https://github.com/uccser/cs-unplugged/issues/1203>`__
- Change Pixel Painter legend to reverse digits for 1 and 0. `#1220 <https://github.com/uccser/cs-unplugged/issues/1220>`__
- Add new single page variations for Pixel Painter printable.
- Add button on topics page to link to classic topic list. `#985 <https://github.com/uccser/cs-unplugged/issues/985>`__
- Fix bug when viewing programming language questions that are not translated.
- Remove deprecated custom Google App Engine health check logic.
- Update documentation for topics application. `#1205 <https://github.com/uccser/cs-unplugged/issues/1205>`__
- Update flow charts in author/topics documentation page. `#749 <https://github.com/uccser/cs-unplugged/issues/749>`__

- Dependency updates:

  - Update coverage from 4.5.2 to 5.0.
  - Update cssselect from 1.0.3 to 1.1.0.
  - Update django-debug-toolbar from 1.11 to 2.1.
  - Update django-extensions from 2.1.6 to 2.2.5.
  - Update django-modeltranslation from 0.13 to 0.14.1.
  - Update django-widget-tweaks from 1.4.3 to 1.4.5.
  - Update flake8 from 3.7.7 to 3.7.9.
  - Update lxml from 4.2.5 to 4.40.2.
  - Update Pillow from 5.4.1 to 6.2.1.
  - Update pydocstyle from 3.0.0 to 5.0.1.
  - Update python-bidi from 0.4.0 to 0.4.2.
  - Update python-markdown-math from 0.5 to 0.6.
  - Update PyYAML from 5.1 to 5.2.
  - Update sphinx from 2.0.0 to 2.2.2.
  - Update sphinx from 2.2.2 to 2.3.0.
  - Update tqdm from 4.28.1 to 4.40.2.
  - Update wheel from 0.33.1 to 0.33.6.
  - Update yattag from 1.11.1 to 1.12.2.

4.2.1
==============================================================================

- **Release date:** 2nd April 2019
- **Downloads:** `Source downloads are available on GitHub`_

**Changelog:**

- Fix bug where Te Reo Māori language data was not added to Django.

4.2.0
==============================================================================

- **Release date:** 1st April 2019
- **Downloads:** `Source downloads are available on GitHub`_

**Summary of changes:**

This release adds Te Reo Māori, Simplified Chinese (简体中文), and German (Deutsche) content, along with many bugfixes.

**Changelog:**

- Added Simplified Chinese (简体中文) language, currently the following pages are available:
  - All basic pages
  - All printables
  - Binary numbers topic: one lesson for 8 to 10 year olds, and 3 curriculum integrations.
- Added Te Reo Māori language, currently the following pages are available:
  - All basic pages
  - All printables
- Added new German (Deutsche) content:
  - Kidbots topic has 2 lessons for 5 to 7 year olds, and 4 curriculum integrations.
  - Sorting networks topic has 2 lessons for 5 to 7 year olds, and 2 curriculum integrations.
  - Additional content to the binary numbers topic includes 2 new lessons for 8 to 10 year olds, and 4 more curriculum integrations.
- Added 17 glossary definitions. `#472 <https://github.com/uccser/cs-unplugged/issues/472>`__
- Added 'Treasure Island' printable.
- Added description of alphabet on 'Binary to Alphabet' printable if required.
- Removed use of SVG for adding labels to 'Job Badges' printable.
- Added 'Kauri Tree' option for 'Sorting Network Cards' printable.
- Removed 'Māori colours' and 'Māori numbers' option from 'Sorting Network Cards' printable, these are now accessed through the Te Reo Māori language.
- Added 'alt' descriptions to images for greater content accessibility.
- Fixed various minor text corrections across content.
- Listed sponsors in README document.
- Fixed incorrect statement on 'Pixel Painter' printable description page.
- Removed extra spaces around programming language ages. `#1151 <https://github.com/uccser/cs-unplugged/issues/1151>`__
- Simplified logic required for translation is not available badges within templates.
- Added warning to printable if translation is not available.
- Removed files of printable thumbnails, and use generated thumbnails.
- Replace translation pipeline 'crowdin bot' with new 'Arnold system'.
- Added 'lite_update' command for only loading key content for development.
- Package updates:

  - Update wheel from 0.31.1 to 0.33.1.
  - Update Pillow from 5.2.0 to 5.4.1.
  - Update yattag from 1.10.0 to 1.11.1.
  - Update verto from 0.7.4 to 0.10.0.
  - Update django-widget-tweaks from 1.4.2 to 1.4.3.
  - Update PyYAML from 4.2b4 to 5.1.
  - Update tqdm from 4.25.0 to 4.28.1.
  - Update lxml from 4.2.4 to 4.2.5.
  - Update django-modeltranslation from 0.12.2 to 0.13.
  - Update sphinx from 1.7.7 to 2.0.0.
  - Update sphinx-rtd-theme from 0.4.1 to 0.4.3.
  - Update django-debug-toolbar from 1.9.1 to 1.11.
  - Update django-extensions from 2.1.0 to 2.1.6.
  - Update flake8 from 3.5.0 to 3.7.7.
  - Update pydocstyle from 2.1.1 to 3.0.0.
  - Update coverage from 4.5.1 to 4.5.2.
  - Removed gsutil dependency.

4.1.0
==============================================================================

- **Release date:** 24th August 2018
- **Downloads:** `Source downloads are available on GitHub`_

**Summary of changes:**

This release focuses on adding multingual support, with limited versions of the website available in German (Deutsche) and Spanish (Español).

**Changelog:**

- Enable German (Deutsche) language, currently the following pages are available:
  - All basic pages
  - All printables
  - Binary numbers topic: one lesson for 5 to 7 year olds, and 3 curriculum integrations.
- Enable Spanish (Español) language, currently the following pages are available:
  - All basic pages
  - All printables
  - Binary numbers topic: one lesson for 8 to 10 year olds, and 7 curriculum integrations.
- Add Python implementations for many existing programming challenges.
- Modify 'Treasure Hunt' printable to 'Number Hunt', due to redesign of activity for universal use (English language concepts were being used).
- Modify 'Piano Keys' printable to allow different types of key labels.
- Modify printable PDF generation to include all languages.
- Modify printable thumbnail generation to only create English language (add warning when displaying thumbnail in non-English language).
- Use Bootstrap styling for printable generation form.
- Allow custom layout of printables in PDF generation.
- Lock website search to English only, until multilingual search is implemented. `#989 <https://github.com/uccser/cs-unplugged/issues/989>`__
- Add Travis CI status to README for each website. `#1003 <https://github.com/uccser/cs-unplugged/issues/1003>`__
- Add name labels to Travis CI jobs. `#996 <https://github.com/uccser/cs-unplugged/pull/996>`__
- Add configuration file for link checker and translation syncer.
- Package updates:

  - Update django to 1.11.14.
  - Update django-bootstrap-breadcrumbs to 0.9.1.
  - Update django-extensions to 2.1.0.
  - Update django-haystack to 2.8.1.
  - Update django-widget-tweaks to 1.4.2.
  - Update gsutil to 4.33.
  - Update lxml to 4.2.4.
  - Update Pillow to 5.2.0.
  - Update python-markdown-math to 0.5.
  - Update PyYAML to 4.2b4.
  - Update sphinx to 1.7.7.
  - Update sphinx-rtd-theme to 0.4.1.
  - Update tqdm to 4.25.0.
  - Update verto to 0.7.4.
  - Update wheel to 0.31.1.

4.0.2
==============================================================================

- **Release date:** 21st February 2018
- **Downloads:** `Source downloads are available on GitHub`_

**Changelog:**

- Allow searching for general pages and Classic CS Unplugged pages. `#799 <https://github.com/uccser/cs-unplugged/issues/799>`__
- Update navigational bar. `#885 <https://github.com/uccser/cs-unplugged/pull/885>`__
- Remove admin application. `#781 <https://github.com/uccser/cs-unplugged/issues/781>`__
- Update Barcode Checksum Poster design. `#877 <https://github.com/uccser/cs-unplugged/issues/877>`__
- Fix Kidbots illustration. `#875 <https://github.com/uccser/cs-unplugged/issues/875>`__
- Fix positioning of programming challenge language implementation icon.
- Package updates:

  - Update django-haystack to 2.7.0.
  - Update sphinx to 1.7.0.
  - Update coverage to 4.5.1.
  - Add cssselect 1.0.3.

4.0.1
==============================================================================

- **Release date:** 7th February 2018
- **Downloads:** `Source downloads are available on GitHub`_

**Changelog:**

- Fix bug where logo isn't centered in mobile navbar. `#863 <https://github.com/uccser/cs-unplugged/issues/863>`__
- Increase size of pixel painter resource thumbnails. `#866 <https://github.com/uccser/cs-unplugged/issues/866>`__
- Remove redundant headings in related lessons table for printable. `#857 <https://github.com/uccser/cs-unplugged/issues/857>`__
- Redesign topic page to add emphasis to lessons. `#864 <https://github.com/uccser/cs-unplugged/issues/864>`__
- Add 404 page when a page cannot be found. `#851 <https://github.com/uccser/cs-unplugged/issues/851>`__
- Only prepend ``www`` for production website. `#860 <https://github.com/uccser/cs-unplugged/issues/860>`__
- Update repository README file for version ``4.0.0`` release.

4.0.0
==============================================================================

- **Release date:** 5th February 2018
- **Downloads:** `Source downloads are available on GitHub`_

**Summary of changes:**

This is the official release of the rewritten CS Unplugged to the
csunplugged.org domain, while the existing Wordpress site is archived to
classic.csunplugged.org.

This release adds search functionality, while also adding new lessons for
5 to 7 year olds in the searching algorithms topic.
Also included are many small improvements such as better printing of webpages,
clearer video and learning outcome panels, new learning outcomes, and many more.

**Changelog:**

- Add search feature. `#789 <https://github.com/uccser/cs-unplugged/pull/789>`__
- Add sequential and binary search lessons for ages 5 to 7. `#807 <https://github.com/uccser/cs-unplugged/issues/807>`__
- Optimise all images `#801 <https://github.com/uccser/cs-unplugged/pull/801>`__
- Change term 'Resources' to 'Printables'. `#787 <https://github.com/uccser/cs-unplugged/pull/787>`__
- Allow pre-filling of resource forms. `#768 <https://github.com/uccser/cs-unplugged/issues/768>`__
- Update relative link template to allow query parameters.
- Add welcome message to homepage. `#850 <https://github.com/uccser/cs-unplugged/pull/850>`__
- Add print view CSS. `#175 <https://github.com/uccser/cs-unplugged/pull/175>`__
- Add all example classroom videos at appropriate positions. `#842 <https://github.com/uccser/cs-unplugged/pull/842>`__
- Update binary numbers topic description. `#365 <https://github.com/uccser/cs-unplugged/pull/365>`__
- Add learning outcomes for lesson 2 (8-10) for Error Correction and Detection. `#419 <https://github.com/uccser/cs-unplugged/pull/419>`__
- Update the wording on reinforcing sequencing junior. `#630 <https://github.com/uccser/cs-unplugged/pull/630>`__
- Add GitHub Code of Conduct page that points to page in docs. `#829 <https://github.com/uccser/cs-unplugged/pull/829>`__
- Fix bug where learning outcomes were displayed multiple times. `#827 <https://github.com/uccser/cs-unplugged/pull/827>`__
- Prevent line wrapping on tables for programming exercises. `#443 <https://github.com/uccser/cs-unplugged/pull/443>`__
- IE/Edge browser compatibility features. `#824 <https://github.com/uccser/cs-unplugged/pull/824>`__
- Show video symbol on video panels. `#814 <https://github.com/uccser/cs-unplugged/pull/814>`__
- Hide learning outcomes within panel. `#813 <https://github.com/uccser/cs-unplugged/pull/813>`__
- Add URL redirects for Classic CS Unplugged URLs to new subdomain. `#811 <https://github.com/uccser/cs-unplugged/pull/811>`__
- Combine and update changelogs with Classic CS Unplugged. `#820 <https://github.com/uccser/cs-unplugged/pull/820>`__
- Update documentation on Verto 'relative-link' behaviour. `#504 <https://github.com/uccser/cs-unplugged/pull/504>`__
- Rewrite content style guide for external contributors. `#791 <https://github.com/uccser/cs-unplugged/pull/791>`__
- Add pre-requisite lesson for curriculum integrations. `#366 <https://github.com/uccser/cs-unplugged/issues/366>`__ `#849 <https://github.com/uccser/cs-unplugged/pull/849>`__
- Package updates:

  - Update django to 1.11.10.
  - Update verto to 0.7.3.
  - Update Pillow to 5.0.0.
  - Update yattag to 1.10.0.
  - Update django-modeltranslation to 0.12.2.
  - Update sphinx to 1.6.7.
  - Update django-extensions to 1.9.9.
  - Update coverage to 4.5.
  - Add django-haystack 2.6.1.
  - Add Whoosh 2.7.4.
  - Add django-widget-tweaks 1.4.1.

4.0.0-alpha.6.1
==============================================================================

- **Release date:** 22nd December 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Changelog:**

- Fix bug where Cloud SQL Proxy searched for wrong credential file.

4.0.0-alpha.6
==============================================================================

- **Release date:** 22nd December 2017
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
  - Update resources index to use card design for links.
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
  - Add django-bidi-utils 1.0.
  - Update tqdm to 4.19.5.
  - Update django-debug-toolbar 1.9.1.
  - Update django-extensions 1.9.8.
  - Update coverage to 4.4.2
  - Update Django to 1.11.7 and lock Django to 1.11 versions (long term release). `#679 <https://github.com/uccser/cs-unplugged/issues/679>`_ `#743 <https://github.com/uccser/cs-unplugged/issues/743>`_

4.0.0-alpha.5
==============================================================================

- **Release date:** 30th October 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Summary of changes:**

This release improves many backend features, including smarter resource generation,
dynamic resource previews, improved system testing, and bug fixes.

**Changelog:**

- Alter resources to use class based generators. `#636 <https://github.com/uccser/cs-unplugged/issues/636>`_
- Add resource thumbnails on generation page. `#642 <https://github.com/uccser/cs-unplugged/issues/642>`_
- Fix bug where production website is using development static files. `#646 <https://github.com/uccser/cs-unplugged/issues/646>`_
- Fix bug where production static files are not deployed.

4.0.0-alpha.4
==============================================================================

- **Release date:** 17th October 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Summary of changes:**

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

4.0.0-alpha.3
==============================================================================

- **Release date:** 27th June 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Summary of changes:**

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

4.0.0-alpha.2
==============================================================================

- **Release date:** 26th June 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Summary of changes:**

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

4.0.0-alpha.1
==============================================================================

- **Release date:** 20th June 2017
- **Downloads:** `Source downloads are available on GitHub`_

**Summary of changes:**

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

3.2.2
==============================================================================

- **Release date:** 11th January 2016
- **Downloads:** `Word document <https://classic.csunplugged.org/wp-content/uploads/2015/01/CSUnplugged_OS_2015_v3.2.2.docx>`__

**Changelog:**

- Transcript of VP with chatbot reinstated in Turing Test material.

3.2.1
==============================================================================

- **Release date:** 6th January 2016
- **Downloads:** `Word document <https://classic.csunplugged.org/wp-content/uploads/2015/01/CSUnplugged_OS_2015_v3.2.1.docx>`__

**Changelog:**

- Two missing images (first example solution, and ladder networks) added to the Steiner trees activity.

3.2.0
==============================================================================

- **Release date:** 5th January 2016
- **Downloads:** `Word document <https://classic.csunplugged.org/wp-content/uploads/2015/01/CSUnplugged_OS_2015_v3.2.docx>`__

**Changelog:**

- Fixed some incorrect references to activity numbers caused by inserting a new activity.
- Some minor grammar/spelling corrections.

3.1.0
==============================================================================

- **Release date:** March 2015
- **Downloads:** `Word document <https://classic.csunplugged.org/wp-content/uploads/2015/03/CSUnplugged_OS_2015_v3.1.docx>`__ and `PDF document <https://classic.csunplugged.org/wp-content/uploads/2015/03/CSUnplugged_OS_2015_v3.1.pdf>`__

**Changelog:**

- Switched to new logo design.
- Combination of the two parts into one book and introduces version numbering.
- Introduction updated.
- New activity added – Tablets of Stone.
- Minor updates to several activities and explanations.
- Improve Curriculum links (moving away from NZ Curriculum to general curriculum).
- Formatting improvements (fixing page numbers, layout, fonts changed – no more Comic Sans!).
- Fixed footers and copyright information to make creative commons license clearer.

2.5.0
==============================================================================

- **Release date:** 2012
- **Downloads:** `Part 1 Word document <https://classic.csunplugged.org/wp-content/uploads/2015/01/CSUnplugged_OS_Part1_2012.docx>`__ and `Part 2 Word document <https://classic.csunplugged.org/wp-content/uploads/2015/01/CSUnplugged_OS_Part2_2012.doc>`__

**Changelog:**

- Updated version of the teachers’ edition, including the remaining 8 activities from version 1.0.
- Updated a few terms that would no longer be meaningful to students e.g. mention of floppy disks.

2.0.0
==============================================================================

- **Release date:** 2010
- **Downloads:** `Word document <https://classic.csunplugged.org/wp-content/uploads/2015/01/unplugged-v2-teachers-March2010.doc>`__

**Changelog:**

- The first 12 activities of the original version re-written by teachers in 1999/2000 so that it was more suitable for use in the classroom; minor changes were made through to 2010.
- This was eventually released as "open source" i.e. in MS Word, to support creating translations and local versions.
- Updated images and cartoons.
- Included links to the New Zealand curriculum.

1.0.0
==============================================================================

- **Release date:** Mid 1990s
- **Downloads:** `PDF document <https://classic.csunplugged.org/wp-content/uploads/2015/01/unplugged-book-v1.pdf>`__ and `LaTeX source <https://classic.csunplugged.org/wp-content/uploads/2015/01/unplugged-book-v1-latex-source.zip>`__

**Changelog:**

- Original version developed in the mid-1990s, with 20 activities, written by academics primarily for use as an outreach tool.

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
