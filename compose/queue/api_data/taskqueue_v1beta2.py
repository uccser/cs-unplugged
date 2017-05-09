import logging, os, time, json, uuid, redis
from flask import Blueprint, make_response, request

# REDIS SETUP
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=0)
r = redis.Redis(connection_pool=redis_pool)

# Models
def generate_id():
    id = str(uuid.uuid4())
    while r.exists(id):
        id = str(uuid.uuid4())
    return id

def now():
    return int(time.time())

class Task(object):
    def __init__(self, queueName, payloadBase64, id=None, kind="taskqueues#task", enqueueTimestamp=None, leaseTimestamp=0, retry_count=0, tag=""):
        self.id = id if id is not None else generate_id()
        self.kind = kind
        self.enqueueTimestamp = enqueueTimestamp if enqueueTimestamp is not None else now()
        self.leaseTimestamp = leaseTimestamp
        self.payloadBase64 = payloadBase64
        self.queueName = queueName
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

    queue_key = ".".join([project, taskqueue])

    # Lists all non-deleted Tasks in a TaskQueue, whether or not
    # they are currently leased, up to a maximum of 100.
    if request.method == "GET":
        keys = r.lrange(queue_key, 0, 100)
        items = filter(None, [r.get(key).decode() for key in keys])
        items = map(lambda x: json.loads(x), items)
        return json.dumps({
            "kind"  : "taskqueues#tasks",
            "items" : list(items)
        })

    # Insert a task into an existing queue.
    elif request.method == "POST":
        task_json = json.loads(request.get_data().decode())

        task = Task(**task_json)
        task_string = json.dumps(task.to_json())
        task_id = task.id

        r.rpush(queue_key, task_id)
        r.set(task_id, task_string)

        return task_string

@taskqueue_v1beta2_api.route(
    "/<project>/taskqueues/<taskqueue>/tasks/lease",
    methods=["POST"])
def lease_api(project=None, taskqueue=None):
    if project is None:
        return "You must specify a project.", 400
    elif taskqueue is None:
        return "You must specify a taskqueue.", 400

    queue_key = ".".join([project, taskqueue])

    # Acquires a lease on the topmost N unowned tasks in the specified
    # queue.
    #     Required query parameters: leaseSecs, numTasks
    if request.method == "POST":
        pass
        # TODO lpop
        # TODO update leased tasks

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

    queue_key = ".".join([project, taskqueue])

    # Gets the named task in a TaskQueue.
    if request.method == "GET":
        task_string = r.get(task_id).decode()
        return task_string

    # Update the duration of a task lease.
    #     Required query parameters: newLeaseSeconds
    elif request.method == "POST":
        task_string = r.get(task_id).decode()
        task_json = json.loads(task_string)
        task = Task.from_json(task_json)

        input_json = json.loads(request.get_data().decode())
        input_task = Task.from_json(input_json)
        task.leaseTimestamp = input_task.leaseTimestamp
        task_string = json.dumps(task.to_json())

        r.set(task_id, task_string)
        return task_string
        #TODO: Expiration
        #TODO: newLeaseSeconds

    # Update tasks that are leased out of a TaskQueue.
    #     Required query parameters: newLeaseSeconds
    elif request.method == "PATCH":
        task_string = r.get(task_id).decode()
        task_json = json.loads(task_string)
        task = Task.from_json(task_json)

        input_json = json.loads(request.get_data().decode())
        task.leaseTimestamp = input_json["leaseTimestamp"]
        task_string = json.dumps(task.to_json())

        r.set(task_id, task_string)
        return task_string
        #TODO: Expiration
        #TODO: newLeaseSeconds
        #TODO: needs only queueName


    # Deletes a task from a TaskQueue.
    elif request.method == "DELETE":
        pass
        # TODO
