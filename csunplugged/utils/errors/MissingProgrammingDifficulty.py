from .Error import Error

ERROR_MESSAGE_TEMPLATE = """
Could not find Programming Difficulty: {difficulty}

Options:
  - Check the programming-exercises-structure.yaml file for the list of
    available difficulty levels
  - Check you have included the programming-exercises-structure.yaml
    file in structure.yaml
"""


class MissingProgrammingDifficulty(Error):
    """Exception raised when no learning objective matches a given key.
    """

    def __init__(self, filename, programming_difficulty):
        super().__init__()
        self.filename = filename
        self.programming_difficulty = programming_difficulty

    def __str__(self):
        base_message = self.base_message.format(filename=self.filename)
        return base_message + ERROR_MESSAGE_TEMPLATE.format(difficulty=self.programming_difficulty)
