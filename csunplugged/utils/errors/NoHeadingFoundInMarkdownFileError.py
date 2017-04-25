from .Error import Error

ERROR_MESSAGE = "\nThe file does not contain a heading.\n"


class NoHeadingFoundInMarkdownFileError(Error):
    '''Raised when a title cannot be found in a Markdown File
    '''

    def __init__(self, md_file_path):
        super().__init__()
        self.md_file_path = md_file_path

    def __str__(self):
        return self.base_message.format(filename=self.md_file_path) + ERROR_MESSAGE
