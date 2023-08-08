#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

message: str = ""
last_digit: int = 0

if number < 0:
    last_digit = ((number * -1) % 10) * -1
else:
    last_digit = number % 10

if last_digit == 0:
    message = "and is 0"
elif last_digit > 5:
    message = "and is greater than 5"
else:
    message = "and is less than 6 and not 0"

print(F"Last digit of {number} is {last_digit} {message}")
