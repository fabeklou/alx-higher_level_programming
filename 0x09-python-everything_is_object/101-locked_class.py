#!/usr/bin/python3

"""This module defines a LockedClass which is protected"""


class LockedClass:
    """This class creates a frozen object that can only
    accept one attribute

    src:
        https://stackoverflow.com/questions/3603502/

    """
    __slots__ = ["first_name"]

    """Can only add and update an instance attribute
    named `first_name`

    """
