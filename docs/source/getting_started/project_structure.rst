Project structure
###########################################

This page covers the structure of the CS Unplugged project.
The following diagram will be helpful when reading the following sections:

.. include:: ../_static/html_snippets/folder_tree.rst

Repository folder
=================================================

The repository folder (or root folder) contains the following:

- ``csunplugged`` folder

  - This folder contains the Django web system for the CS Unplugged website.
    This includes all raw text content, images, resources, etc.

- ``docs`` folder

  - This folder contains the documentation for the repository (which includes
    the file you are reading now).

- ``subtitles`` folder

  - This folder contains subtitle files for CS Unplugged videos.

- ``README.md``

  - This file contains an introduction and important information for the
    repository.

- ``LICENSE.md``

  - This file details the licenses the repository uses.

- Plus other files used for installation and repository configuration.

csunplugged folder
=================================================

The ``csunplugged`` folder holds the Django web system and is split across
the following folders:

- ``config``

  - This folder holds the settings used by the Django system.
    It's unlikely you'll edit the contents of this folder unless you are
    changing the Django configuration (for example: adding a new application).

Django contains 'applications' which are Python packages that provide
some set of features.
Each large part/chunk of the CS Unplugged is a separate application.
The project currently contains the following applications:

- ``general``

  - This applicate displays webpages for generic pages on the website.
    For example: homepage, about page, contact page, etc.

- ``topics``

  - The core CS Unplugged content is split across topics, with each topic
    containing any combination of unit plans, lessons, follow up activities,
    programming exercises (plugged in activities), and much more.
    This application stores and displays the topics content.

- ``resources``

  - The CS Unplugged project contains custom printable resources that can
    contain randomly generated components and translations.
    This application stores, generates, and displays these resources.

Details on how to modify an application can be found within their relavent
author and developer documentation pages.

The following folders are also required by the Django system:

- ``static``

  - This folder contains non-user-generated media assets (for example:
    images, JavaScript, CSS/SCSS, etc).

- ``templates``

  - This folder contains all the HTML templates for the Django system.

- ``locale``

  - This folder contains translations required for the Django system.
    Translations for ``topics`` are stored within the ``topics/content``.

The following folders are used when the server is running (for example:
a script compiles the SCSS to CSS and saves it to the ``build`` folder for
serving on a webpage).
You should never save anything in these folders, as the contents are often
overwritten and cleared.

- ``build``

  - Contains the generated output of the front-end script (for example:
    compiled and minified CSS and JavaScript, compressed images, etc).

- ``temp``

  - Contains temporary files used in creating generated files for
    ``build`` folder.

The ``csunplugged`` folder also contains the following files:

- ``manage.py``

  - A file created by Django used to manage the Django web system.
    Don't modify the contents of this file.
