#!/usr/bin/python3
for l_digit in range(0, 9):
    for r_digit in range(0, 10):
        if r_digit > l_digit:
            print("{}{}".format(l_digit, r_digit),
                  end=("\n" if l_digit == 8 and r_digit == 9 else ", "))
