#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
	gital = -1 * (- number % 10)
else:
	gital = number % 10
if gital > 5:
	print(f"Last digit of {:d} is {:d} and is greater than 5", gital)
elif gital == 0:
	print(f"Last digit of {:d} is {:d} and is equal to 0", gital)
elif gital < 6 and gital != 0:
	print(f"Last digit of {:d} is {:d}", gital, end= " ")
	print("and is not equal to zero.")
