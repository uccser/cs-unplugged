import os, redis, logging, json
from flask import Flask, make_response, request

# REDIS SETUP

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=0)
r = redis.Redis(connection_pool=redis_pool)

# FLASK SETUP

app = Flask(__name__)

@app.route('/')
def index():
    return 'CS-Unplugged - Fake Google TaskQueue'

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

@app.route('/<project>/taskqueues/<taskqueue>/tasks',
           methods=['GET', 'POST'])
def task(project=None, taskqueue=None):
    if project is None:
        return "You must specify a project.", 400
    elif taskqueue is None:
        return "You must specify a taskqueue.", 400

    queue_key = ".".join([project, taskqueue])

    # Lists all non-deleted Tasks in a TaskQueue, whether or not
    # they are currently leased, up to a maximum of 100.
    if request.method == 'GET':
        pass

    # Insert a task into an existing queue.
    elif request.method == 'POST':
        key = generate_key()  # TODO: Generate key
        task = request.get_data()  # TODO: Validate task
        r.lpush(queue_key, task)
        r.set(key, task)
        return "Added {}".format(task), 200


@app.route('/<project>/taskqueues/<taskqueue>/tasks/lease',
           methods=['POST'])
def task(project=None, taskqueue=None):
    if project is None:
        return "You must specify a project.", 400
    elif taskqueue is None:
        return "You must specify a taskqueue.", 400

    queue_key = ".".join([project, taskqueue])

    # Acquires a lease on the topmost N unowned tasks in the specified
    # queue.
    #     Required query parameters: leaseSecs, numTasks
    if request.method == 'POST':
        pass

@app.route('/<project>/taskqueues/<taskqueue>/tasks/<task>',
           methods=['GET', 'POST', 'PATCH', 'DELETE'])
def task(project=None, taskqueue=None, task=None):
    if project is None:
        return "You must specify a project.", 400
    elif taskqueue is None:
        return "You must specify a taskqueue.", 400
    elif task is None:
        return "You must specify something to add.", 400

    queue_key = ".".join([project, taskqueue])

    # Gets the named task in a TaskQueue.
    if request.method == 'GET':
        pass

    # Update the duration of a task lease.
    #     Required query parameters: newLeaseSeconds
    elif request.method == 'POST':
        pass

    # Update tasks that are leased out of a TaskQueue.
    #     Required query parameters: newLeaseSeconds
    elif request.method == 'PATCH':
        pass

    # Deletes a task from a TaskQueue.
    elif request.method == 'DELETE':
        pass

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
