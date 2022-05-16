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
- We wrap translatable strings in {% trans %} or {% blocktrans trimmed %} tags.
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

Setting Custom Converter Templates
==============================================================================
We use Verto to convert Markdown files to HTML. To override a default Verto
template, add a new HTML file to ``utils/custom_converter_templates/<processor-name>.html``.

The template file name must correspond to the name of a processor in Verto
(for example: ``image.html``, or the name of a supporting template specified in
Verto documentation (for example: ``relative-image-link.html``).
A list of the available processors is available in the `Verto Documentation`_.

.. _django-bootstrap-breadcrumbs: http://django-bootstrap-breadcrumbs.readthedocs.io/en/latest/
.. _Verto Documentation: https://verto.readthedocs.io/en/latest/
