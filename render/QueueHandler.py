"""Handles transactions with the taskqueue api."""
import json
import logging
from apiclient.discovery import build, HttpError
from base64 import b64encode, b64decode


def authorize_session():
    """Authorize for taskqueue transactions.

    Returns:
        Something in future!
    """
    pass  # TODO


def encode_dictionary(dictionary):
    """Encode a dictionary into a base64 string.

    Args:
        dictionary: A python dictionary to convert.
    Returns:
        The encoded string.
    """
    string = json.dumps(dictionary)
    encoded_string = b64encode(string.encode('ascii')).decode()
    return encoded_string


def decode_dictionary(encoded_string):
    """Decode a base64 string into a dictionary.

    Args:
        encoded_string: A base64 string to decode.
    Returns:
        A python dictionary deserialized from the string.
    """
    string = b64decode(encoded_string).decode()
    dictionary = json.loads(string)
    return dictionary


class QueueHandler(object):
    """Handles transactions with the taskqueue api."""

    def __init__(self, project_name, taskqueue_name):
        """Create a new QueueHandler.

        Args:
            project_name: The project the taskqueue belongs to.
            taskqueue_name: The name of the taskqueue.
        """
        self.task_api = build('taskqueue', 'v1beta2')
        self.project_name = project_name
        self.taskqueue_name = taskqueue_name

    def create_task(self, task, tag=None):
        """Create a new task and places it on the taskqueue.

        Args:
            task: A dicitonary describing the task.
            tag: A tag attached to the task.
        Returns:
            The task id of the created task, otherwise None if error.
        """
        try:
            task = {
                "kind": "taskqueues#task",
                "queueName": self.taskqueue_name,
                "payloadBase64": encode_dictionary(task)
            }
            if tag is not None:
                task["tag"] = tag

            insert_request = self.task_api.tasks().insert(
                project=self.project_name,
                taskqueue=self.taskqueue_name,
                body=task
            )
            result = insert_request.execute()
            return result['id']
        except HttpError as http_error:
            logging.error('Error during insert request: {}'.format(http_error))
            return None

    def lease_tasks(self, tasks_to_fetch, lease_secs):
        """Lease tasks from the taskqueue.

        Args:
            tasks_to_fetch: The number of tasks to fetch.
            lease_secs: The number of seconds to lease for.
        Returns:
            A Google Task as a dicitonary with the user defined
            task (dictionary) under that 'task' key.
        """
        try:
            tasks = []
            lease_request = self.task_api.tasks().lease(
                project=self.project_name,
                taskqueue=self.taskqueue_name,
                leaseSecs=lease_secs,
                numTasks=tasks_to_fetch
            )
            result = lease_request.execute()
            if result["kind"] == "taskqueue#tasks":
                for task in result['items']:
                    task['task'] = decode_dictionary(result['payloadBase64'])
                    tasks.append(task)
            elif result["kind"] == "taskqueue#task":
                task['task'] = decode_dictionary(result['payloadBase64'])
                tasks.append(task)
            return tasks
        except HttpError as http_error:
            logging.error('Error during lease request: {}'.format(http_error))
            return None

    def delete_tasks(self, task_ids):
        """Delete tasks from the taskqueue.

        Args:
            task_ids: An array of tasks ids to be deleted.
        Returns:
            An array of booleans determining if the task was
            deleted successfully.
        """
        is_deleted = []
        for task_id in task_ids:
            try:
                delete_request = self.task_api.tasks().delete(
                    project=self.project_name,
                    taskqueue=self.taskqueue,
                    task=task_id
                )
                result = delete_request.execute()
                is_deleted.append(result.body == '')
            except HttpError as http_error:
                logging.error('Error during delete request: {}'.format(http_error))
                is_deleted.append(False)
        return is_deleted
