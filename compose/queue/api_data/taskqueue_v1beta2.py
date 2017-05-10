import os
import time
import json
import uuid
import redis
from flask import Blueprint, request

# REDIS SETUP
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=0)
r = redis.StrictRedis(connection_pool=redis_pool)


# Models
def generate_id():
    """
    Returns:
        A string of an uuid that does not exist in the redis server.
    """
    id = str(uuid.uuid4())
    while r.exists(id):
        id = str(uuid.uuid4())
    return id


def now():
    """
    Returns:
        An integer of the current time since the epoch in microseconds.
    """
    return int(time.time() * 10**6)


class Task(object):
    def __init__(self, queueName, payloadBase64, id=None, kind="taskqueues#task",
                 enqueueTimestamp=None, leaseTimestamp=None, retry_count=0, tag=""):
        self.queueName = queueName
        self.payloadBase64 = payloadBase64

        self.id = id if id is not None else generate_id()
        self.enqueueTimestamp = enqueueTimestamp if enqueueTimestamp is not None else now()
        self.leaseTimestamp = leaseTimestamp if leaseTimestamp is not None else now()
        self.kind = kind
        self.retry_count = retry_count
        self.tag = tag

    def _asdict(self):
        return {
            "id": self.id,
            "kind": self.kind,
            "enqueueTimestamp": self.enqueueTimestamp,
            "leaseTimestamp": self.leaseTimestamp,
            "payloadBase64": self.payloadBase64,
            "queueName": self.queueName,
            "retry_count": self.retry_count,
            "tag": self.tag
        }

    def to_json(self):
        return self._asdict()

    @staticmethod
    def from_json(json):
        keys = [
            "id", "kind", "enqueueTimestamp", "leaseTimestamp", "payloadBase64",
            "queueName", "retry_count", "tag"
        ]
        if any(key not in json for key in keys):
            raise Exception("Not all values specified.")
        return Task(**json)


class Stats(object):
    def __init__(self, leasedLastHour=0, leasedLastMinute=0, oldestTask=0, totalTasks=0):
        self.leasedLastHour = leasedLastHour
        self.leasedLastMinute = leasedLastMinute
        self.oldestTask = oldestTask
        self.totalTasks = totalTasks

    def _asdict(self):
        return {
            "leasedLastHour": self.leasedLastHour,
            "leasedLastMinute": self.leasedLastMinute,
            "oldestTask": self.oldestTask,
            "totalTasks": self.totalTasks
        }

    def to_json(self):
        return self._asdict()

    @staticmethod
    def from_json(json):
        keys = [
            "leasedLastHour", "leasedLastMinute", "oldestTask", "totalTasks"
        ]
        if any(key not in json for key in keys):
            raise Exception("Not all values specified.")
        return Stats(**json)


class Acl(object):
    def __init__(self, adminEmails=None, consumerEmails=None, producerEmails=None):
        self.adminEmails = adminEmails if adminEmails is not None else []
        self.consumerEmails = consumerEmails if consumerEmails is not None else []
        self.producerEmails = producerEmails if producerEmails is not None else []

    def _asdict(self):
        return {
            "adminEmails": self.adminEmails,
            "consumerEmails": self.consumerEmails,
            "producerEmails": self.producerEmails
        }

    def to_json(self):
        return self._asdict()

    @staticmethod
    def from_json(json):
        keys = [
            "adminEmails", "consumerEmails", "producerEmails"
        ]
        if any(key not in json for key in keys):
            raise Exception("Not all values specified.")
        return Acl(**json)


class TaskQueue(object):
    def __init__(self, id=None, kind="taskqueues#taskqueue", maxLeases=None, stats=None, acl=None):
        self.id = id if id is not None else generate_id()
        self.kind = kind
        self.maxLeases = maxLeases
        self.stats = stats if stats is not None else Stats()
        self.acl = acl if acl is not None else Acl()

    def _asdict(self):
        return {
            "id": self.id,
            "kind": self.kind,
            "maxLeases": self.maxLeases,
            "stats": self.stats,
            "acl": self.acl
        }

    def to_json(self):
        d = self._asdict()
        d["stats"] = self.stats.to_json()
        d["acl"] = self.acl.to_json()
        return d

    @staticmethod
    def from_json(json):
        keys = [
            "id", "kind", "maxLeases", "stats", "acl"
        ]
        if any(key not in json for key in keys):
            raise Exception("Not all values specified.")

        q = TaskQueue(**json)
        q.stats = Stats.from_json(json["stats"])
        q.acl = Acl.from_json(json["acl"])
        return q


# Taskqueue Blueprint
taskqueue_v1beta2_api = Blueprint("taskqueue.v1beta2", __name__)


@taskqueue_v1beta2_api.route(
    "/<project>/taskqueues/<taskqueue>/tasks",
    methods=["GET", "POST"])
