"""Webservice application specification."""
import os
import logging
import subprocess
from flask import Flask
from render.daemon.utils import check_pid, get_active_daemon_details

RENDER_DAEMONS = int(os.getenv("RENDER_DAEMONS", 1))
DEBUG = not int(os.getenv("FLASK_PRODUCTION", 1))
PORT = int(os.getenv("PORT", 8080))

log_formatter = logging.Formatter("%(asctime)s [%(process)s] [%(levelname)s] %(message)s", "[%Y-%m-%d %H:%M:%S %z]")

application = Flask(__name__)
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
log_handler.setFormatter(log_formatter)
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)


@application.route("/")
def index():
    """Get an index page describing the service."""
    return "CS-Unplugged - Render Engine"


@application.errorhandler(500)
def server_error(e):
    """Log and reports back information about internal errors."""
    logger.exception("An error occurred during a request.")
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
    errored = False
    max_waits = 10

    inactive_daemons = {i for i in range(1, RENDER_DAEMONS + 1)}
    daemons = get_active_daemon_details("render")
    for info in daemons:
        if check_pid(info.pid):
            logger.info("Render daemon {} is running.".format(info.number))
            inactive_daemons.discard(info.number)
        else:
            logger.info("Render daemon {} is not running.".format(info.number))

    if len(inactive_daemons) > 0:
        logger.info("Attempting to restart render daemons {}.".format(inactive_daemons))

    processes = []
    for daemon_number in inactive_daemons:
        args = ["/docker_venv/bin/python", "-m", "render.daemon",
                "--daemon", str(daemon_number),
                "start"]
        p = subprocess.Popen(args,
                             stdin=subprocess.DEVNULL,
                             stdout=subprocess.DEVNULL,
                             stderr=None)
        processes.append((daemon_number, p, 0))

    while len(processes) > 0:
        daemon_number, p, retries = processes.pop(0)
        returncode = None

        try:
            returncode = p.wait(0.02)
        except subprocess.TimeoutExpired as e:
            pass

        if returncode is None:
            if retries < max_waits:
                processes.append((daemon_number, p, retries + 1))
            else:
                p.terminate()
                logger.error("Failed to restart render daemon {} too many polls.".format(daemon_number, returncode))
                errored = True
            continue

        if returncode != 0:
            logger.error("Failed to restart render daemon {} with errorcode {}.".format(daemon_number, returncode))
            errored = True
        elif returncode == 0:
            logger.info("Restarted render daemon {}.".format(daemon_number))

    return "", 200 if not errored else 500
