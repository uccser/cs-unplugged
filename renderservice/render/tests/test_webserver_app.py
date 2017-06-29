import unittest
import subprocess
from render.webserver.app import application
from render.daemon.utils import get_active_daemon_details, check_pid


class WebserverAppTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index_page(self):
        with application.test_client() as c:
            response = c.get("/")
            self.assertEqual(response.get_data().decode(), "CS-Unplugged - Render Engine")

    def test_health_check(self):
        print()  # print to separate logging messages
        with application.test_client() as c:
            response = c.get("/_ah/health")
            self.assertEqual(response.status_code, 200)

    def test_health_check_recovery(self):
        """This test depends on daemon utils for success."""
        print()  # print to separate logging messages
        # kill daemons
        details = get_active_daemon_details("render")
        number_daemons = len(details)
        for daemon in details:
            args = ["/docker_venv/bin/python", "-m", "render.daemon",
                    "--daemon", str(daemon.number),
                    "stop"]
            p = subprocess.Popen(args,
                                 stdin=subprocess.DEVNULL,
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL)
            returncode = None
            for _ in range(10):
                try:
                    returncode = p.wait(1)
                except subprocess.TimeoutExpired:
                    pass

            if returncode is None:
                p.terminate()
                p.wait(1)

            self.assertEqual(returncode, 0)

        # recover daemons with health check
        with application.test_client() as c:
            response = c.get("/_ah/health")
            self.assertEqual(response.status_code, 200)

        details = get_active_daemon_details("render")
        self.assertEqual(len(details), number_daemons)

        for daemon in details:
            self.assertTrue(check_pid(daemon.pid))
