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
- Markdown file containing name/description.
- Python module for creating the resource pages.
- Thumbnail image.

Each of these are explained in further detail below.
We recommend looking at existing resources to get a clearer picture of how new
resources should look.


YAML file definition
------------------------------------------------------------------------------

Each resource is defined in the YAML file located at:
``csunplugged/resources/content/structure/resources.yaml``.

Each resource requires the following:

-  ``<resource-key>``: This is the key for the resource.

  - ``generator-module``: Python module for generating resource, relative from
    ``csunplugged/resources/generators/`` (for example: ``SortingNetworkResourceGenerator``).
  - ``thumbnail-static-path``: Thumbnail image for the resource, relative from
    ``csunplugged/static/`` (for example:
    ``img/resources/sorting-network/thumbnail.png``).
  - ``copies``: Boolean if the resource should allow multiple copies.
    If each resource is exactly the same, then the value should be set
    to ``false``.)


Markdown file
------------------------------------------------------------------------------

Every resource must have a markdown file containing the name and description
of the resource. This will be parsed by Verto, and must begin with a top level
heading which will be used as the resource name. This file must be named
``<resource-key>.md`` and located in ``csunplugged/resources/content/en``.


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

If specific user options are required for resource generation, the generator class
can implement a function ``get_additional_options(self)`` which must return a dictionary
mapping an option identifier to a ``ResourceParameter`` instance.
For example, a resource subclass may implement the following:

