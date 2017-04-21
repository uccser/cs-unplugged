from .Error import Error

class KeyNotFoundError(Error):
    '''Raised when configuration file specifies a key that does not exist.
    '''
    
    def __init__(self, config_file_path, key, field):
    	super().__init__()
    	self.config_file_path = config_file_path
    	self.key = key
    	self.field = field

    def __str__(self):
    	key_not_found_message = '\nKey: {}'.format(self.key) + \
    		'\n"{}" did not match any {}.'.format(self.key, self.field) + \
    	    '\n  - Did you spell the name of the key correctly?' + \
            '\n  - Does the key exist?'
    	return self.base_message.format(self.config_file_path) + \
    	    key_not_found_message
