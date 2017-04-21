from .Error import Error

class MissingRequiredFieldError(Error):
    '''Raised when a required field is missing from a yaml file
    '''
    
    def __init__(self, config_file_path, required_fields, model):
    	super().__init__()
    	self.config_file_path = config_file_path
    	self.required_fields = required_fields
    	self.model = model

    def __str__(self):
    	fields = ''
    	for field in self.required_fields:
    		fields += '\n  - {}'.format(str(field))
    	missing_field_message = '' + \
    	    '\nA {} requires the following fields:'.format(self.model) + \
    	    fields + \
    	    '\nOne or more of these fields are missing.' + \
    	    '\n  - Are all the field names spelt correctly?' + \
    	    '\n  - Do all fields have values?'  	    
    	return self.base_message.format(self.config_file_path) + \
    	    missing_field_message
