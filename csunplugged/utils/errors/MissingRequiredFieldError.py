from .Error import Error

class MissingRequiredFieldError(Error):
    '''Raised when a required field is missing from a yaml file
    '''
    
    def __init__(self):
    	super().__init__()
