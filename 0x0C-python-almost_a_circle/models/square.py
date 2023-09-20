#!/usr/bin/python3

"""This module defines a Square object, which
inherit from the Rectangle class and is used to work
with square objects
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class defines a structre fo square objects"""

    def __init__(self, size, x=0, y=0, id=None):
        """is called at instanciation of a new square object

        Args:
            size (int):
                size of the square
            x (int):
                x position of the square
            y (int):
                y position of the square
            id (int):
                identifier of the square

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns a printable verison of a square object
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """The size property is based on the width and height
        properties of a rectangle object and can be used to set/get
        he value of the size private instance attribute safely

        Args:
            value (int):
                size of the square object

        Returns:
            (int):
                the size of the square object

        Raises:
            TypeError:
                if size is not an integer
            ValueError:
                if size is <= 0

        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update is a variadic method. All arguments
        passed to it are packed into a tuple/dict before it called.
        We iterate over the tuple/dict to get the individual values
        and update the rectangle object occordingly

        Args:
            args (:list: :int):
                list of values of attributs to update from id to height
            kwargs (dict):
                list of key-word arguments

        """
        if args:
            attrs: list = ["id", "size", "x", "y"]
            for idx, value in enumerate(args):
                setattr(self, attrs[idx], value)
            return
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def to_dictionary(self):
        """returns the dict representation of a square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
