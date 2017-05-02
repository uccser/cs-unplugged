from google.appengine.api import taskqueue

class Worker(object):

    def __init__(self):
        self.q = taskqueue.Queue('render-queue')
        self.active = False
        self.lease_length = 60
        self.lease_number = 20

    def __call__(self):
        self.active = True
        while active:
            tasks = q.lease_tasks(lease_length, lease_number)
            for task in tasks:
                print(task.payload)
            q.delete_tasks(tasks)
