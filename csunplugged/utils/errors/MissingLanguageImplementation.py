from .Error import Error

class MissingLanguageImplementation(Error):
    """Exception raised when no learning objective matches a given key.
    """

    def __init__(self, loader, language):
        super().__init__()
        self.loader = loader
        self.language = language

    def __str__(self):
        return '\n***************ERROR***************\n' + \
        'Could not find Language Implementation: {}\n'.format(self.language) + \
        'Options:\n' + \
            '- Check the programming-exercises-structure.yaml file for the list of ' + \
            'available programming languages\n' + \
            '- Check you have included the programming-exercises-structure.yaml ' + \
            'file in structure.yaml'
