"""Render Daemon for collecting and consuming render jobs."""
import os
import time
import random
from daemons.prefab.run import RunDaemon
from QueueHandler import QueueHandler

PROJECT_NAME = os.getenv("PROJECT_NAME", None)
QUEUE_NAME = os.getenv("QUEUE_NAME", None)
DISCOVERY_URL = os.getenv("API_DISCOVERY_URL", None)


class RenderDaemon(RunDaemon):
    def run(self):
        q = QueueHandler(project_name=PROJECT_NAME, taskqueue_name=QUEUE_NAME, discovery_url=DISCOVERY_URL)
        while True:
            task = {
                "test": ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789-=!@#$%^&*()_+") for i in range(20))
            }
            task_id = q.create_task(task_payload=task)
            if task_id is None:
                logging.error("Render {}: Task creation failed.". format(self.pid))
            time.sleep(5)
