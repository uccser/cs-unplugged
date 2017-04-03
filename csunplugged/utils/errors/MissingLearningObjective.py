from .Error import Error

class MissingLearningObjective(Error):
    """Exception raised when no learning objective matches a given key.
    """

    def __init__(self, loader, learning_outcome_slug):
        super().__init__()
        self.loader = loader
        self.learning_outcome_slug = learning_outcome_slug

    def __str__(self):
        return '\n***************ERROR***************\n' + \
        'Could not find Learning Outcome: {}\n'.format(self.learning_outcome_slug) + \
        'Options:\n' + \
            '- Check the learning-outcomes.yaml file for the list of available ' + \
            'Learning Outcome key-value pairs\n' + \
            '- Check you have included the learning-outcomes.yaml file in ' + \
            'structure.yaml'
