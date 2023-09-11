#!/usr/bin/python3

"""This module defines a MyInt class"""


class MyInt(int):
    """MyInt class: defines a class which  inherits
    from the built-in int class and inverts `==` and `!=`
    comparaison operator

    """
    def __eq__(self, other):
        """Changes the default behavior of the
        __eq__ magic method

        """
        return self.real != other

    def __ne__(self, other):
        """Changes the default behavior of the
        __ne__ magic method

        """
        return self.real == other


my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
