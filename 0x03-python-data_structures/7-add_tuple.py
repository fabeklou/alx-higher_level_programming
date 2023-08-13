#!/usr/bin/python3
def set_tuple_memb(tuple_x=()):
    if len(tuple_x) == 0:
        int0, int1 = 0, 0
    elif len(tuple_x) == 1:
        int0, int1 = tuple_x[0], 0
    else:
        int0, int1 = tuple_x[0], tuple_x[1]
    return (int0, int1)


def add_tuple(tuple_a=(), tuple_b=()):
    a, b = set_tuple_memb(tuple_a)
    x, y = set_tuple_memb(tuple_b)
    return (a + x, b + y)
