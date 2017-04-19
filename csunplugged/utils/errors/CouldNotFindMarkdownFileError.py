from .Error import Error

class CouldNotFindMarkdownFileError(Error):
    '''Raised when no matching Markdown file can be found in the given path
    '''
    
    def __init__(self, md_file_path, config_file_path):
        '''
        '''
        super().__init__()
        self.md_file_path = md_file_path
        self.config_file_path = config_file_path

    def __str__(self):
        self.reference = self.reference_message.format(self.config_file_path)
        return self.base_message.format(self.md_file_path) + \
            self.reference + self.missing_file_suggestions