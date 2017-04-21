from .Error import Error

class EmptyConfigFileError(Error):
    '''Raised when there is no content in a config file
    '''
    
    def __init__(self, yaml_file_path):
    	'''
    	'''
    	super().__init__()
    	self.yaml_file_path = yaml_file_path

    def __str__(self):
    	empty_file_message = '\nA config file cannot be empty'
    	return self.base_message.format(self.yaml_file_path) + empty_file_message
