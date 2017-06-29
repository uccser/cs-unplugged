"""Mimicked API for the Google Taskqueue API v1beta2."""
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
    """Get a unique identifier.

    Returns:
        A string of an uuid that does not exist in the redis server.
    """
    id = str(uuid.uuid4())
    while r.exists(id):
        id = str(uuid.uuid4())
    return id


def now():
    """Get the current time since the epoch.

    Returns:
        An integer of the current time since the epoch in microseconds.
    """
    return int(time.time() * 10**6)


class Task(object):
    """Describes a Google Task.

    With methods for creation from json with error check and automatic
    property building on creation.
    """

    def __init__(self, queueName, payloadBase64, id=None, kind="taskqueues#task",
                 enqueueTimestamp=None, leaseTimestamp=None, retry_count=0, tag=""):
        """Create a new Task object.

        Where only the queueName and payloadBase64 are required to
        make a new object.

        Args:
            queueName: A string of the name of the associated queue.
            payloadBase64: A string of the user-defined payload as a
                string in base64.
            id: A string of the task id, if None is automatically
                generated.
            kind: A string of the kind of object.
            enqueueTimestamp: A long integer of the timesince the epoch the
                task was enqueued.
            leaseTimestamp: A long integer of the time the task becomes
                avaliable for leasing.
            retry_count: The number of times a task was leased.
            tag: The tag associated with the tag.
        """
        self.queueName = queueName
        self.payloadBase64 = payloadBase64

        self.id = id if id is not None else generate_id()
        self.enqueueTimestamp = enqueueTimestamp if enqueueTimestamp is not None else now()
        self.leaseTimestamp = leaseTimestamp if leaseTimestamp is not None else now()
        self.kind = kind
        self.retry_count = retry_count
        self.tag = tag

    def _asdict(self):
        """Convert the current object into a dictionary.

        Returns:
            A dictionary of properties mapped to keys.
        """
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
        """Convert the current object into a json dictionary.

        Returns:
            A dictionary where the keys match the properties of the
            object.
        """
        return self._asdict()

    @staticmethod
    def from_json(json):
        """Create a new Task object from a json dictionary.

        Includes error checking that all the required properties
        are present.

        Args:
            json: A dictionary where keys map to Task object
                properties.
        Returns:
            The converted Task object.
        """
        keys = [
            "id", "kind", "enqueueTimestamp", "leaseTimestamp", "payloadBase64",
            "queueName", "retry_count", "tag"
        ]
        if any(key not in json for key in keys):
            raise Exception("Not all values specified.")
        return Task(**json)


class Stats(object):
    """Describes a Stats object used in the Google TaskQueue.

    The methods for creation from json with error check and automatic
    property building on creation.

    TODO: We currently do not update our stats objects.
    """

    def __init__(self, leasedLastHour=0, leasedLastMinute=0, oldestTask=0, totalTasks=0):
        """Create a new Stats object.

        Args:
            leasedLastHour: The number of tasks leased in the last hour.
            leasedLastMinute: The number of tasks leased in the last minute.
            oldestTask: The age of the oldest task.
            totalTasks: The number of the tasks in the queue.
        """
        self.leasedLastHour = leasedLastHour
        self.leasedLastMinute = leasedLastMinute
        self.oldestTask = oldestTask
        self.totalTasks = totalTasks

    def _asdict(self):
        """Convert the current object into a dictionary.

        Returns:
            A dictionary of properties mapped to keys.
        """
        return {
            "leasedLastHour": self.leasedLastHour,
            "leasedLastMinute": self.leasedLastMinute,
            "oldestTask": self.oldestTask,
            "totalTasks": self.totalTasks
        }

    def to_json(self):
        """Convert the current object into a json dictionary.

        Returns:
            A dictionary where the keys match the properties of the
            object.
        """
        return self._asdict()

    @staticmethod
    def from_json(json):
        """Create a new Stats object from a json dictionary.

        Includes error checking that all the required properties
        are present.

        Args:
            json: A dictionary where keys map to Task object
                properties.
        Returns:
            The converted Stats object.
        """
        keys = [
            "leasedLastHour", "leasedLastMinute", "oldestTask", "totalTasks"
        ]
        if any(key not in json for key in keys):
            raise Exception("Not all values specified.")
        return Stats(**json)


