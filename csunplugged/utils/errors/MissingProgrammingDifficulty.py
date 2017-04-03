from .Error import Error

class MissingProgrammingDifficulty(Error):
    """Exception raised when no learning objective matches a given key.
    """

    def __init__(self, loader, programming_difficulty):
        super().__init__()
        self.loader = loader
        self.programming_difficulty = programming_difficulty

    def __str__(self):
        return '\n***************ERROR***************\n' + \
        'Could not find Programming Difficulty: {}\n'.format(
            self.programming_difficulty) + \
        'Options:\n' + \
            '- Check the programming-exercises-structure.yaml file for the list of ' + \
            'available difficulty levels\n' + \
            '- Check you have included the programming-exercises-structure.yaml ' + \
            'file in structure.yaml'
