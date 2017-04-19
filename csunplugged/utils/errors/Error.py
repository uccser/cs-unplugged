class Error(Exception):
    '''Base class for Errors.
    (Exceptions from external sources such as inputs).
    '''
    def __init__(self):
        self.base_message = '\n' + \
            '\n****************************ERROR****************************' + \
            '\nFile: {}'
            
        self.reference_message = '\nReferenced in: {}'

        self.missing_file_suggestions = '' + \
            '\n  - Did you spell the name of the file correctly?' + \
            '\n  - Does the file exist?' + \
            '\n  - Is the file saved in the correct directory?'
