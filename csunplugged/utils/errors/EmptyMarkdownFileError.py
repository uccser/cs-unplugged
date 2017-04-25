from .Error import Error

ERROR_MESSAGE = """
The file contains no content.

Note: A file containting a title and no other content is
also considered to be empty.
"""


class EmptyMarkdownFileError(Error):
    '''Raised when there is no content (excluding title) in a Markdown File
    '''

    def __init__(self, md_file_path):
        '''
        '''
        super().__init__()
        self.md_file_path = md_file_path

    def __str__(self):
        return self.base_message.format(filename=self.md_file_path) + ERROR_MESSAGE
