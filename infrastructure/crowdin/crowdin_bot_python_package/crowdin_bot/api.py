"""Module for interacting with the crowdin API."""

import lxml.etree
import json
import os
import requests

API_KEY = os.environ["CROWDIN_API_KEY"]
API_URL = "https://api.crowdin.com/api/project/cs-unplugged/{method}"


def api_call_text(method, **params):
    """Call a given api method and return text content.

    Returns:
        Text content of the response (str).
    """
    params["key"] = API_KEY
    response = requests.get(
        API_URL.format(method=method),
        params=params
    )
    return response.text


def api_call_xml(method, **params):
    """Call a given api method and return XML tree."""
    response_text = api_call_text(method, **params)
    xml = lxml.etree.fromstring(response_text.encode())
    return xml

def api_call_json(method, **params):
    """Call a given api method and return JSON dictionary."""
    response_text = api_call_text(method, json=True, **params)
    return json.loads(response_text)
