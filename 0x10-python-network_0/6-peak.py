#!/usr/bin/python3

"""This module defines a function that finds the peak
in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """find_peak - finds and retruns the peak
    in a list of unsorted integers

    Args:
        list_of_integers (List[int]): an unsorted list of integer

    Returns:
        (int): the peak or None if the list is empty

    """
    peak = None
    l = list_of_integers  # aliasing

    for i in range(1, len(l) - 1):
        if l[i] > l[i - 1] and l[i] > l[i + 1]:
            peak = l[i]
    return peak
