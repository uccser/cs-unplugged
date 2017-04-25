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
        base_message = self.base_message.format(filename=self.md_file_path)
        reference = self.reference_message.format(reference=self.config_file_path)
        return base_message + reference + self.missing_file_suggestions
