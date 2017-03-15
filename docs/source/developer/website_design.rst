Website Design (HTML templates/CSS)
##############################################################################

This page covers the HTML templates and CSS styling used for the CS Unplugged
website.

.. warning::

  The current design of the website is a work in progress.

  Expect **everything** to change.

In summary:

- We plan to use Bootstrap 4 for the underlying framework for responsive design.
- We use SCSS for style sheets where possible.
- We use the `django-bootstrap-breadcrumbs`_ package for breadcrumbs on the
  website.

  - This requires templates to inherit from the template one level up on the
    breadcrumb track in order for breadcrumbs to be calculated correctly.
  - This also requires specific objects in the context to be named the same
    as parents in the breadcrumb chain.
    For example: the associated topic is always saved in the template context
    as ``topic``.
  - For complete examples of the breadcrumb package being used, look at the
    templates for the ``topics`` application.

.. _django-bootstrap-breadcrumbs: http://django-bootstrap-breadcrumbs.readthedocs.io/en/latest/
