import os
import logging
import json
from flask import Flask
from api_data.taskqueue_v1beta2 import taskqueue_v1beta2_api


# FLASK SETUP

ADDRESS = os.getenv("ADDRESS", "queue")
PORT = int(os.getenv("PORT", 5000))
app = Flask(__name__)
app.register_blueprint(taskqueue_v1beta2_api, url_prefix="/taskqueue/v1beta2/projects")


@app.route("/")
def index():
    return "CS-Unplugged - Fake Google TaskQueue"


@app.route("/api/<api>/<version>")
def api(api=None, version=None):
    content = None
    filepath = os.path.join("api_data", "{0}_{1}.api".format(api, version))
    if not os.path.exists(filepath):
        message = "API does not exist for {} version {}.".format(api, version)
        logging.exception(message)
        return message, 404
    elif not os.path.isfile(filepath):
        message = "Server Error: API exists for {} (version {}) but is not file.".format(api, version)
        logging.exception(message)
        return message, 500
    with open(filepath, "r") as f:
        api_json = json.loads(f.read())
        api_json["baseUrl"] = "http://{}:{}/{}/{}/projects/".format(ADDRESS, PORT, api, version)
        api_json["basePath"] = "/{}/{}/projects/".format(api, version)
        api_json["rootUrl"] = "http://{}:{}/".format(ADDRESS, PORT)
        api_json["servicePath"] = "{}/{}/projects/".format(api, version)
        content = json.dumps(api_json)
    return content


@app.errorhandler(500)
def server_error(e):
    logging.exception("An error occurred during a request.")
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
