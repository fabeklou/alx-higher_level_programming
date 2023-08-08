#!/usr/bin/python3
for num in range(0, 100):
    if (num < 10):
        print("0", end="")
    print("{:d}".format(num), end=(", " if num < 99 else "\n"))
