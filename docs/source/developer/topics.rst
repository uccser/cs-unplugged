Topics Application
##############################################################################

The topics application is the main focus of the CS Unplugged website, as it
contains the majority of educational material for the project.

.. note::

  This guide assumes you've read the following documentation:

  - :doc:`../author/topics` - Provides detail on content in topics application
  - :doc:`django_setup` - Provides detail of database structure

In general the topics application is a standard Django application, however it
does store and update it's associated data for it's models uniquely.

Instead of creating and updating model objects through the website
(for example: edited by an online editor),
the objects are updated by a management script.
The content for the topics application is stored within the ``contents/``
directory, as is run for each deployment of the system.
Storing the content within the Git repository gives us greater control on
reviewing and accepted proposed changes to content.

The management command for updating the applications data is ``loadtopics``
(which is automatically called when running ``updatedata``), and can be found at
``management/commands/loadtopics.py``.
