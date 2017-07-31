Resources Application
##############################################################################

.. warning::

  The documentation for this page is still being written.
  This page will also cover:

  - Structure of resource application and model.
  - Creating new resources.

Resource Specification
==============================================================================

Each resource requires the following:

- Definition in YAML file.
- Custom HTML form to allow user generation.
- Python module for creating the resource pages.
- Thumbnail image.

Each of these are explained in further detail below.
We recommend looking at existing resources to get a clearer picture of how new
resources should look.

YAML file definition
------------------------------------------------------------------------------

Each resource is defined in the YAML file located at:
``csunplugged/resources/content/resources.yaml``.

Each resource requires the following:

-  ``<resource-key>``: This is the key for the resource.

  - ``name``: English name of the resource.
  - ``webpage-template``: Template file for the HTML form, relative from
    ``csunplugged/templates/``
    (for example: ``resources/sorting-network.html``).
  - ``generation-view``: Python module for generating resource, relative from
    ``csunplugged/resources/views/`` (for example: ``sorting_network.py``).
  - ``thumbnail-static-path``: Thumbnail image for the resource, relative from
    ``csunplugged/static/`` (for example:
    ``img/resources/sorting-network/thumbnail.png``).
  - ``copies``: Boolean if the resource should allow multiple copies.
    If each resource is exactly the same, then the value should be set
    to ``false``.)

HTML form
------------------------------------------------------------------------------

Each resource has a HTML form to allow the user to customise the resulting
generated resource.
The HTML form file is specified in the YAML definition.

The template should extend ``resources/resource.html``, and contain two blocks:

1. ``block description``: This should contain a paragraph describing the resource.

2. ``block generation_form`` (optional): This should contain any additional
inputs for the generation form (paper size and custom header are already provided).

Python module
------------------------------------------------------------------------------

The Python module must contain the following function definitions:

.. function:: resource(request, resource)

  Create one copy for the resource.

  :param request: HTTP request object (HttpRequest)
  :param resource: Object of resource data (Resource)
  :rtype: A dictionary or list of dictionaries for each resource page.

    Each dictionary must contain the following keys/value pairs:

    - ``type``: Page type (either ``image`` or ``html``) as a string.
    - ``data``: If ``type`` is ``html``, then a HTML string is expected.
      If type is ``image``, a Pillow Image object is expected.

.. function:: subtitle(request, resource)

  Return the subtitle string of the resource.

  Used after the resource name in the filename, and
  also on the resource image.

  :param request: HTTP request object (HttpRequest)
  :param resource: Object of resource data (Resource)
  :rtype: Text for subtitle (str)

.. function:: valid_options()

  Provide dictionary of all valid parameters.

  This excludes the header text parameter.

  :rtype: All valid options (dict)

.. note::

  The following utility modules may be useful:

  - ``utils.retrieve_query_parameter``
  - ``utils.bool_to_yes_no``

Thumbnail image
------------------------------------------------------------------------------

This image should represent the resource, and be at least 350px high.
