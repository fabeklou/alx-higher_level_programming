#!/usr/bin/python3

"""This module defines a function that tells if
an object is direct or indirect instance of a class or not
"""


def is_kind_of_class(obj, a_class):
    """Returns `True` if obj is a direct or indirect
    instance of a_class `False` otherwise

    Args:
        obj (Any): is an object
        a_class (Any): is a class

    Returns:
        bool: True if obj is an instance of a_class
            False otherwise

    """
    return isinstance(obj, a_class)
