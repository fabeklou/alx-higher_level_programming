#!/usr/bin/python3

"""
This module defines the structure for rectangle objects
"""

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
        self.y = y

    def __str__(self):
        """
        returns a printable verison of a rectangle object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

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

        Raises:
            TypeError:
                if width is not an integer
            ValueError:
                if width is <= 0

        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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

        Raises:
            TypeError:
                if height is not an integer
            ValueError:
                if height is <= 0

        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
        print("inited !")

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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area value of a reactangle object
        """
        return self.width * self.height

    def display(self):
        """
        Prints a rectangle object using '#' characters
        """
        print("{}".format((self.y * '\n') + ((self.x * ' ') +
                          ('#' * self.width) + '\n') * self.height), end="")

    def update(self, *args):
        """update is a variadic method. All arguments
        passed to it are packed in the tuple before it called.
        We iterate over the tuple to get the individual values
        and update the rectangle object occordingly

        Args:
            args (:list: :int):
                list of values of attributs to update from id to heigt

        """
        attrs: list = ["id", "x", "y", "width", "height"]
        for idx, value in enumerate(args):
            setattr(self, attrs[idx], value)
