from .Error import Error

ERROR_MESSAGE_TEMPLATE = """
Could not find Curriculum Area: {area}

Options:
  - Check the curriculum-areas.yaml file for the list of available
    Curriculum Areas
  - Check you have included the curriculum_areas.yaml file in
    structure.yaml
"""


class MissingCurriculumArea(Error):
    """Exception raised when no learning objective matches a given key.
    """

    def __init__(self, filename, curriculum_area_name):
        super().__init__()
        self.filename = filename
        self.curriculum_area_name = curriculum_area_name

    def __str__(self):
        base_message = self.base_message.format(filename=self.filename)
        return base_message + ERROR_MESSAGE_TEMPLATE.format(area=self.curriculum_area_name)
