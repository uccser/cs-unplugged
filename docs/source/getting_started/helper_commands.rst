Helper Commands for Developing
##############################################################################

.. note::

  We assume by this point you have installed the project, checked the
  setup is working (see :ref:`installation-check-project-setup-works`),
  and also have a basic understanding of the
  :doc:`project structure <project_structure>`.

The CS Unplugged project uses many systems (Django, Docker, Gulp, etc) to run,
so we have written a script for running groups of commands for running the
system while developing.

The script is called ``csu`` and can be found in the ``cs-unplugged`` folder
of the repository.
To run this script, open a terminal window in the directory and enter the
following command (you don't need to enter the ``$`` character, this shows
the start of your terminal prompt):

.. code-block:: bash

    $ ./csu [COMMAND]

Where ``[COMMAND]`` is a word from the list below:

- :ref:`build`
- :ref:`clean`
- :ref:`dev`
- :ref:`end`
- :ref:`help`
- :ref:`restart`
- :ref:`start`
- :ref:`update`
- :ref:`wipe`

All users of the project (content and technical developers) should become
familiar with the following commands:

- :ref:`start`
- :ref:`end`
- :ref:`build`
- :ref:`update`

Technical developers should also understand the ``dev`` command.

-----------------------------------------------------------------------------

.. _build:

``build``
==============================================================================

Running ``./csu build`` will build or rebuild the Docker images that are
required for the CS Unplugged system.

-----------------------------------------------------------------------------

.. _clean:

``clean``
==============================================================================

Running ``./csu clean`` deletes 'dangling' Docker images left over from builds,
which will free up hard drive space.

-----------------------------------------------------------------------------

.. _dev:

``dev``
==============================================================================

The ``./csu dev [DEV_COMMAND]`` command runs developer tasks, where
``[DEV_COMMAND]`` is the name of developer command.
Run ``./csu help`` to see a list of developer commands.

-----------------------------------------------------------------------------

.. _end:

``end``
==============================================================================

Running ``./csu end`` will stop any containers which are currently running,
this usually takes 10 to 20 seconds.

-----------------------------------------------------------------------------

.. _help:

``help``
==============================================================================

Running ``./csu help`` displays brief help text for the script.
More details for each command can be found on this page.

-----------------------------------------------------------------------------

.. _restart:

``restart``
==============================================================================

Running ``./csu restart`` is a shortcut for running:

- ``./csu end``
- ``./csu start``

More details for each command can be found on this page.

-----------------------------------------------------------------------------

.. _start:

``start``
==============================================================================

Running ``./csu start`` starts the development environment.
When you run this command for the first time on a computer it will also run
``./csu build`` to build the system Docker images.
This can take some time, roughly 15 to 30 minutes, depending on your computer
and internet speed.
Images are only required to be built once, unless the image specifications
change (you can rebuild the images with ``./csu build``).
Once the images are built, the script will run these images in containers.

Once the development environment is operational, the script will perform the
following tasks:

- Start the Django website system
- Start the Nginx server to display the website and static files
- Start the database server
- Update the database with the required structure (known as the schema)
- Load the CS Unplugged content into the database
- Create the required static files

Once the script has performed all these tasks, the script will let you know
the website is ready.
Open your preferred web browser to the URL ``localhost`` to view the website.

-----------------------------------------------------------------------------

.. _update:

``update``
==============================================================================

Running ``./csu update`` runs the Django ``makemigratations`` and ``migrate``
commands for updating the database schema, and then runs the custom
``updatedata`` command to load the topics content into the database.
It also runs the ``static`` command to generate static files.

If changes are made to the topics content when the system is running, this
command needs to be run to view the new changes on the website.

-----------------------------------------------------------------------------

.. _wipe:

``wipe``
==============================================================================

Running ``./csu wipe`` delete all Docker containers and images on your computer.
Once this command has be run, a full download and rebuild of images is
required to run the system (can be triggered by the ``build`` or ``start``
commands).

-----------------------------------------------------------------------------

You now know the basic commands for using the CS Unplugged system.
You are now ready to tackle the documentation for the area you wish to
contribute on.
Head back to the :doc:`documentation homepage <../index>` and choose the documentation related
to the task you wish to contribute to.
