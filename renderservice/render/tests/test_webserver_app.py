import os
import unittest
import tempfile
from render.webserver.app import application

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
        pass

    def test_health_check_recovery(self):
        pass
