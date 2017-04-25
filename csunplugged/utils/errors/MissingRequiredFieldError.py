from .Error import Error

ERROR_MESSAGE_TEMPLATE = """
A {model} requires the following fields:
{fields}

One or more of these fields are missing.
  - Are all the field names spelt correctly?
  - Do all fields have values?
"""


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
            fields += '  - {field}\n'.format(field=str(field))
        missing_field_message = ERROR_MESSAGE_TEMPLATE.format(
            model=self.model,
            fields=fields
        )
        return self.base_message.format(filename=self.config_file_path) + missing_field_message
