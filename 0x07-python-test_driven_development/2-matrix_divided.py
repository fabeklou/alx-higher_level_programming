#!/usr/bin/python3

"""This module defines a function that devides elements
of a matrix and return a new matrix

Example:
>>> matrix = [[1, 2, 3], [7, 8, 9]]
>>> new_matrix = matrix_divided(matrix, 2)
>>> new_matrix
[[0.5, 1.0, 1.5], [3.5, 4.0, 4.5]]

"""


def matrix_divided(matrix: list, div: int = 1) -> list:
    """This function divides all the elements of a matrix

        Args:
            matrix (:list: list): is a list of lists (2D list) of integers 
                or floats
            div (int): is a non null (!= 0) integer or floating point number
                to divide the matrix elements with

        Returns:
            matrix: a list of lists of floats rounded to 2 decimal places

        Raises:
            TypeError: if matrix is not a list of lists of integers or floats
            TypeError: if the rows in the matrix do not have the same size
            TypeError: if `div` is not an integer or a float
            ZeroDivisionError: if the value of `div` is Zero (0)

    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for element in matrix:
        if not isinstance(element, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if not bool(element):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for value in element:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    even_cols = set([len(element) for element in matrix])

    if len(even_cols) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Using list comprehension to generate a new matrix, made of
    # individual element of the list divided by `div`
    return [[round(value/div, 2) for value in element] for element in matrix]


if __name__ == "__main__":
    matrix_divided = __import__('2-matrix_divided').matrix_divided

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
