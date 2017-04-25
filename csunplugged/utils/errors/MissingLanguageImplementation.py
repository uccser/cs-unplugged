from .Error import Error

ERROR_MESSAGE_TEMPLATE = """
Could not find Language Implementation: {language}

Options:
  - Check the programming-exercises-structure.yaml file for the list of
    available programming languages
  - Check you have included the programming-exercises-structure.yaml
    file in structure.yaml
"""


class MissingLanguageImplementation(Error):
    """Exception raised when no learning objective matches a given key.
    """

    def __init__(self, filename, language):
        super().__init__()
        self.filename = filename
        self.language = language

    def __str__(self):
        base_message = self.base_message.format(filename=self.filename)
        return base_message + ERROR_MESSAGE_TEMPLATE.format(language=self.language)
