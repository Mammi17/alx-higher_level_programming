#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    gital = -1 * (- number % 10)
else:
    gital = number % 10
if gital > 5:
    print(f"Last digit of {number:d} is {gital:d} and is greater than 5")
elif gital == 0:
    print(f"Last digit of {number:d} is {gital:d} and is 0")
elif gital < 6 and gital != 0:
    print(f"Last digit of {number:d} is {gital:d}", end="")
    print(" and is less than 6 and not 0")
