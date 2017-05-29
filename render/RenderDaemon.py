"""Render Daemon for collecting and consuming render jobs."""
import os
import time
import signal
import logging
import importlib
from io import BytesIO
from PIL import Image
from base64 import b64encode
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from daemons.prefab.run import RunDaemon
from QueueHandler import QueueHandler
from ResourceManager import ResourceManager

# Daemon Setup and Task Management Constants
PROJECT_NAME = os.getenv("PROJECT_NAME", None)
QUEUE_NAME = os.getenv("QUEUE_NAME", None)
DISCOVERY_URL = os.getenv("API_DISCOVERY_URL", None)
STORAGE_BUCKET = os.getenv("STORAGE_BUCKET", None)

TASK_COUNT = int(os.getenv("TASK_COUNT", 20))
TASK_SECONDS = float(os.getenv("TASK_SECONDS", 15))
TASK_TIME_MULT = float(os.getenv("TASK_TIME_MULT", 1.33))
TASK_RETRY_LIMIT = int(os.getenv("TASK_RETRY_LIMIT", 5))

RENDER_SLEEP_TIME = float(os.getenv("RENDER_SLEEP_TIME", 10))

logger = logging.getLogger(__name__)

# File Generation and Processing Constants
MM_TO_PIXEL_RATIO = 3.78
A4_MM_SCALE = 267
LETTER_MM_SCALE = 249


def handle_timelimit_exceeded():
    """Raise the timeout exception when SIGALRM signal is caught."""
    raise TimeoutError("Timelimit exceeded.")


class RenderDaemon(RunDaemon):
    """A daemon that processes tasks related to the rendering pipeline."""

    def __init__(self, *args, **kwargs):
        """Create a Render Daemon.

        Assumes that any SIGALRM signals are sent by itself for
        timeout exceptions.
        """
        super(RenderDaemon, self).__init__(*args, **kwargs)
        self.handle(signal.SIGALRM, handle_timelimit_exceeded)
        self.resource_manager = ResourceManager(STORAGE_BUCKET)
        self.template_environment = Environment(
            loader=FileSystemLoader('/render/templates'),
            autoescape=False
        )
        # Handle SIGUSR1 for closing up for pre-emption.

    def run(self):
        """Consumes jobs and produces rendered documents."""
        queue = QueueHandler(project_name=PROJECT_NAME, taskqueue_name=QUEUE_NAME, discovery_url=DISCOVERY_URL)
        logger.info("Daemon with pid {} running.".format(self.pid))
        while True:
            lease_secs = TASK_COUNT * TASK_SECONDS
            tasks = queue.lease_tasks(tasks_to_fetch=TASK_COUNT, lease_secs=lease_secs)

            for task_descriptor in tasks:
                task_id = task_descriptor["id"]
                retries = task_descriptor["retry_count"]
                timeout_seconds = TASK_SECONDS + TASK_SECONDS * TASK_TIME_MULT * retries

                if retries > TASK_RETRY_LIMIT:
                    pass  # TODO: delete task tell django

                signal.alarm(timeout_seconds)
                try:
                    self.process_task(queue, task_descriptor)
                except Exception as e:
                    queue.update_task(task_id=task_id, new_lease_secs=1)
                    logger.exception("Task {} raise exception with error: {}", task_descriptor["id"], e)

            time.sleep(RENDER_SLEEP_TIME)

    def process_task(self, queue, task_descriptor):
        """Process the given task, then delete it.

        Render tasks produce and save out documents.

        Args:
            queue: The taskqueue to delete from.
            task_descriptor: The queue task with the user
                definied task as the payload.
        """
        task_id = task_descriptor["id"]
        task = task_descriptor["payload"]
        task_kind = task["kind"]

        filename, document = self.generate_resource_pdf(task)

        if task_kind == "task#render":
            try:
                # TODO: save then delete
                queue.delete_task(task_id)
            except TimeoutError as e:
                # TODO: ensure saved and deleted
                queue.delete_task(task_id)
        else:
            raise Exception("Unrecognized task: {}.".format(task_kind))

    # Task needs:

    def generate_resource_pdf(self, task):
        """Return a response containing a generated PDF resource.

        Args:
            task: A dicitionary of values specifying the task.
                Must have:
                  - filename
                  - header_text
                  - paper_size
                  - copies
                  - resource_slug
                  - resource_name
                  - resource_view
                  - url

        Returns:
            Tuple of PDF file of generated resource and filename.
        """
        if task["paper_size"] is None:
            raise Exception()  # TODO

        module_path = "resources.{}".format(task["resource_view"])
        resource_image_generator = importlib.import_module(module_path)

        context = dict()
        context["resource_name"] = task["resource_name"]
        context["header_text"] = task["header_text"]
        context["url"] = task["url"]

        context["resource_images"] = []
        for copy in range(0, context["copies"]):
            context["resource_images"].append(
                self.generate_resource_image(context, resource_image_generator)
            )

        filename = "{} ({})".format(task["resource_name"], resource_image_generator.subtitle(context))
        context["filename"] = filename

        template_filename = task.get("template", "base-resource-pdf.html")
        css_filename = task.get("css", "static/css/print-resource-pdf.css")

        template = self.template_environment.get_template(template_filename)
        pdf_html = template.render(context)  # TODO: Future consider async
        html = HTML(string=pdf_html, base_url=task["base_url"])
        css_string = self.resource_manager.load(css_filename, encoding="UTF-8")
        base_css = CSS(string=css_string)
        return filename, html.write_pdf(stylesheets=[base_css])

    def generate_resource_image(self, task, resource_image_generator):
        """Retrieve image(s) for one copy of resource from resource generator.

        Images are resized to size.

        Args:
            task: The specification of file to generate as a dictionary.
            resource_image_generator: The file generation module.

        Returns:
            List of Base64 strings of a generated resource images for one copy.
        """
        # Get images from resource image creator
        raw_images = resource_image_generator.resource_image(task, self.resource_manager)
        if not isinstance(raw_images, list):
            raw_images = [raw_images]

        # Resize images to reduce file size
        max_pixel_height = 0
        if task["paper_size"].lower() == "a4":
            max_pixel_height = A4_MM_SCALE * MM_TO_PIXEL_RATIO
        elif task["paper_size"].lower() == "letter":
            max_pixel_height = LETTER_MM_SCALE * MM_TO_PIXEL_RATIO
        else:
            raise Exception()  # TODO

        images = []
        for image in raw_images:
            width, height = image.size
            if height > max_pixel_height:
                ratio = max_pixel_height / height
                width *= ratio
                height *= ratio
                image = image.resize((int(width), int(height)), Image.ANTIALIAS)

            # Save image to buffer
            image_buffer = BytesIO()
            image.save(image_buffer, format="PNG")

            # Add base64 of image to list of images
            images.append(b64encode(image_buffer.getvalue()))

        return images
