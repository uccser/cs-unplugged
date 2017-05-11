import json
import logging
from apiclient.discovery import build, HttpError
from base64 import b64encode, b64decode


def authorize_session():
    pass


def encode_dictionary(dictionary):
    string = json.dumps(dictionary)
    encoded_string = b64encode(string.encode('ascii')).decode()
    return encoded_string


def decode_dictionary(encoded_string):
    string = b64decode(encoded_string).decode()
    dictionary = json.loads(string)
    return dictionary


class QueueHandler(object):

    def __init__(self, project_name, taskqueue_name):
        self.task_api = build('taskqueue', 'v1beta2')
        self.project_name = project_name
        self.taskqueue_name = taskqueue_name

    def create_task(self, task, tag=None):
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
        for task_id in task_ids:
            try:
                delete_request = self.task_api.tasks().delete(
                    project=self.project_name,
                    taskqueue=self.taskqueue,
                    task=task_id
                )
                result = delete_request.execute()
                return result.body == ''
            except HttpError as http_error:
                logging.error('Error during delete request: {}'.format(http_error))
                return False
