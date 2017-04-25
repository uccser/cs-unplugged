from .Error import Error


class CouldNotFindImageError(Error):
    '''Raised when an image cannot be found in static/ directory
    '''

    def __init__(self, image_path, reference_file_path):
        '''
        '''
        super().__init__()
        self.image_path = image_path
        self.reference_file_path = reference_file_path

    def __str__(self):
        base_message = self.base_message.format(filename=self.image_path)
        reference = self.reference_message.format(reference=self.reference_file_path)
        return base_message + reference + self.missing_file_suggestions
