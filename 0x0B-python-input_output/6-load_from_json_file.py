#!/usr/bin/python3

"""This module defines a function that open a text file
reads the content deserialize it and returns it as a
python object
"""

import json


def load_from_json_file(filename):
    """load_from_json_file: open a text file reads the content
    then deserialize it and returns it as a python object

    Args:
        filename (str):
            path to the file to read from

    Returns:
        (any): the deserialize object (python object)
    """
    with open(filename, encoding="utf-8") as fo:
        return json.loads(fo.read())
