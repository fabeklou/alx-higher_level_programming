#!/usr/bin/python3

"""
This module contains an addition function (add_integer)
the function adds two integers together and retruns the result.

Example:
>>> add_integer(2)
100
>>> add_integer(-10, 20)
10

"""


def add_integer(a: int, b: int = 98) -> int:
    """
    This function add two numbers a and b together and
    return the result

    Args:
        a (int): is a mandatory argument of type integer or a float
            to be casted.
        b (int): is an optional argument of type integer or a float
            to be casted and is set to 98 by default.

    Returns:
        int: representing the result of `a` + `b`

    Raises:
        TypeError: if one or both arguments are not integer or float

    """
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
        a = int(a)
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
        b = int(b)
    return a + b
