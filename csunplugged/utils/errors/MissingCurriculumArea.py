from .Error import Error

class MissingCurriculumArea(Error):
    """Exception raised when no learning objective matches a given key.
    """

    def __init__(self, loader, curriculum_area_name):
        super().__init__()
        self.loader = loader
        self.curriculum_area_name = curriculum_area_name
        
    def __str__(self):
        return '\n***************ERROR***************\n' + \
        'Could not find Curriculum Area: {}\n'.format(self.curriculum_area_name) + \
        'Options:\n' + \
            '- Check the curriculum_areas.yaml file for the list of available ' + \
            'Curriculum Areas\n' + \
            '- Check you have included the curriculum_areas.yaml file in ' + \
            'structure.yaml'