class Acl(object):
    """Describes the user writes over the associated object.

    TODO: We currently do not explicitly use the Acl object.
    """

    def __init__(self, adminEmails=None, consumerEmails=None, producerEmails=None):
        """Create a new Acl object.

        Args:
            adminEmails: A list of administrator emails.
            consumerEmails: A list of emails with access to read/delete.
            producerEmails: A list of emails with access to write.
        """
        self.adminEmails = adminEmails if adminEmails is not None else []
        self.consumerEmails = consumerEmails if consumerEmails is not None else []
        self.producerEmails = producerEmails if producerEmails is not None else []

    def _asdict(self):
        """Convert the current object into a dictionary.

        Returns:
            A dictionary of properties mapped to keys.
        """
        return {
            "adminEmails": self.adminEmails,
            "consumerEmails": self.consumerEmails,
            "producerEmails": self.producerEmails
        }

    def to_json(self):
        """Convert the current object into a json dictionary.

        Returns:
            A dictionary where the keys match the properties of the
            object.
        """
        return self._asdict()

    @staticmethod
    def from_json(json):
        """Create a new Acl object from a json dictionary.

        Includes error checking that all the required properties
        are present.

        Args:
            json: A dictionary where keys map to Task object
                properties.
        Returns:
            The converted Acl object.
        """
        keys = [
            "adminEmails", "consumerEmails", "producerEmails"
        ]
        if any(key not in json for key in keys):
            raise Exception("Not all values specified.")
        return Acl(**json)


class TaskQueue(object):
    """Describes a Google TaskQueue.

    With methods for creation from json with error check and automatic
    property building on creation.

    TODO: Current implementation does not make use of stats and maxLeases etc.
    """

    def __init__(self, id=None, kind="taskqueues#taskqueue", maxLeases=None, stats=None, acl=None):
        """Create a new TaskQueue object.

        Args:
            id: The identifier of the taskqueue, if None is given a
                identifier is generated.
            kind: The kind of the taskqueue.
            maxLeases: The max number of leases an item can take before
                it is removed from the queue.
            stats: An Stats object recording information on the queue.
            acl: An Acl object of Authorised users of the queue.
        """
        self.id = id if id is not None else generate_id()
        self.kind = kind
        self.maxLeases = maxLeases
        self.stats = stats if stats is not None else Stats()
        self.acl = acl if acl is not None else Acl()

    def _asdict(self):
        """Convert the current object into a dictionary.

        Returns:
            A dictionary of properties mapped to keys.
        """
        return {
            "id": self.id,
            "kind": self.kind,
            "maxLeases": self.maxLeases,
            "stats": self.stats,
            "acl": self.acl
        }

    def to_json(self):
        """Convert the current object into a json dictionary.

        Returns:
            A dictionary where the keys match the properties of the
            object.
        """
        d = self._asdict()
        d["stats"] = self.stats.to_json()
        d["acl"] = self.acl.to_json()
        return d

    @staticmethod
    def from_json(json):
        """Create a new TaskQueue object from a json dictionary.

        Includes error checking that all the required properties
        are present.

        Args:
            json: A dictionary where keys map to Task object
                properties.
        Returns:
            The converted TaskQueue object.
        """
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
    "/<project>/taskqueues/<taskqueue>",
    methods=["GET", "POST"])
def taskqueue_api(project=None, taskqueue=None):
    """List details on the given taskqueue.

    Currently stats such as leasedLastMinute, leasedLastHour
    are not tracked as they are not useful.

    Args:
        project: A string of the project to work on.
        taskqueue: A string of the affected taskqueue.

    GET:
        List the details describing the task queue.
    """
    if project is None:
        return "You must specify a project.", 400
    elif taskqueue is None:
        return "You must specify a taskqueue.", 400

    project = project.replace("b~", "")
    queue_key = ".".join([project, taskqueue])

    if request.method == "GET":
        taskqueue_id = "projects/b~{}/taskqueues/{}".format(project, taskqueue)
        response = {
            "kind": "taskqueues#taskqueue",
            "id": taskqueue_id,
        }

        getStats = request.args.get("getStats")
        if getStats:
            totalTasks = r.zcard(queue_key)

            keys = r.zrange(name=queue_key, start=0, end=1)
            oldestTask = 0
            if len(keys) != 0:
                key = keys[0]
                oldestTask = r.zscore(queue_key, key)

            response["stats"] = {
                "totalTasks": totalTasks,
                "oldestTask": oldestTask,
                "leasedLastMinute": 0,
                "leasedLastHour": 0
            }
        return json.dumps(response)
    return "", 404


