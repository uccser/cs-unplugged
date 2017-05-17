"""Webserver for the render service."""

import os
import logging
import json
from flask import Flask

from apiclient.discovery import build, HttpError
from base64 import b64encode

DEBUG = not int(os.getenv("FLASK_PRODUCTION", 1))
PORT = int(os.getenv("PORT", 8080))
DISCOVERY_URL = os.getenv("API_DISCOVERY_URL", None)

application = Flask(__name__)
task_api = None


def load_api():
    """TEST METHOD, NOT INVITED TO FUTURE ENDEAVOURS."""
    global task_api
    if task_api is None:
        if DISCOVERY_URL is not None:
            task_api = build("taskqueue", "v1beta2", discoveryServiceUrl=DISCOVERY_URL)
        else:
            task_api = build("taskqueue", "v1beta2")
    return task_api


@application.route("/")
def index():
    """Get an index page describing the service."""
    return "CS-Unplugged - Render Engine"


@application.route("/get/<file>")
def get(file=None):
    """Retrieve a file after generation.

    Args:
        file: An identier associated with the file.
    Returns:
        The file with 200 status or a 204 if not found.
    """
    pass  # TODO


@application.route("/add/<item>")
def add(item=None):
    """TEST METHOD, NOT INVITED TO FUTURE ENDEAVOURS."""
    task_api = load_api()
    try:
        encoded_string = b64encode(item.encode("ascii")).decode()
        task = {
          "kind": "taskqueues#task",
          "queueName": "render-queue",
          "payloadBase64": encoded_string
        }
        insert_request = task_api.tasks().insert(
          project="b~cs-unplugged-develop",
          taskqueue="render-queue",
          body=task
        )
        result = insert_request.execute()
        return json.dumps(result), 200
    except HttpError as http_error:
        return "Error", 500


@application.route("/list")
def list():
    """TEST METHOD, NOT INVITED TO FUTURE ENDEAVOURS."""
    task_api = load_api()
    try:
        list_request = task_api.tasks().list(
          project="b~cs-unplugged-develop",
          taskqueue="render-queue"
        )
        result = list_request.execute()
        return json.dumps(result), 200
    except HttpError as http_error:
        return "Error", 500


@application.route("/lease")
def lease():
    """TEST METHOD, NOT INVITED TO FUTURE ENDEAVOURS."""
    task_api = load_api()
    try:
        lease_request = task_api.tasks().lease(
          project="b~cs-unplugged-develop",
          taskqueue="render-queue",
          numTasks=1,
          leaseSecs=3600
        )
        result = lease_request.execute()
        return json.dumps(result), 200
    except HttpError as http_error:
        return "Error", 500


@application.errorhandler(500)
def server_error(e):
    """Log and reports back information about internal errors."""
    logging.exception("An error occurred during a request.")
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


@application.route("/_ah/health")
def health_check():
    """Perform a health check.

    This method is to ensure the api and associated processes are
    working correctly.
    """
    return "", 200


if __name__ == "__main__":
    application.run(debug=DEBUG, host="0.0.0.0", port=PORT)
