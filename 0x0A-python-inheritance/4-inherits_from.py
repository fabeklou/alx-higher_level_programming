#!/usr/bin/python3

"""This module defines a function that tells if
an object is instance of the sub_class of a class or not
"""


def inherits_from(obj, a_class):
    """Returns `True` if obj is an instance of the sub_class
    of a_class `False` otherwise

    Args:
        obj (Any): is an object
        a_class (Any): is a class

    Returns:
        bool: True if obj is an instance of
            the sub_class of a_class otherwise False

    """
    return False if type(obj) == a_class else issubclass(type(obj), a_class)
