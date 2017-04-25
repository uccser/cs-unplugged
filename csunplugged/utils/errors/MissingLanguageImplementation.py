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

    def __init__(self, loader, language):
        super().__init__()
        self.loader = loader
        self.language = language

    def __str__(self):
        return self.base_message + ERROR_MESSAGE_TEMPLATE.format(language=self.language)
