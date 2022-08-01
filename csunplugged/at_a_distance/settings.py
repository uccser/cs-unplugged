"""Settings for the at a distance application."""

import os.path
from django.conf import settings


AT_A_DISTANCE_FILE_GENERATION_LOCATION = os.path.join(
    str(settings.ROOT_DIR.path("build")),
    "slides",
)

AT_A_DISTANCE_INTRODUCTION_FILENAME = 'introduction.md'
AT_A_DISTANCE_SUPPORTING_RESOURCES_FILENAME = 'supporting-resources.yaml'
AT_A_DISTANCE_SLIDES_TEMPLATE_BASE_PATH = 'at_a_distance/lesson-slides'

AT_A_DISTANCE_SLIDE_RESOLUTION_HEIGHT = "1080"
AT_A_DISTANCE_SLIDE_RESOLUTION_WIDTH = "1920"

# Settings computed from above settings
AT_A_DISTANCE_SLIDE_RESOLUTION = f'{AT_A_DISTANCE_SLIDE_RESOLUTION_WIDTH}x{AT_A_DISTANCE_SLIDE_RESOLUTION_HEIGHT}'