from .Error import Error

class MissingConfigFileError(Error):
    '''Raised when a yaml file cannot be found
    '''
    
    def __init__(self):
    	super().__init__()
