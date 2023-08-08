#!/usr/bin/python3
import random
number = random.randint(-10, 10)
result: str = ""
if number < 0:
    result = str(number) + " is negative"
elif number == 0:
    result = str(number) + " is zero"
else:
    result = str(number) + " is positive"
print(result)
