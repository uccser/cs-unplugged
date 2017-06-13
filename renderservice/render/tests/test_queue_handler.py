"""Test the file manager for reading of and writing to files."""
import os
import time
from render.tests.BaseTest import BaseTest
from render.daemon.QueueHandler import QueueHandler

DISCOVERY_URL = os.getenv("API_DISCOVERY_URL", None)


class QueueHandlerTest(BaseTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue = QueueHandler(project_name="test_project",
                                  taskqueue_name="test_queue",
                                  discovery_url=DISCOVERY_URL)
        self.clear_queue()
        self.assertEqual(len(self.queue), 0)

    def clear_queue(self):
        while len(self.queue) > 0:
            tasks = self.queue.list_tasks()
            for task in tasks:
                self.queue.delete_task(task["id"])

    def tearDown(self):
        self.clear_queue()

    def test_create_task(self):
        task_id = self.queue.create_task(task_payload={"hello": "world"})
        self.assertEqual(len(self.queue), 1)
        self.queue.delete_task(task_id)
        self.assertEqual(len(self.queue), 0)

    def test_lease_tasks(self):
        num_tasks = 10
        lease_length = 3600

        task_ids = []
        for i in range(num_tasks):
            task_ids.append(self.queue.create_task(task_payload={"task": i}))
        self.assertEqual(len(self.queue), num_tasks)

        # Lease 1 task
        expected_leaseTimestamp = (time.time() + lease_length) * 10 ** 6
        tasks = self.queue.lease_tasks(tasks_to_fetch=1, lease_secs=lease_length)
        self.assertEqual(len(tasks), 1)
        self.assertDictEqual(tasks[0]["payload"], {"task": 0})
        self.assertAlmostEqual(tasks[0]["leaseTimestamp"], expected_leaseTimestamp, -7)  # within 10 seconds difference

        # Lease the rest of the tasks
        expected_leaseTimestamp = (time.time() + lease_length) * 10 ** 6
        tasks = self.queue.lease_tasks(tasks_to_fetch=100, lease_secs=lease_length)
        self.assertEqual(len(tasks), num_tasks - 1)

        payloads = set()
        expected_payloads = { tuple({"task": i}.items()) for i in range(1, num_tasks) }
        for task in tasks:
            payloads.add(tuple(task["payload"].items()))
            self.assertAlmostEqual(task["leaseTimestamp"], expected_leaseTimestamp, -7)
        self.assertSetEqual(payloads, expected_payloads)

        for task_id in task_ids:
            self.queue.delete_task(task_id)
        self.assertEqual(len(self.queue), 0)

    def test_lease_tagged_tasks(self):
        num_generic_tasks = 100
        num_tagged_tasks = 10
        lease_length = 3600
        tag = "Special"

        generic_task_ids = []
        for i in range(num_generic_tasks):
            generic_task_ids.append(self.queue.create_task(task_payload={"task": i}))
        self.assertEqual(len(self.queue), num_generic_tasks)

        tagged_task_ids = []
        for i in range(num_tagged_tasks):
            tagged_task_ids.append(self.queue.create_task(task_payload={"tagged_task": i}, tag=tag))
        self.assertEqual(len(self.queue), num_generic_tasks + num_tagged_tasks)

        expected_leaseTimestamp = (time.time() + lease_length) * 10 ** 6
        tasks = self.queue.lease_tasks(tasks_to_fetch=1000, lease_secs=lease_length, tag=tag)
        self.assertEqual(len(tasks), num_tagged_tasks)

        payloads = set()
        expected_payloads = { tuple({"tagged_task": i}.items()) for i in range(num_tagged_tasks) }
        for task in tasks:
            payloads.add(tuple(task["payload"].items()))
            self.assertAlmostEqual(task["leaseTimestamp"], expected_leaseTimestamp, -7)
        self.assertSetEqual(payloads, expected_payloads)

        for task_id in generic_task_ids + tagged_task_ids:
            self.queue.delete_task(task_id)
        self.assertEqual(len(self.queue), 0)

    def test_update_lease(self):
        payload = {"task": "update"}
        task_id = self.queue.create_task(task_payload=payload)
        self.assertEqual(len(self.queue), 1)

        lease_length = 3600
        expected_leaseTimestamp = (time.time() + lease_length) * 10 ** 6
        tasks = self.queue.lease_tasks(tasks_to_fetch=1000, lease_secs=lease_length)
        self.assertEqual(len(tasks), 1)
        self.assertDictEqual(tasks[0]["payload"], payload)
        self.assertAlmostEqual(tasks[0]["leaseTimestamp"], expected_leaseTimestamp, -7)

        task_id = tasks[0]["id"]
        update_lease_time = 30
        expected_leaseTimestamp = (time.time() + lease_length) * 10 ** 6
        task = self.queue.update_task(task_id=task_id, new_lease_secs=lease_length)
        self.assertAlmostEqual(task["leaseTimestamp"], expected_leaseTimestamp, -7)

        self.queue.delete_task(task_id)
        self.assertEqual(len(self.queue), 0)
