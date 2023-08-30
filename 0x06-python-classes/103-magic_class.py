#!/usr/bin/python3

import math

"""This module defines a class MagicClass"""


class MagicClass:
    """The MagicClass class represents the bytecode of a function"""

    def __init__(self, radius=0):
        """The __init__ method is called each time a MagicClass
        object is created and sets radius to 0 by default

        Args:
            radius (int): radius of the class

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """The area method computes and returns the area of a MagicClass
        object

        Returns:
            The area of the MagicClass object

        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """The circumference method computes and returns the circumference
        of a MagicClass object

        Returns:
            The circumference of a MagicClass object

        """
        return 2 * math.pi * self.__radius
