"""Module for retrieving a GET request query parameter."""

from django.http import Http404


def retrieve_query_parameter(request, parameter, valid_options=None):
    """Retrieve the query parameter.

    If the parameter cannot be found, or is not found in the list of
    valid options, then a 404 error is raised.

    Args:
        request: Request object (Request).
        parameter: Parameter to retrieve (str).
        valid_options: If provided, a list of valid options (list of str).

    Returns:
        String value of parameter.
    """
    value = request.get(parameter, None)
    if value is None:
        raise Http404("{} parameter not specified.".format(parameter))
    if valid_options and value not in valid_options:
        raise Http404("{} parameter not valid.".format(parameter))
    return value


def retrieve_query_parameter_list(request, parameter, valid_options=None):
    """Retrieve the query parameter list.

    If the parameter cannot be found, or is not found in the list of
    valid options, then a 404 error is raised.

    Args:
        request: Request object (Request).
        parameter: Parameter to retrieve (str).
        valid_options: If provided, a list of valid options (list of str).

    Returns:
        List of strings of values of parameter.
    """
    values = request.getlist(parameter, None)
    if values is None:
        raise Http404("{} parameter not specified.".format(parameter))
    if valid_options:
        for value in values:
            if value not in valid_options:
                raise Http404("{} parameter not valid.".format(parameter))
    return values
