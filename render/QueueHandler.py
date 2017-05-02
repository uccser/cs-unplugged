from apiclient.discovery import build, HttpError

class QueueHandler(object):

    def __init__(self, project_name, taskqueue_name):
        self.task_api = build('taskqueue', 'v1beta2')
        self.project_name = project_name
        self.taskqueue_name = taskqueue_name

    def lease_tasks(self, tasks_to_fetch, lease_secs):
        try:
            lease_request = self.task_api.tasks().lease(
                project=self.project_name,
                taskqueue=self.taskqueue_name,
                leaseSecs=lease_secs,
                numTasks=tasks_to_fetch,
                body={}
            )
            result = lease_request.execute()
            return result
        except HttpError as http_error:
            logger.error('Error during lease request: {}'.format(http_error))
            return None

    def delete_tasks(self, task_ids):
        for task_id in task_ids:
            try:
                delete_request = task_api.tasks().delete(
                    project=self.project_name,
                    taskqueue=self.taskqueue,
                    task=task_id
                )
                result = delete_request.execute()
                return result.body == ''
            except HttpError as http_error:
                #logging.error
                return False
