#!/usr/bin/python3

"""This module defines a function that multiplies 2 matrices
and returns the result as a new matrix product using numpy
module

exemple:

>>> import numpy
>>> m1 = [[1, 2]]
>>> m2 = [[3, 4], [5, 6]]
>>> lazy_matrix_mul(m1, m2)
[[13 16]]

"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """This function multiples two matrices and
    returns a new matrixproduct using numpy

    Args:
        m_a (:list: list)
            a list of lists of integers
        m_b (:list: list)
            a lus of lists of integers

    Returns:
        :list: list: a new matrix product

    """
    return numpy.matmul(m_a, m_b)
