"""Render Daemon for collecting and consuming render jobs."""
import os
import time
import signal
import logging
from daemons.prefab.run import RunDaemon
from QueueHandler import QueueHandler

PROJECT_NAME = os.getenv("PROJECT_NAME", None)
QUEUE_NAME = os.getenv("QUEUE_NAME", None)
DISCOVERY_URL = os.getenv("API_DISCOVERY_URL", None)

TASK_COUNT = int(os.getenv("TASK_COUNT", 20))
TASK_SECONDS = float(os.getenv("TASK_SECONDS", 15))
TASK_TIME_MULT = float(os.getenv("TASK_TIME_MULT", 1.33))
TASK_RETRY_LIMIT = int(os.getenv("TASK_RETRY_LIMIT", 5))


def handle_timelimit_exceeded():
    """Raise the timeout exception when SIGALRM signal is caught."""
    raise TimeoutError("Timelimit exceeded.")


class RenderDaemon(RunDaemon):
    """A daemon that processes tasks related to the rendering pipeline."""

    def __init__(self, *args, **kwargs):
        """Create a Render Daemon.

        Assumes that any SIGALRM signals are sent by itself for
        timeout exceptions.
        """
        super(RenderDaemon, self).__init__(*args, **kwargs)
        self.handle(signal.SIGALRM, handle_timelimit_exceeded)
        # Handle SIGUSR1 for closing up for pre-emption.

    def run(self):
        """Consumes jobs and produces rendered documents."""
        queue = QueueHandler(project_name=PROJECT_NAME, taskqueue_name=QUEUE_NAME, discovery_url=DISCOVERY_URL)
        logging.log("Daemon with pid {} running.".format(self.pid))
        while True:
            lease_secs = TASK_COUNT * TASK_SECONDS
            tasks = queue.lease_tasks(tasks_to_fetch=TASK_COUNT, lease_secs=lease_secs)

            for task_descriptor in tasks:
                task_id = task_descriptor["id"]
                retries = task_descriptor["retry_count"]
                timeout_seconds = TASK_SECONDS + TASK_SECONDS * TASK_TIME_MULT * retries

                if retries > TASK_RETRY_LIMIT:
                    pass  # TODO

                signal.alarm(timeout_seconds)
                try:
                    self.process_task(queue, task_descriptor)
                except Exception as e:
                    queue.update_task(task_id=task_id, new_lease_secs=1)
                    logging.exception("Task {} raise exception with error: {}", task_descriptor["id"], e)

            time.sleep(5)

    def process_task(self, queue, task_descriptor):
        """Process the given task, then delete it.

        Render tasks produce and save out documents.

        Args:
            queue: The taskqueue to delete from.
            task_descriptor: The queue task with the user
                definied task as the payload.
        """
        task_id = task_descriptor["id"]
        task = task_descriptor["payload"]
        task_kind = task["kind"]

        if task_kind == "task#render":
            try:
                # save then delete
                queue.delete_task(task_id)
            except TimeoutError as e:
                # ensure saved and deleted
                queue.delete_task(task_id)
        else:
            raise Exception("Unrecognized task: {}.".format(task_kind))
