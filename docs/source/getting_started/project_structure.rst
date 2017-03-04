Understanding the project structure
###########################################

This page covers the structure of the CS Unplugged project.

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

Introduction to be added.

- ``static``

  - Description to be added.

- ``templates``

  - Description to be added.

Introduction to be added.

- ``locale``

  - Description to be added.

Introduction to be added.

- ``build``

  - Description to be added.

- ``temp``

  - Description to be added.

Introduction to be added.

- ``manage.py``

  - Description to be added.
