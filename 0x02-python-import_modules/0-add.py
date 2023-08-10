#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add
    a: int = 1
    b: int = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
