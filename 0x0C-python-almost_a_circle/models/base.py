#!/usr/bin/python3

"""This module defines a Base class used to manage the
id attribute across multiple other classes
"""


class Base:
    """Base class: defines a structure for Base objects.
    Parent class for all the classes in this project, used
    for avoiding duplaction and manage the id attribute

    Args:
        __nb_objects (int):
            nomber of Base objects created without initial id

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of the Base class used to create a new Base object
        with id = the given value if the the actual value is != None. Otherwise
        id = __nb_objects + 1

        Args:
            id (int):
                identifier of rhe user of type integer

        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            return
        self.id = id
