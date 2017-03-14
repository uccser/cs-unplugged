Django setup
##############################################################################

This page covers the configuration of Django for this project.

Django overview
==============================================================================

We aim to create and clear Django system for ease of development.
We are using some advised patterns and practices from
`Two Scoops of Django - Best Practices for Django 1.8`_, which include (but is
not limited to the following):

- Locking versions of dependencies.
- Django secret settings are loaded from environment variables.
- All templates are located in the ``templates/`` directory.
- The base Django directory, containing ``settings.py`` and base ``urls.py`` is
  called ``config/``.

The Django system currently contains the following applications:

- ``general/`` - For general website pages (for example: home, about, etc).
- ``topics/`` - For topics content (for example: lessons, follow up activities,
  programming exercises, etc).
- ``resources/`` - For translatable PDF resources with random elements.

Database structure
==============================================================================

The following image shows the relationships between models across all
applications within the database.

.. The following image can copied for be edits here: https://goo.gl/kcycns
.. image:: ../_static/img/database_overview_diagram.svg
  :alt: A diagram detailing the general structure of the database

.. note::

  **Lesson** and **Programming Exercise Language Implementation** models have
  the parent's **Topic** saved directly within their model.

The rest of the :doc:`index` will inform you of how to develop the
applications and other components of the CS Unplugged project.

.. _Two Scoops of Django - Best Practices for Django 1.8: https://www.twoscoopspress.com/products/two-scoops-of-django-1-8
