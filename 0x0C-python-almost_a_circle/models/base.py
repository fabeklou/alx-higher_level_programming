#!/usr/bin/python3

"""This module defines a Base class used to manage the
id attribute across multiple other classes
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list[dict]):
                list of dictionnaries to serialize

        Returns:
            (json str): json string representation of the given list object

        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a json string representation of a list object to a file

        Args:
            list_objs (list[obj]):
                list of ojects, instances of the Rectangle or Square class

        """
        if hasattr(cls, "size"):
            f_name = "Square.json"
        else:
            f_name = "Rectangle.json"

        dict_list: list = []
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())

        with open(f_name, "w") as fo:
            fo.write(cls.to_json_string(dict_list))
