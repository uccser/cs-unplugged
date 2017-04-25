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

    def __init__(self, loader, programming_difficulty):
        super().__init__()
        self.loader = loader
        self.programming_difficulty = programming_difficulty

    def __str__(self):
        return self.base_message + ERROR_MESSAGE_TEMPLATE.format(difficulty=self.programming_difficulty)
