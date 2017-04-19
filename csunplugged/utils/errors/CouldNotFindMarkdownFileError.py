from .Error import Error

class CouldNotFindMarkdownFileError(Error):
    '''Raised when no matching Markdown file can be found in the given path
    '''
    
    def __init__(self, md_file_path, config_file_path):
    	super().__init__()
    	self.md_file_path = md_file_path
    	self.config_file_path = config_file_path

    def __str__(self):
    	return '\n' + \
    	'\n****************************ERROR****************************' + \
    	'\nFile: {}'.format(self.md_file_path) + \
    	'\nReferenced in: {}'.format(self.config_file_path) + \
    	'\n  - Did you spell the name of the file correctly?' + \
    	'\n  - Does the file exist?'
