from .Error import Error

class EmptyMarkdownFileError(Error):
    '''Raised when there is no content (excluding title) in a Markdown File
    '''
    
    def __init__(self, md_file_path):
    	'''
    	'''
    	super().__init__()
    	self.md_file_path = md_file_path

    def __str__(self):
    	empty_file_message = '\nThe file contains no content. ' + \
    	    '\n  Note: A file containting a title and no other content is ' + \
    	    'also considered to be empty.'
    	return self.base_message.format(self.md_file_path) + empty_file_message
