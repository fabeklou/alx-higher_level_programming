#!/usr/bin/python3

import json

"""This module defines a function `to_json_string` that
can generate a JSON (Javascript Object Notation)
representation of any kind of object
"""


def to_json_string(my_obj):
    """to_json_string: generates the json representation
    of a given object

    Args:
        my_obj (any): is the object to be serialized

    Returns:
        (str): json representation of the given object if
            the serialization is possible

    """
    return json.dumps(my_obj)
