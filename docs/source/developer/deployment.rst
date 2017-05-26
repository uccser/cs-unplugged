Deployment
##############################################################################

.. note::

  This page is intended only for staff within the University of Canterbury
  Computer Science Education Research Group, as deployment requires access
  to secret passwords and values.

Requirements
==============================================================================

The project is designed to run on the following systems:

- Google App Engine: Flexible Enviroment.
- Google Cloud SQL: Postgres Database.

  - Several Django models require Postgres specific data types, so the
    system will not function on a different database type (for example: MySQL).

- Static files server.

.. warning::

  The deployment steps for this project are still in development.
  Our goal is to have deployment automated for both production and development
  server.

  The following steps will allow manual deployment to the development server
  available at http://cs-unplugged-develop.appspot.com/.
  This information is not exhaustive, but will provide enough information for
  manual deployment.

  For any manual deployment, you will require the `gcloud`_ tool to be
  installed on your machine, and login with the research group admin Google
  account.

  Manual deployment requires three steps, and all could be done independently
  of one another if required:

  1. Connecting to the Google Cloud SQL database and updating schema and data.
  2. Updating static files on Google Cloud Storage Bucket.
  3. Updating Django application on Google App Engine.

  **Updating database**

  To update the development database, we will setup a SQL proxy to the server,
  and then locally run the Django project that will connect to the server.
  We can then perform the ``migrate`` and ``updatedata`` commands as required.

  Using the `guide for Django on Google App Engine Flexible Environment`_,
  download and setup the SQL proxy.
  You will need to choose a port that the SQL proxy and Django will operate on,
  using ``5433`` should work for most developers.
  Alter the Django configuration to connect using the proxy port, and run the
  system.
  You should be able to then perform the ``migrate`` and ``updatedata``
  commands.

  **Updating static files**

  The simpliest way to upload the static files on the storage bucket, is to
  do the following:

  1.  Delete the following folders if they exist:

    - ``csunplugged/build/``
    - ``csunplugged/staticfiles/``
    - ``csunplugged/temp/``

  2. Run the ``./csu start`` command.
     When the system is started, the static files are generated.
     Once the system has started successfully, run the ``./csu end`` command.

  3. From the root directory, run the following command:

     .. code-block:: bash

       $ gsutil rsync -R csunplugged/staticfiles/ gs://cs-unplugged-develop/static/

  **Updating Django application**

  In the root directory, create a copy of ``app-sample.yaml`` called
  ``app-develop.yaml``, and enter the required values.
  The complete contents for this file is also stored in our password management
  system.

  From the root directory, run the following command:

  .. code-block:: bash

    $ gcloud app deploy app-develop.yaml

.. _gcloud: https://cloud.google.com/sdk/gcloud/
.. _guide for Django on Google App Engine Flexible Environment: https://cloud.google.com/python/django/flexible-environment
