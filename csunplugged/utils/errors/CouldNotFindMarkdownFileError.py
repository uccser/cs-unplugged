from .Error import Error

class CouldNotFindMarkdownFileError(Error):
    '''Raised when no matching Markdown file can be found in the given path
    '''
    
    def __init__(self):
    	super().__init__()
