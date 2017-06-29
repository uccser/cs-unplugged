"""Render Daemon for collecting and consuming render jobs."""
import os
import time
import pickle
import signal
import logging
from base64 import b64encode
from daemons.prefab.run import RunDaemon
from render.daemon.QueueHandler import QueueHandler
from render.daemon.ResourceGenerator import ResourceGenerator

# Daemon Setup and Task Management Constants
PROJECT_NAME = os.getenv("PROJECT_NAME", None)
QUEUE_NAME = os.getenv("QUEUE_NAME", None)
DISCOVERY_URL = os.getenv("API_DISCOVERY_URL", None)

TASK_COUNT = int(os.getenv("TASK_COUNT", 20))
TASK_SECONDS = float(os.getenv("TASK_SECONDS", 15))
TASK_TIME_MULT = float(os.getenv("TASK_TIME_MULT", 1.33))
TASK_RETRY_LIMIT = int(os.getenv("TASK_RETRY_LIMIT", 5))

RENDER_SLEEP_TIME = float(os.getenv("RENDER_SLEEP_TIME", 10))

logger = logging.getLogger(__name__)


def handle_timelimit_exceeded():
    """Raise the timeout exception when SIGALRM signal is caught."""
    raise TimeoutError("Timelimit exceeded.")


class RenderDaemon(RunDaemon, ResourceGenerator):
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
        logger.info("Daemon with pid {} running.".format(self.pid))
        while True:
            lease_secs = TASK_COUNT * TASK_SECONDS
            tasks = queue.lease_tasks(tasks_to_fetch=TASK_COUNT, lease_secs=lease_secs)
            self.process_tasks(tasks, queue)
            time.sleep(RENDER_SLEEP_TIME)

    def process_tasks(self, tasks, queue):
        """Run main loop for determining individual task logic.

        Tasks will be run to recieve a result, saved if necessary
        then deleted. Tasks that return a none result or are
        interupted by an exception will not be deleted and have
        their lease reduced for another daemon. Tasks that have
        surpassed their retry limit will have a failure result
        saved if necessary otherwise they will be deleted.

        Args:
            tasks: A list of json task objects.
            queue: QueueHandler to update and delete tasks from.
        """
        for task_descriptor in tasks:
            task_id = task_descriptor["id"]
            retries = task_descriptor["retry_count"]
            timeout_seconds = TASK_SECONDS + TASK_SECONDS * TASK_TIME_MULT * retries

            result = None
            if retries < TASK_RETRY_LIMIT:
                internal_filename = "{}.pickle".format(task_id)
                signal.alarm(timeout_seconds)
                try:
                    result = self.process_task(task_descriptor)
                except Exception as e:
                    logger.exception("Task {} raise exception with error: {}", task_descriptor["id"], e)
            else:
                result = self.handle_retry_limit(task_descriptor)

            # Task was successful or had too many failures
            if result is not None:
                queue.delete_task(task_id)
            # Task failed and should be retried
            else:
                queue.update_task(task_id=task_id, new_lease_secs=1)

            # Save out documents
            if result is not None and result["kind"] == "result#document":
                data = pickle.dumps(result)
                self.resource_manager.save(internal_filename, data)

    def process_task(self, task_descriptor):
        """Process the given task and get result.

        Render tasks produce and save out documents.

        Args:
            task_descriptor: The queue task with the user
                definied task as the payload.
        Returns:
            A dictionary of the result.
        """
        task = task_descriptor["payload"]
        task_kind = task["kind"]
        result = None

        if task_kind == "task#render":
            filename, document = self.generate_resource_pdf(task)
            result = {
                "kind": "result#document",
                "success": True,
                "filename": filename,
                "document": b64encode(document)
            }
        else:
            raise Exception("Unrecognized task: {}.".format(task_kind))
        return result

    def handle_retry_limit(self, task_descriptor):
        """Process the given task and get result.

        Render tasks produce and save out documents.

        Args:
            task_descriptor: The queue task with the user
                definied task as the payload.
        Returns:
            A dictionary of the result.
        """
        task = task_descriptor["payload"]
        task_kind = task["kind"]
        result = dict()  # result should never be None

        if task_kind == "task#render":
            result = {
                "kind": "result#document",
                "success": False,
                "filename": None,
                "document": None
            }
        return result
