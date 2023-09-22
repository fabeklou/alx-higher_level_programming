#!/usr/bin/python3

"""This module defines a Base class used to manage the
id attribute across multiple other classes
"""

import json
import csv
import turtle


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
        f_name: str = cls.__name__ + ".json"

        dict_list: list = []
        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())

        with open(f_name, "w") as fo:
            fo.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list object from a json string representation

        Args:
            json_string (json str):
                json string represention of an object

        Returns:
            (list[obj]):
                list of python object

        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        (Alternative constructor)

        Args:
            dictionary (dict):
                collection of key-value paires representing the attributes
                and their values

        Returns:
            (obj): a new Rectangle or Square object

        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of Square/Rectangle objects loads from
        a file and desirialize
        """
        f_name: str = cls.__name__ + ".json"

        try:
            with open(f_name) as fo:
                list_dct = cls.from_json_string(fo.read())
                list_instance = [cls.create(**dct) for dct in list_dct]
                return list_instance
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects and save it to a csv file

        Args:
            list_objs (list[obj]):
                list of Rectangle/Square objects

        """
        f_name: str = cls.__name__ + ".csv"

        with open(f_name, "w") as fo:

            if cls.__name__ == "Rectangle":
                field_names: list[str] = ["id", "width", "height", "x", "y"]
            else:
                field_names: list[str] = ["id", "size", "x", "y"]

            csv_writer = csv.DictWriter(fo, fieldnames=field_names)

            if list_objs:
                list_dct = [obj.to_dictionary() for obj in list_objs]
            else:
                list_dct = []

            csv_writer.writeheader()
            csv_writer.writerows(list_dct)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize the content of a csv file and returns a list
        of dictionary object

        """
        f_name: str = cls.__name__ + ".csv"
        try:
            with open(f_name) as fo:

                csv_reader = csv.DictReader(fo)

                list_csv_dct: list = [dct for dct in csv_reader]

                list_dct: list = []
                for dct in list_csv_dct:
                    tmp_dct = {}
                    for key, value in dct.items():
                        tmp_dct.update({key: int(value)})
                    list_dct.append(tmp_dct)
                return [cls.create(**dct) for dct in list_dct]
        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and daws all Rectangles and Squares

        Args:
            list_rectangles (list[obj]):
                is a list of Rectangle objects
            list_squares (list[obj]):
                is a list of Square objects

        useful article:
            https://www.geeksforgeeks.org/turtle-programming-python/

        """
        turtle.title("Drawing : Rectangles and Squares")
        turtle.bgcolor("#001419")
        turtle.hideturtle()
        turtle.pensize(2)

        for rectangle in list_rectangles:
            turtle.color("#53FF45")
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)

        for square in list_squares:
            turtle.color("#F5B841")
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.exitonclick()
