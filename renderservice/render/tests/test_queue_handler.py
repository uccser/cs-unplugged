"""Test the file manager for reading of and writing to files."""
import os
import shutil
from render.tests.BaseTest import BaseTest
from render.daemon.QueueHandler import QueueHandler

DISCOVERY_URL = os.getenv("API_DISCOVERY_URL", None)


class QueueHandlerTest(BaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue = QueueHandler(project_name="test_project", taskqueue_name="test_queue", discovery_url=DISCOVERY_URL)
        self.assertEquals(len(self.queue), 0)

    def test_create_task(self):
        task_id = self.queue.create_task(task_payload={"hello": "world"})
        self.assertEquals(len(self.queue), 1)
        self.queue.delete_task(task_id)
        self.assertEquals(len(self.queue), 0)  

    def test_lease_tasks(self):
        pass

    def test_update_lease(self):
        pass
