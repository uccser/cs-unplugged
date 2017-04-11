from .Error import Error

class MarkdownFileMissingTitleError(Error):
    '''Raised when a title cannot be found in a Markdown File
    '''
    
    def __init__(self):
    	super().__init__()
