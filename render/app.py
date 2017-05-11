import os
import logging
from flask import Flask, make_response
from QueueHandler import QueueHandler

from apiclient.discovery import build, HttpError
from base64 import b64encode

DEBUG = not int(os.getenv("FLASK_PRODUCTION", 1))
PORT = int(os.getenv("PORT", 8080))
DISCOVERY_URL = os.getenv("API_DISCOVERY_URL", None)

app = Flask(__name__)


@app.route('/')
def index():
    return "CS-Unplugged - Render Engine"


@app.route("/add/<item>")
def add(item=None):
    # TODO: Event
    try:
        task_api = None
        if DISCOVERY_URL is not None:
            task_api = build("taskqueue", "v1beta2", discoveryServiceUrl=DISCOVERY_URL)
        else:
            task_api = build("taskqueue", "v1beta2")
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
        return "Added", 200
    except HttpError as http_error:
        return "Error", 500


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


@app.route("/_ah/health")
def health_check():
    content = ''
    response = make_response(content, 200)
    return response


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
