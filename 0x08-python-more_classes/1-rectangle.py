#!/usr/bin/python3

"""This module defines a Rectangle class"""


class Rectangle:
    """Defines basic structure for a Rectangle object

    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """width is a property and can be used to get or set
        the value of the width private instance attribute

        getter:
            the getter is used to get the value of private
            instance attribute __width
            Returns:
                the value of __width in the object

        setter:
            the setter is use to set or to reset the value of
            the private instance attribute __width
            Returns:
                nothing
            Raises:
                TypeError: if width is not an integer
                ValueError: if width is negative

        """
        return self.__width

    @property
    def height(self) -> int:
        """height is a property and can be used to get or set
        the value of the width private instance attribute

        getter:
            the getter is used to get the value of private
            instance attribute __height
            Returns:
                the value of __height in the object

        setter:
            the setter is use to set or to reset the value of
            the private instance attribute __height
            Returns:
                nothing
            Raises:
                TypeError: if height is not an integer
                ValueError: if height is negative
        """
        return self.__height

    @width.setter
    def width(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value


if __name__ == "__main__":

    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