.. code-block:: python

  @classmethod
  def get_additional_options(cls):
      """Additional options for BinaryCardsSmallResourceGenerator."""
      return {
          "number_bits": EnumResourceParameter(
              name="number_bits",
              description=_("Number of Bits"),
              values= {
                  "4": _("Four (1 to 8)"),
                  "8": _("Eight (1 to 128)"),
                  "12": _("Twelve (1 to 2048)")
              },
              default="4"
          ),
          "dot_counts": BoolResourceParameter(
              name="dot_counts",
              description=_("Display Dot Counts"),
              default=True,
          ),

The following ResourceParameter subclasses are available:

  - EnumResourceParameter - One from a set of predefined values
  - BoolResourceParameter - True/False values
  - TextResourceParameter - Freeform text value
  - IntegerResourceParameter - Integer value

Each ResourceParameter class has configurable options which are documented on in the class docstring.
We recommend looking at existing resources to see how the various ResourceParameter classes can be used.

If ``get_additional_options`` is implemented, the ``subtitle`` property method should be overridden.
The method should display the additional options and also call the parent's subtitle result:

.. note::

  The ``subtitle`` method should be declared as a property with ``@property`` and only have one parameter ``self``.

.. function:: subtitle(self)

  Return the subtitle string of the resource.

  Used after the resource name in the filename, and
  also on the resource image.

  :rtype: Text for subtitle (str).

For example, a resource with options ``display_numbers`` and ``black_back`` might implement the following subtitle method

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

If copies are required for the resource, ``COPIES = True`` should be added as a class constant on the subclass.

If custom thumbnails are to be displayed for each resource combination, the ``save_thumbnail`` method can be overridden.

Thumbnail image
------------------------------------------------------------------------------

This image should represent the resource, and be at least 350px high.

Dynamic Text Overlay
==============================================================================
In many cases, resources comprise of a base PNG image with text dynamically overlayed from within the python view, based on a users request.
Cases where this is necessary include:

- Randomly generated numbers or data.
- Text, which must be translated into the user's language.

While the actual text is added dynamically, the layout/colour/font/size of that text on the resource should be determined as part of the design process.
To achieve this, we have developed a pipeline to allow designers to define these text fields in Adobe Illustrator, and export them in an SVG format.
This information can then be used to dynamically render the required text as closely as possible to the intended design. This process is outlined in more detail below, for both developers and designers.

For Designers
------------------------------------------------------------------------------
The following workflow has been designed for Adobe Illustrator. Currently, other graphics software is not supported.

Setting up the document
*******************************************************************************
  1. Create a new layer called ``TEXT`` (Anything on this layer will be ignored during the export to PNG).

Creating a new dynamic text field
*******************************************************************************
  1.  Create a new transparent rectangular text box in the ``TEXT`` layer.
  2.  Add sample text.
  3.  Set font, font size and colour.
  4.  Position and rotate text box as required.
  5.  Expand text box to define the area in which the text will be allowed.
  6.  Give the text box element a unique identifier.

      - This is achieved by expanding the ``TEXT`` layer in the layers panel, and double-clicking on the text box element.
      - The identifier must be unique across all layers.

Notes:
  - Sample text must be added - do not leave the box empty.
  - The colour, font and font size information of the first character in the text will be used.
  - While we strive to match the original design as much as possible during rendering, the result is not exact. Ensure there is some padding around all sides of the text box to allow for this.
  - Text boxes in shapes other than rectangles are currently not supported.
  - During the design process, consider that some languages are written right to left.

Export procedure
*******************************************************************************
Firstly, check that every element in the ``TEXT`` layer has been given a unique, lowercase identifier as outlined above.

Next, resize the artboard to fit to artwork bounds:

  1. Ensure all layers (including the ``TEXT`` layer) are visible.
  2. Click ``Object -> Artboards -> Fit To Artwork Bounds``.

Now export the base PNG image:

  1. Ensure the ``TEXT`` layer is hidden.
  2. Export PNG, ensuring that `Use Artboards` is selected.

Finally, export the SVG file containing the text field information:

  1. Ensure all layers (including the ``TEXT`` layer) are visible.
  2. Click ``File -> Save As``.
  3. Use the same file name (without extension) as was used for the PNG.
  4. Choose ``SVG`` as the format, and select ``Use Artboards``.
  5. Click ``Save``.
  6. In the dropdown for ``CSS Properties``, choose ``Style Attributes``.
  7. Click ``OK``.


For Developers
------------------------------------------------------------------------------

Rendering text into defined text fields (i.e. defined in an SVG file)
*******************************************************************************

To dynamically render text onto the resource, use the TextBoxDrawer class.

.. code-block:: python

  from utils.TextBoxDrawer import TextBoxDrawer

Load the base PNG image, set it up for editing, and then instantiate a TextBoxDrawer object.

.. code-block:: python

  image = Image.open("my_resource.png")
  draw = ImageDraw.Draw(image)
  textbox_drawer = TextBoxDrawer(image, draw, svg_path="my_resource.svg")

Dynamically populate text fields by calling the ``write_text_box`` function.

.. code-block:: python

  textbox_drawer.write_text_box(
      "title",
      "This is some text",
      horiz_just="center",
  )

Notes:
  - Justification information (horizontal and vertical) is not extracted from the original design. The default is top left, but can be overrided using the kwargs ``horiz_just`` and ``vert_just``.
  - Colour, font, and font size information is extracted from the original design, but can also be set with kwargs here. If provided, kwargs will take precedence.
  - See the docstrings in ``TextBoxDrawer.py`` for more detailed information on the options available.

Rendering text without defined text fields (i.e. without an SVG file)
*******************************************************************************

It is also possible to use this class for dynamically rendering text *without* an SVG file to define the parameters of the text fields.

  1. Initialise TextBoxDrawer without an SVG path.
  2. Create an instance of the TextBox class to define the parameters of the text field (this is normally created automatically with the information extracted from the SVG).
  3. Call ``write_text_box`` with the instantiated TextBox object instead of a textbox identifier.

A simple example:

.. code-block:: python

  from utils.TextBoxDrawer import TextBoxDrawer, TextBox

  image = Image.open("my_resource.png")
  draw = ImageDraw.Draw(image)
  textbox_drawer = TextBoxDrawer(image, draw)

  font_path = "static/fonts/PatrickHand-Regular.ttf"
  font_size = 40

  x, y = 100, 200
  width, height = 300, 400

  # Vertices clockwise from top left
  vertices = [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]

  box = TextBox(vertices,
    width,
    height,
    color="#ba325b",
    font_path=font_path,
    font_size=font_size
  )

  textbox_drawer.write_text_box(
    box,
    "This is some text"
  )

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
