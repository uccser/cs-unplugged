from .Error import Error

class NoHeadingFoundInMarkdownFileError(Error):
    '''Raised when a title cannot be found in a Markdown File
    '''
    
    def __init__(self, md_file_path):
    	super().__init__()
    	self.md_file_path = md_file_path

    def __str__(self):
    	no_heading_message = '\nThe file does not contain a heading.'
    	return self.base_message.format(self.md_file_path) + no_heading_message

