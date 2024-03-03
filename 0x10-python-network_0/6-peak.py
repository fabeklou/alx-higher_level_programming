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

    # brute force approach: looping & comparison
    # time O(n) & space O(1)
    """
    peak = None
    size = len(list_int)

    if size == 0:
        return peak
    if size == 1:
        return list_int[0]
    if list_int[0] > 0 and list_int[0] >= list_int[1]:
        return list_int[0]
    if list_int[size - 1] > 0 and list_int[size - 1] >= list_int[size - 2]:
        return list_int[size - 1]

    for i in range(1, size - 1):
        if list_int[i] > list_int[i - 1] and list_int[i] > list_int[i + 1]:
            peak = list_int[i]
            return peak
    return peak
    """

    # optimized solution: Iterative Binary Search
    # time O(log n) > & space O(1)
    # O(n) time complexity because of the len() function

    peak = None
    size = len(list_int)
    left, right = 0, size - 1

    while left <= right:
        # find the middle index of the list/sub_list in which the
        #    peak number may be located
        mid = (left + right) // 2

        # if middle element is the peak, break the loop and return it
        #   do not check the left side of the mid element if his index is 0
        #   do not check the right side of the mid element if his index
        #       is size - 1
        if (mid == 0 or list_int[mid] >= list_int[mid - 1])\
                and (mid == size - 1 or list_int[mid] >= list_int[mid + 1]):
            peak = list_int[mid]
            break

        # if the element on the left side of the middle element
        #   is greater than him, the peak should be
        #   in the left half of the list
        # otherwise the peak is in the right half of the list
        if mid > 0 and list_int[mid - 1] > list_int[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return peak
