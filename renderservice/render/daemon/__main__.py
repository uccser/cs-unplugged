"""Module containing daemon logic for consuming and rendering tasks."""
import os
import sys
import logging
import optparse
from logging.handlers import RotatingFileHandler
from render.daemon.utils import PID_DIRECTORY
from render.daemon.RenderDaemon import RenderDaemon

LOG_DIRECTORY = os.getenv("DAEMON_LOG_DIRECTORY", os.path.join(os.getcwd(), "logs"))


def parse_args():
    """Command-line option parser for program control.

    For usage & options, type: "render.py -h".
    """
    opts = optparse.OptionParser(
        usage="{0} [options] input-data-set(s)".format(sys.argv[0]),
        description="Create, modify and kill render daemons.")
    opts.add_option("--daemon",
                    "-d",
                    action="store",
                    type="int",
                    help="The number of the daemon to apply the command too.",
                    default=None)
    options, arguments = opts.parse_args()
    return options, arguments


def setup_logging(options):
    """Initialise the logging configuration.

    Args:
        options: The program options.
    """
    max_log_size = 100 * 1024 * 1024
    logs_directory = LOG_DIRECTORY
    os.makedirs(logs_directory, exist_ok=True)

    logfile = os.path.join(logs_directory, "render_{}.log".format(options.daemon))
    log_formatter = logging.Formatter("%(asctime)-20s %(levelname)s:%(name)-30s Message: %(message)s")

    log_handler = RotatingFileHandler(logfile,
                                      mode="a",
                                      maxBytes=max_log_size,
                                      backupCount=5,
                                      encoding=None,
                                      delay=False)
    log_handler.setFormatter(log_formatter)
    log_handler.setLevel(logging.INFO)

    render_log = logging.getLogger()
    render_log.setLevel(logging.INFO)
    render_log.addHandler(log_handler)


def render_daemon_control(daemon, action):
    """Load and request a daemon to perform an action.

    Do not trust code or the process to be running after this method
    as certain actions such as 'start' cause the main thread to be
    killed.

    Args:
        daemon: An integer representing the daemon number.
        action: A string which is either 'start', 'stop', 'restart'
    """
    # Set-up directories
    pid_directory = PID_DIRECTORY
    os.makedirs(pid_directory, exist_ok=True)
    pidfile = os.path.join(pid_directory, "render_{}.pid".format(daemon))

    d = RenderDaemon(pidfile=pidfile)

    if action == "start":
        d.start()
    elif action == "stop":
        d.stop()
    elif action == "restart":
        d.restart()


if __name__ == "__main__":
    options, arguments = parse_args()
    setup_logging(options)
    action = arguments[0]

    render_daemon_control(options.daemon, action)