def tasks_api(project=None, taskqueue=None):
    if project is None:
        return "You must specify a project.", 400
    elif taskqueue is None:
        return "You must specify a taskqueue.", 400

    project = project.replace("b~", "")
    queue_key = ".".join([project, taskqueue])

    # Lists all non-deleted Tasks in a TaskQueue, whether or not
    # they are currently leased, up to a maximum of 100.
    if request.method == "GET":
        keys = r.zrange(name=queue_key, start=0, end=99)  # Upto and including
        items = [json.loads(r.get(name=key).decode()) for key in keys]
        return json.dumps({
            "kind": "taskqueues#tasks",
            "items": list(items)
        })

    # Insert a task into an existing queue.
    elif request.method == "POST":
        task_json = json.loads(request.get_data().decode())

        task = Task(**task_json)
        task_string = json.dumps(task.to_json())
        task_id = task.id

        if r.exists(name=task_id):
            return "Task name is invalid", 400

        p = r.pipeline()
        p.zadd(queue_key, task.enqueueTimestamp, task_id)
        p.set(name=task_id, value=task_string)
        p.execute()

        return task_string


@taskqueue_v1beta2_api.route(
    "/<project>/taskqueues/<taskqueue>/tasks/lease",
    methods=["POST"])
def lease_api(project=None, taskqueue=None):
    if project is None:
        return "You must specify a project.", 400
    elif taskqueue is None:
        return "You must specify a taskqueue.", 400

    project = project.replace("b~", "")
    queue_key = ".".join([project, taskqueue])

    # Acquires a lease on the topmost N unowned tasks in the specified
    # queue.
    #     Required query parameters: leaseSecs, numTasks
    if request.method == "POST":
        leaseSecs = request.args.get("leaseSecs")
        numTasks = request.args.get("numTasks")
        if leaseSecs is None or numTasks is None:
            return "Missing leaseSecs and numTasks in query.", 400

        groupByTag = request.args.get("groupByTag", False)
        tag = request.args.get("tag", "")
        if not groupByTag and tag != "":
            return "In query tag specified without groupByTag", 400

        start = 0
        tasks = []
        now_milliseconds = now()
        while len(tasks) < numTasks:
            end = start + numTasks
            keys = r.zrange(name=queue_key, start=start, end=end)

            for key in keys:  # Could become parallelizable
                if not r.exists(name=key):
                    continue

                task_string = r.get(name=key).decode()
                task_json = json.loads(task_string)
                task = Task.from_json(task_json)

                if groupByTag and task.tag != tag:
                    continue

                task.leaseTimestamp = now_milliseconds + int(leaseSecs) * 10**6
                tasks.append(task.to_json())

            start = end + 1

        return json.dumps({
            "kind": "taskqueues#tasks",
            "items": tasks
        }), 200


@taskqueue_v1beta2_api.route(
    "/<project>/taskqueues/<taskqueue>/tasks/<task_id>",
    methods=["GET", "POST", "PATCH", "DELETE"])
def task_api(project=None, taskqueue=None, task_id=None):
    if project is None:
        return "You must specify a project.", 400
    elif taskqueue is None:
        return "You must specify a taskqueue.", 400
    elif task_id is None:
        return "You must specify something to add.", 400

    project = project.replace("b~", "")
    queue_key = ".".join([project, taskqueue])

    # Gets the named task in a TaskQueue.
    if request.method == "GET":
        task_string = r.get(name=task_id).decode()
        return task_string

    # Update the duration of a task lease.
    #     Required query parameters: newLeaseSeconds
    elif request.method == "POST":
        if not r.exists(name=task_id):
            return "Task name is invalid", 400

        task_string = r.get(name=task_id).decode()
        task_json = json.loads(task_string)
        task = Task.from_json(task_json)
        if now() > task.leaseTimestamp:
            return "The task lease has expired", 400

        input_json = json.loads(request.get_data().decode())
        input_task = Task.from_json(input_json)
        if input_task.queueName != taskqueue:
            return "Cannot change task in a different queue", 400
        if input_task.id != task.id:
            return "Task IDs must match", 400

        newLeaseTimestamp = now() + request.args.get("newLeaseSeconds") * 10**6
        task.leaseTimestamp = newLeaseTimestamp
        task_string = json.dumps(task.to_json())

        r.set(name=task_id, value=task_string)
        return task_string

    # Update tasks that are leased out of a TaskQueue.
    #     Required query parameters: newLeaseSeconds
    elif request.method == "PATCH":
        if not r.exists(name=task_id):
            return "Task name is invalid", 400

        task_string = r.get(name=task_id).decode()
        task_json = json.loads(task_string)
        task = Task.from_json(task_json)
        if now() > task.leaseTimestamp:
            return "The task lease has expired", 400

        # minimal only needs queue-name
        input_json = json.loads(request.get_data().decode())
        if input_json["queueName"] != taskqueue:
            return "Cannot change task in a different queue", 400

        newLeaseTimestamp = now() + request.args.get("newLeaseSeconds") * 10**6
        task.leaseTimestamp = newLeaseTimestamp
        task_string = json.dumps(task.to_json())

        r.set(name=task_id, value=task_string)
        return task_string

    # Deletes a task from a TaskQueue.
    elif request.method == "DELETE":
        p = r.pipeline()
        p.zrem(queue_key, task_id)
        p.expire(name=task_id, time=120)
        p.execute()
        return "", 204
