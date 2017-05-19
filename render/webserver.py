"""Webserver for the render service."""

import os
import logging
from flask import Flask

DEBUG = not int(os.getenv("FLASK_PRODUCTION", 1))
PORT = int(os.getenv("PORT", 8080))

application = Flask(__name__)


@application.route("/")
def index():
    """Get an index page describing the service."""
    return "CS-Unplugged - Render Engine"


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
