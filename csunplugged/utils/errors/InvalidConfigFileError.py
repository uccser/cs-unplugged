from .Error import Error

class InvalidConfigFileError(Error):
    '''Raised when there is no content in a config file
    '''
    
    def __init__(self, yaml_file_path):
    	'''
    	'''
    	super().__init__()
    	self.yaml_file_path = yaml_file_path

    def __str__(self):
    	invalid_message = '\nInvalid configuration file.' + \
            '\n  - Does the file match the expected layout?' + \
            '\n  - Does the file contain at least one key:value pair?' + \
            '\n  - Is the syntax correct? (are you missing a colon somewhere?...)'
    	return self.base_message.format(self.yaml_file_path) + invalid_message
