"""Test the file manager for reading of and writing to files."""
import logging
import subprocess
from render.tests.BaseTest import BaseTest
from render.daemon.utils import check_pid, get_active_daemon_details

logger = logging.getLogger(__name__)


class DaemonUtilsTest(BaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        cls.daemon_number = 9999
        args = ["/docker_venv/bin/python", "-m", "render.daemon",
                "--daemon", str(cls.daemon_number),
                "start"]
        p = subprocess.Popen(args,
                             stdin=subprocess.DEVNULL,
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.STDOUT)
        cls.returncode = p.wait(10)

    @classmethod
    def tearDownClass(cls):
        args = ["/docker_venv/bin/python", "-m", "render.daemon",
                "--daemon", str(cls.daemon_number),
                "stop"]
        p = subprocess.Popen(args,
                             stdin=subprocess.DEVNULL,
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.STDOUT)
        returncode = p.wait(10)

        if returncode != 0:
            logger.warning("Daemon {} failed to be stopped, please do so manually.")

    def test_get_active_daemon_details(self):
        self.assertEqual(self.returncode, 0)

        details = get_active_daemon_details("render")
        self.assertGreaterEqual(len(details), 1)

        numbers = {daemon.number for daemon in details}
        self.assertTrue(self.daemon_number in numbers)

    def test_check_pid(self):
        self.assertEqual(self.returncode, 0)

        details = get_active_daemon_details("render")
        self.assertGreaterEqual(len(details), 1)

        pid = 0
        for daemon in details:
            if daemon.number == self.daemon_number:
                pid = daemon.pid
        self.assertNotEqual(pid, 0)

        self.assertTrue(check_pid(pid))
        self.assertFalse(check_pid(pid + 8192))
