#!/usr/bin/python3

"""This module defines a MyList class which is a
subclass of the built-in list class
"""


class MyList(list):
    """MyList is an extension of the built-in
    list class

    """
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print("{}".format(sorted(self)))
