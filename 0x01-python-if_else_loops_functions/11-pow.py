#!/usr/bin/python3
def pow(a, b):
    result: int = 1
    if b > 0:
        while b > 0:
            b -= 1
            result *= a
    elif b < 0:
        while b < 0:
            b += 1
            result /= a
    return result
