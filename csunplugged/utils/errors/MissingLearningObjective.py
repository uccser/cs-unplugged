from .Error import Error

ERROR_MESSAGE_TEMPLATE = """
Could not find Learning Outcome: {slug}

Options:
  - Check the learning-outcomes.yaml file for the list of available
    Learning Outcome key-value pairs.
  - Check you have included the learning-outcomes.yaml file in
    structure.yaml
"""


class MissingLearningObjective(Error):
    """Exception raised when no learning objective matches a given key.
    """

    def __init__(self, filename, learning_outcome_slug):
        super().__init__()
        self.filename = filename
        self.learning_outcome_slug = learning_outcome_slug

    def __str__(self):
        base_message = self.base_message.format(filename=self.filename)
        return base_message + ERROR_MESSAGE_TEMPLATE.format(slug=self.learning_outcome_slug)
