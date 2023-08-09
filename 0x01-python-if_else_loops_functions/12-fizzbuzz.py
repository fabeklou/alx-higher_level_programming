#!/usr/bin/python3
def fizzbuzz():
    for value in range(1, 101):
        if value % 15 == 0:
            result = "FizzBuzz"
        elif value % 5 == 0:
            result = "Buzz"
        elif value % 3 == 0:
            result = "Fizz"
        else:
            result = value
        print("{} ".format(result), end=("" if value != 100 else "\n"))