@taskqueue_v1beta2_api.route(
    "/<project>/taskqueues/<taskqueue>/tasks",
    methods=["GET", "POST"])
def tasks_api(project=None, taskqueue=None):
    """List items or Insert into a given queue.

    Args:
        project: A string of the project to work on.
        taskqueue: A string of the affected taskqueue.

    GET:
        Lists all non-deleted Tasks in a TaskQueue, whether or not
        they are currently leased, up to a maximum of 100.

        Returns:
            A json object containing a kind and items attribute.
            Where items is a list of tasks.

    POST:
        Inserts a task into an existing queue.

        Body:
            Must be a JSON Task object, where only the queueName
            and payloadBase64 need to be specified.
        Returns:
            A json object of the created Task.
    """
    if project is None:
        return "You must specify a project.", 400
    elif taskqueue is None:
        return "You must specify a taskqueue.", 400

    project = project.replace("b~", "")
    queue_key = ".".join([project, taskqueue])

    # Lists all non-deleted Tasks in a TaskQueue, whether or not
    # they are currently leased, up to a maximum of 100.
    if request.method == "GET":
        start = 0
        tasks = []
        numTasks = 100
        while len(tasks) < numTasks:
            tasks_needed = numTasks - len(tasks)
            end = max(start, start + tasks_needed - 1)
            keys = r.zrange(name=queue_key, start=start, end=end)
            if len(keys) == 0:
                break

            for key in keys:  # Could become parallelizable
                task_string = r.get(name=key)
                if task_string is None:
                    continue

                task_string = task_string.decode()
                task_json = json.loads(task_string)
                tasks.append(task_json)

            start = end + 1

        return json.dumps({
            "kind": "taskqueue#tasks",
            "items": tasks
        })

    # Insert a task into an existing queue.
    elif request.method == "POST":
        task_json = json.loads(request.get_data().decode())

        task = Task(**task_json)
        task_string = json.dumps(task.to_json())
        task_id = task.id

        if r.exists(name=task_id):
            return "Task name is invalid.", 400

        p = r.pipeline()
        p.zadd(queue_key, task.enqueueTimestamp, task_id)
        p.set(name=task_id, value=task_string)
        p.execute()

        return task_string


@taskqueue_v1beta2_api.route(
    "/<project>/taskqueues/<taskqueue>/tasks/lease",
    methods=["POST"])
def lease_api(project=None, taskqueue=None):
    """Lease items from the taskqueue.

    Args:
        project: A string of the project to work on.
        taskqueue: A string of the affected taskqueue.

    POST:
        Acquires a lease on the topmost N unowned tasks in the
        specified queue.

        Query:
            leaseSecs: An integer of the number of seconds to lease
                the tasks for.
            numTasks: An integer of the number of tasks to lease.
            groupByTag: (Optional) true or false, determining whether
                to get tasks by tag.
            tag: (Optional) A string specifing which tag leased tasks
                must have.
        Returns:
            A json object containing a kind and items attribute.
            Where items is a list of tasks.
    """
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
            return "In query tag specified without groupByTag.", 400

        # load tag of the oldest task
        if groupByTag and "tag" not in request.args.keys():
            keys = r.zrange(name=queue_key, start=0, end=0)
            if len(keys) == 1:
                key = keys[0]
                task_string = r.get(name=key)
                if task_string is not None:
                    task_string = task_string.decode()
                    task_json = json.loads(task_string)
                    task = Task.from_json(task_json)
                    tag = task.tag

        start = 0
        tasks = []
        now_milliseconds = now()
        numTasks = min(int(numTasks), 1000)
        while len(tasks) < numTasks:
            tasks_needed = numTasks - len(tasks)
            end = max(start, start + tasks_needed - 1)
            keys = r.zrange(name=queue_key, start=start, end=end)
            if len(keys) == 0:
                break

            for key in keys:  # Could become parallelizable
                task_string = r.get(name=key)
                if task_string is None:
                    continue

                task_string = task_string.decode()
                task_json = json.loads(task_string)
                task = Task.from_json(task_json)

                if groupByTag and task.tag != tag:
                    continue

                if task.leaseTimestamp > now_milliseconds:
                    continue

                task.leaseTimestamp = now_milliseconds + int(leaseSecs) * 10**6
                task_json = task.to_json()
                tasks.append(task_json)

                task.retry_count += 1
                task_string = json.dumps(task_json)
                r.set(name=key, value=task_string)

            start = end + 1

        return json.dumps({
            "kind": "taskqueue#tasks",
            "items": tasks
        })


