#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max: int = 0
    for value in my_list:
        if value > max:
            max = value
    return max
