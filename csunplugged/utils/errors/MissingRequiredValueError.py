from .Error import Error

class EmptyMarkdownFileError(Exception):
    """Raised when configuration file specifies a key that does not exist.
    """
    
    def __init__(self):
    	super().__init__()
