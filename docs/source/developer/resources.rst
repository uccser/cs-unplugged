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
  - ``generator-module``: Python module for generating resource, relative from
    ``csunplugged/resources/generators/`` (for example: ``SortingNetworkResourceGenerator``).
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

The Python module defined in the YAML file must contain a class inheriting from
``resources.utils.BaseResourceGenerator``.
The Python class must have the same name as the module.

The generator class must contain the following method definition:

.. function:: data(self)

  Create one copy of the resource.

  :rtype: A dictionary or list of dictionaries for each resource page.

    Each dictionary must contain the following keys/value pairs:

    - ``type``: Page type (either ``image`` or ``html``) as a string.
    - ``data``: If ``type`` is ``html``, then a HTML string is expected.
      If type is ``image``, a Pillow Image object is expected.

    If a list of dictionaries is provided (when a resource has more than one
    page), one of the dictionaries must have the key ``thumbnail`` set to ``True``.
    This is used to determine which page is used to create the resource thumbnails.

If required, the generator class can contain the class variable ``additional_valid_options`` containing the dictionary of parameter options for the resource.
For example, a resource may contain the following:

.. code-block:: python

  additional_valid_options = {
      "display_numbers": [True, False],
      "black_back": [True, False],
  }

If ``additional_valid_options`` are given, the ``subtitle`` property method should be overridden.
The method should display the additional options and also call the parent's subtitle result:

.. note::

  The ``subtitle`` method should be declared as a property with ``@property`` and only have one parameter ``self``.

.. function:: subtitle(self)

  Return the subtitle string of the resource.

  Used after the resource name in the filename, and
  also on the resource image.

  :rtype: Text for subtitle (str).

For example, the subtitle method for the ``additional_valid_options`` above could be:

.. code-block:: python

  @property
  def subtitle(self):
      """Return the subtitle string of the resource.

      Used after the resource name in the filename, and
      also on the resource image.

      Returns:
          Text for subtitle (str).
      """
      if self.requested_options["display_numbers"]:
          display_numbers_text = "with numbers"
      else:
          display_numbers_text = "without numbers"

      if self.requested_options["black_back"]:
          black_back_text = "with black back"
      else:
          black_back_text = "without black back"

      text = "{} - {} - {}".format(
          display_numbers_text,
          black_back_text,
          super().subtitle
      )
      return text

If custom thumbnails are to be displayed for each resource combination, the ``save_thumbnail`` method can be overridden.

Thumbnail image
------------------------------------------------------------------------------

This image should represent the resource, and be at least 350px high.

Specific Resource Details
==============================================================================

Pixel Painter
------------------------------------------------------------------------------

**Adding new images**

Each pixel grid page contains 20 rows and 15 columns of pixels.
Therefore when adding new images, the width and height should be multiples of
these numbers for optimal page usage (for example 40 pixels high by 60 pixels wide).

Each image is required to be available in the following variants:

1.  **Black and white**: The image must only contain a grayscale channel, with pixels either being white (255) or black (0).
2.  **Greyscale**: The image must only contain a grayscale channel, and the pixels must be one of the following values:

    - 0
    - 84
    - 168
    - 255

3.  **Colour**: The image must only contain a red, green, and blue channels (no alpha channel).
    Pixels must be one of the following RGB values:

    - 255, 255, 255 - White
    - 0, 0, 0 - Black
    - 255, 0, 0 - Red
    - 255, 143, 0 - Orange
    - 255, 243, 0 - Yellow
    - 76, 219, 5 - Green
    - 0, 162, 255 - Blue
    - 138, 0, 255 - Purple
