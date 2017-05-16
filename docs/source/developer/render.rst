Render Service
##############################################################################

Production Infrastructure
******************************************************************************

Render Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Local Infrastructure
******************************************************************************

When running locally using the *docker-compose* environment the Google Task Queue component is replaced with 2 other components a Redis instance and a Queue service.

Queue Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Queue Sevice mimics the `Google Task Queue REST API <https://cloud.google.com/appengine/docs/standard/python/taskqueue/rest/>`_ allowing for a local task queue to be created using the Redis instance.

Important files:

.. code-block:: none

  ├── api_data
  |   ├── __init__.py
  |   ├── taskqueue_v1beta2.py
  |   └── taskqueue_v1beta2.api
  ├── Dockerfile
  ├── gunicorn.conf.py
  ├── requirements.txt
  ├── webserver.py
  └── wsgi.py


- ``api_data``: Contains pairs of API specifications and Python Implementation.

  + ``taskqueue_v1beta2.py``: The python implementation of the taskqueue api for version 1beta2.
  + ``taskqueue_v1beta2.api``: Google API description of the taskqueue REST API from the Google Discovery Service. This file have been modified to remove authorization scoping.

- ``Dockerfile``: Dockerfile for building the webservice.
- ``gunicorn.conf.py``: Gunicorn configuration.
- ``requirements.txt``: Specifies required python modules needed to run the webservice.
- ``webserver.py``: Basic discovery webservice which allows for the loading of custom REST APIs.
- ``wsgi.py``: Gunicorn + Docker entrypoint for the Queue service.

When using the Queue service it is important to note:

  - We do not expect this component to be changed much, and it is likely to be replaced in future by `Google Cloud Tasks <https://cloud.google.com/appengine/docs/flexible/python/migrating>`_.
  - It is not a one-to-one mapping of the Google Task Queue REST API as it does not include ``GET`` on a specific Task Queue.
  - Google error codes are not mimicked as they are undocumented, therefore the Queue Server may have more strict requirements on requests for safety but does not return error codes in the same format as Google.
  - Each API call has been tested with the minimal set of body parameters for complience, but it is also possible that some requests that work locally may not work in production.
  - Complex requests should be `tested here <https://cloud.google.com/appengine/docs/standard/python/taskqueue/rest/tasks/insert#try-it>`_.

Redis Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The REDIS service is currently only used by the Queue service as a datastore for tasks and handling the queuing of tasks. For those who with no knowledge of REDIS should consider it a 'high performance, in-memory database that is a glorified dictionary' for simplicity.

For information on working with REDIS see the `REDIS documentation <https://redis.io/commands>`_.
