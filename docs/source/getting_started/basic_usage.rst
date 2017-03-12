Basic project commands
##############################################################################

This page covers basic Django and system commands that both authors and
developers will use when using the CS Unplugged system.

.. note::

  We assume by this point you have installed the project, checked the
  setup is working (see :ref:`installation-check-project-setup-works`),
  and also have a basic understanding of the
  :doc:`project structure <project_structure>`.

These commands can be run from terminal from within the ``csunplugged`` folder
(note: this is the ``cs-unplugged/csunplugged`` folder).
When working on the project, you should type the following commands in order
to preview the work you have done.

.. note::

  The following commands must be run with Python 3. If you followed our
  installation guide, we have set ``python`` to refer to Python 3 already.
  Otherwise you will need to use ``python3`` instead of ``python``.

.. _command-manage-migrate:

``python manage.py migrate``
==============================================================================

The Django system powering this project uses model definitions to specify
the structure of the database (for example: a lesson has a name, number,
connected unit plan, etc).
When a developer makes changes to models, Django creates migration files
which are instructions to alter the database to work with the updated models.

This command checks the database on your machine has all the migration files
applied, and applys any migration updates if needed.

.. note::

  If you encounter an issue when running the ``migrate`` command, it's most
  likely because the database wants to make changes that would cause conflicts
  with data that already exists.

  You can clear data from the database, using the following command:

  .. code-block:: bash

    python manage.py flush

  Answer 'yes' to the prompt. If this completes successully, you should be
  able to now run the ``migrate`` command.

Official documentation on the `migrate command`_ can be found on the Django
website.

.. _command-manage-loaddata:

``python manage.py loaddata``
==============================================================================

This command runs loads data from the ``content`` folders found within the
project into the database. For example, if you modify lesson content, you
will need to run this command to update the database with the new content.

The author and developer documentation sections go into more detail about
what data is loaded into the database.

.. _command-manage-runserver:

``python manage.py runserver``
==============================================================================

The command starts a lightweight development web server on your machine. It's
possible to view the server on ``127.0.0.1:8000`` (which is also
``localhost:8000``), but we will run another command first to setup files
required for the website, and view the website in a special development mode.

Official documentation on the `runserver command`_ can be found on the Django
website.

.. _command-gulp:

``gulp``
==============================================================================

We have a `Gulp`_ script to automate a bunch of tasks like copying and
compressing images, compiling and compressing CSS, SCSS, and JavaScript,
rendering Scratch block images, and displaying the website in an browser which
automatically updates on template/CSS changes (note: the browser will not for
content changes as this requires the ``loaddata`` command to be run).

Running ``gulp`` from the command line will start this script, and open your
preferred web browser to the homepage.

-----------------------------------------------------------------------------

You now know the basic commands for using the CS Unplugged system.
When you pull the project initally or whenever you pull updates from other
contributors, you should enter all four commands in order.

Once you have entered these commands, and are making changes to content, you
can leave two terminal windows running, one with ``python manage.py runserver``
running and one with ``gulp`` running.
Each time you wish to preview your changes, open a third terminal and run the
``python manage.py loaddata`` and refresh the web browser.

You are now ready to tackle the documentation for the area you wish to
contribute on.
Head back to the :doc:`documentation homepage <../index>` and choose the documentation related
to the task you wish to contribute to.

.. _migrate command: https://docs.djangoproject.com/en/dev/ref/django-admin/#migrate:
.. _runserver command: https://docs.djangoproject.com/en/dev/ref/django-admin/#runserver
.. _Gulp: http://gulpjs.com/
