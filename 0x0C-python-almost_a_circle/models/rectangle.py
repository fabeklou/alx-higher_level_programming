#!/usr/bin/python3

"""This module defines the structure for rectangle objects"""

from base import Base


class Rectangle(Base):
    """Rectangle: is a class that defines a rectangle object
    structure and inherits from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor of new rectangle objects
        
        Args:
            width (int):
                width of the rectangle
            height (int):
                height of the rectangle
            x (int):
                x position of the rectangle
            y (int):
                y position of the rectangle

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = x

    @property
    def width(self):
        """The width property can be used to set/get the value
        of the width private instance attribute safely
        
        Args:
            value (int):
                width of the rectangle object
        
        Returns:
            (int):
                the width of the rectangle object

        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """The height property can be used to set/get the value
        of the height private instance attribute safely
        
        Args:
            value (int):
                height of the rectangle object
        
        Returns:
            (int):
                the height of the rectangle object

        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """The x property can be used to set/get the value
        of the x private instance attribute safely
        
        Args:
            value (int):
                x position of the rectangle object
        
        Returns:
            (int):
                the x position of the rectangle object

        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """The y property can be used to set/get the value
        of the y private instance attribute safely
        
        Args:
            value (int):
                y position of the rectangle object
        
        Returns:
            (int):
                the y position of the rectangle object

        """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
