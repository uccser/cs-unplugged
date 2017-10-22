"""Class for Job Badges resource generator."""

from PIL import Image
from utils.BaseResourceGenerator import BaseResourceGenerator


class JobBadgesResourceGenerator(BaseResourceGenerator):
    """Class for Job Badges resource generator."""

    def data(self):
        """Create data for a copy of the Job Badges resource.

        Returns:
            A dictionary of the one page for the resource.
        """

        image = Image.open("static/img/resources/job-badges/job-badges.png")
        return {"type": "image", "data": image}