@taskqueue_v1beta2_api.route(
    "/<project>/taskqueues/<taskqueue>/tasks/<task_id>",
    methods=["GET", "POST", "PATCH", "DELETE"])
def task_api(project=None, taskqueue=None, task_id=None):
    """Get, Update, or Delete a task.

    Args:
        project: A string of the project to work on.
        taskqueue: A string of the affected taskqueue.
        task_id: The id of the task to modify.

    GET:
        Gets the named task in a TaskQueue.

        Returns:
            A task json object.

    POST:
        Update the duration of a task lease.

        Query:
            newLeaseSeconds: The number of seconds to complete the
                task from now.
        Body:
            The json object of the task to update.
        Returns:
            The updated json object of the task.

    PATCH:
        Update the duration of a task lease.

        Query:
            newLeaseSeconds: The number of seconds to complete the
                task from now.
        Body:
            The json object of the task to update where the required
            attributes are minimal and only needs queue-name.
        Returns:
            The updated json object of the task.

    DELETE:
        Deletes a task from a TaskQueue.

        Returns:
            A empty success status i.e 204.
    """
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
        task_string = r.get(name=task_id)
        if task_string is None:
            return "Task name does not exist.", 400
        return task_string.decode()

    # Update the duration of a task lease.
    #     Required query parameters: newLeaseSeconds
    elif request.method == "POST":
        newLeaseSeconds = request.args.get("newLeaseSeconds", None)
        if newLeaseSeconds is None:
            return "newLeaseSeconds is required.", 400
        if not newLeaseSeconds.isdecimal():
            return "newLeaseSeconds must be an integer.", 400
        newLeaseSeconds = int(newLeaseSeconds)

        task_string = r.get(name=task_id)
        if task_string is None:
            return "Task name is invalid.", 400

        task_string = task_string.decode()
        task_json = json.loads(task_string)
        task = Task.from_json(task_json)
        if now() > task.leaseTimestamp:
            return "The task lease has expired.", 400

        input_json = json.loads(request.get_data().decode())
        input_task = Task.from_json(input_json)
        if input_task.queueName != taskqueue:
            return "Cannot change task in a different queue.", 400
        if input_task.id != task.id:
            return "Task IDs must match.", 400

        newLeaseTimestamp = now() + newLeaseSeconds * 10**6
        task.leaseTimestamp = newLeaseTimestamp
        task_string = json.dumps(task.to_json())

        r.set(name=task_id, value=task_string)
        return task_string

    # Update tasks that are leased out of a TaskQueue.
    #     Required query parameters: newLeaseSeconds
    elif request.method == "PATCH":
        newLeaseSeconds = request.args.get("newLeaseSeconds", None)
        if newLeaseSeconds is None:
            return "newLeaseSeconds is required.", 400
        if not newLeaseSeconds.isdecimal():
            return "newLeaseSeconds must be an integer.", 400
        newLeaseSeconds = int(newLeaseSeconds)

        task_string = r.get(name=task_id)
        if task_string is None:
            return "Task name is invalid.", 400

        task_string = task_string.decode()
        task_json = json.loads(task_string)
        task = Task.from_json(task_json)
        if now() > task.leaseTimestamp:
            return "The task lease has expired.", 400

        # minimal only needs queue-name
        input_json = json.loads(request.get_data().decode())
        if input_json["queueName"] != taskqueue:
            return "Cannot change task in a different queue.", 400

        newLeaseTimestamp = now() + newLeaseSeconds * 10**6
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
