#!/usr/bin/python3

"""This module defines a function that serialize
a python object and save it to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file: open the target file, save the
    serialize object into it and close it back

    Args:
        my_obj (any):
            the object to be serialized and saved
        filename (str):
            a path to the file

    """
    with open(filename, "w", encoding="utf-8") as fo:
        fo.write(json.dumps(my_obj))
