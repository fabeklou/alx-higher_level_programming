#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, el in enumerate(row):
            print("{:d}".format(el), end=("" if len(row) - 1 == idx else " "))
        print()
