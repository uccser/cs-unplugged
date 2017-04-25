"""Custom error for missing required field."""

from .Error import Error

ERROR_MESSAGE_TEMPLATE = """
A {model} requires the following fields:
{fields}
One or more of these fields are missing.
  - Are all the field names spelt correctly?
  - Do all fields have values?
"""


class MissingRequiredFieldError(Error):
    """Custom error for missing required field."""

    def __init__(self, config_file_path, required_fields, model):
        """Create error for missing required field."""
        super().__init__()
        self.config_file_path = config_file_path
        self.required_fields = required_fields
        self.model = model

    def __str__(self):
        """
        Override default error string.

        Return:
          Error message for missing required field.
        """
        fields = ""
        for field in self.required_fields:
            fields += "  - {field}\n".format(field=str(field))
        missing_field_message = ERROR_MESSAGE_TEMPLATE.format(
            model=self.model,
            fields=fields
        )
        return self.base_message.format(filename=self.config_file_path) + missing_field_message
