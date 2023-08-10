#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    a: int = 1
    b: int = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
