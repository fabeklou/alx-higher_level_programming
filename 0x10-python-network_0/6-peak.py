#!/usr/bin/python3

"""This module defines a function that finds the peak
in a list of unsorted integers
"""


def find_peak(list_int):
    """find_peak - finds and retruns the peak
    in a list of unsorted integers

    Args:
        list_of_integers (List[int]): an unsorted list of integer

    Returns:
        (int): the peak or None if the list is empty

    """
    peak = None

    for i in range(1, len(list_int) - 1):
        if list_int[i] > list_int[i - 1] and list_int[i] > list_int[i + 1]:
            peak = list_int[i]
    return peak
