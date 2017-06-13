"""Utility helper functions for working with daemons."""
import os
import re
from collections import namedtuple

PID_DIRECTORY = os.getenv("PID_DIRECTORY", os.path.join(os.getcwd(), "pidstore"))


def check_pid(pid):
    """Check that process is still active.

    Args:
        pid: The process id of the process.
    Returns:
        True if the process exists and is active, False otherwise.
    """
    try:
        os.kill(pid, 0)  # kill actually means send UNIX signal.
    except OSError:
        return False
    else:
        return True


def get_active_daemon_details(daemon):
    """Get the pids of all render daemons.

    Returns:
        An array of namedtuples containing daemon number to pid.
    """
    if not os.path.exists(PID_DIRECTORY):
        return []

    DaemonMetaData = namedtuple("DaemonMetaData", "number, pid")
    regex = re.compile(r"^{}_(?P<number>\d*).pid$".format(daemon))

    details = []
    for filename in os.listdir(PID_DIRECTORY):
        m = regex.match(filename)
        if m is not None:
            filepath = os.path.join(PID_DIRECTORY, filename)
            with open(filepath, 'r') as f:
                pid = int(f.read())
                number = int(m.group('number'))
                details.append(DaemonMetaData(number, pid))
    return details
