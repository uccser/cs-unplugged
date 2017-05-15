Render Service
##############################################################################




Local Infrastructure
******************************************************************************

When running locally using the *docker-compose* environment the Google Task Queue component is replaced with 2 other components a Redis instance and a Queue Server.

The Queue Server mimics the `Google Task Queue REST API <https://cloud.google.com/appengine/docs/standard/python/taskqueue/rest/>`_ allowing for a local task queue to be created using the Redis instance.

When using the Queue Server it is important to note:

  - We do not expect this component to be changed much, and it is likely to be replaced in future by `Google Cloud Tasks <https://cloud.google.com/appengine/docs/flexible/python/migrating>`_.
  - It is not a one-to-one mapping of the Google Task Queue REST API as it does not include ``GET`` on a specific Task Queue.
  - Google error codes are not mimicked as they are undocumented, therefore the Queue Server may have more strict requirements on requests for safety but does not return error codes in the same format as Google.
  - Each API call has been tested with the minimal set of body parameters for complience, but it is also possible that some requests that work locally may not work in production.
  - Complex requests should be `tested here <https://cloud.google.com/appengine/docs/standard/python/taskqueue/rest/tasks/insert#try-it>`_.
