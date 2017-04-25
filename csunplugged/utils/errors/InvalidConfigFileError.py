from .Error import Error

ERROR_MESSAGE = """
Invalid configuration file.

Options:
  - Does the file match the expected layout?
  - Does the file contain at least one key:value pair?
  - Is the syntax correct? (are you missing a colon somewhere?)
"""


class InvalidConfigFileError(Error):
    '''Raised when there is no content in a config file
    '''

    def __init__(self, yaml_file_path):
        '''
        '''
        super().__init__()
        self.yaml_file_path = yaml_file_path

    def __str__(self):
        return self.base_message.format(filename=self.yaml_file_path) + ERROR_MESSAGE
