#!/usr/bin/python3

"""This module defines a function `from_json_string` that
can convert a JSON (Javascript Object Notation) string
to an object (Python data structure)
"""

import json


def from_json_string(my_str):
    """from_json_string: generates a python object from
    a json string

    Args:
        my_str (any): is the json string to be deserialized

    Returns:
        (obj): python data structre representation of the given
            json string if the deserialization is possible

    """
    return json.loads(my_str)
