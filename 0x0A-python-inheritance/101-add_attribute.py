#!/usr/bin/python3

"""This module defines a function that adds a new
attributes to an object if it's possible
"""


def add_attribute(obj, attr: str, value):
    """
    Adds a new attribute to an object if it is possbile

    Args:
        obj (any):
            object that the attribute should be added to
        attr (str):
            identifier of the attribute that should be added
        value (any):
            value that the attribute should points to

    Raises:
        TypeError: if the attribute can not be added to the
            object

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
