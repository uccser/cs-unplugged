from .Error import Error

ERROR_MESSAGE = "\nA config file cannot be empty.\n"


class EmptyConfigFileError(Error):
    '''Raised when there is no content in a config file
    '''

    def __init__(self, yaml_file_path):
        '''
        '''
        super().__init__()
        self.yaml_file_path = yaml_file_path

    def __str__(self):
        return self.base_message.format(filename=self.yaml_file_path) + ERROR_MESSAGE
