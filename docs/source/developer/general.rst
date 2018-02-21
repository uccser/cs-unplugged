General Application
##############################################################################

The general application manages and serves basic pages for the CS Unplugged website, including (but not limited to):

- Homepage
- About page
- Contact Us page

The general application uses a model to store pages that are available for searching.
More information about why this application has both data in configuration files and in view/url files can be found in the :doc:`search` documentation.

Searchable General Pages Configuration File
==============================================================================

- **File Name:** ``general-pages.yaml``

- **Location:** ``general/content/``

- **Purpose:** Defines general pages that should be available for searching.

- **Required Fields:**

  - ``<general-page-slug>:`` This is the slug for the general page.
    Each general page has a list of required fields:

    - **Required Fields:**

      - ``name:`` The name of the page.

      .. note::

        Text values are stored within this file (and not separate language files) as the names are only used for the English site.
        The retrieval of names will be need to be established for internationalisation of the search feature (see `#798 <https://github.com/uccser/cs-unplugged/issues/798>`_).
        This could be accomplished by parsing template and using ``TranslatableModel``.

      - ``template:`` Filename of template to parse text values from.
      - ``url-name:`` Name of page URL (as specified in the general's URL routing file).
