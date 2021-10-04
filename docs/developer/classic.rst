Classic Application
##############################################################################

The classic application stores data related to `Classic CS Unplugged <https://classic.csunplugged.org/>`_, are provides redirections to the website for old links and also allows old pages to be available in the website search.

The classic application uses a model to store pages that are available for searching.
More information about why this application has both data in configuration files and in view/url files can be found in the :doc:`search` documentation.

Searchable Classic Pages Configuration File
==============================================================================

- **File Name:** ``classic-pages.yaml``

- **Location:** ``classic/content/``

- **Purpose:** Defines classic pages that should be available for searching.

- **Required Fields:**

  - ``<classic-page-slug>:`` This is the slug for the classic page.
    Each classic page has the following required field:

    - **Required Field:**

      - ``name:`` The name of the page.

      .. note::

        Text values are stored within this file (and not separate language files) because the Classic CS Unplugged website can only guarantee English content.
        These results should not be displayed for other languages.
