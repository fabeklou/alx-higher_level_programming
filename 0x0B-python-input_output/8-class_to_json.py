#!/usr/bin/python3

"""This modulde defines a function that produice the dict
description of an object
"""


def class_to_json(obj):
    """class_to_json: returns he dictionary description with
    simple data structure

    Args:
        obj (any):
            a serializable object

    """
    return obj.__dict__
