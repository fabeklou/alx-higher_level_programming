#!/usr/bin/python3

"""This module defines a function that returns
the list of available attributes and methods of an object
"""


def lookup(obj):
    """Uses the dir() function to return a list of attributes
    and methods available in the given object

    """
    return dir(obj)
