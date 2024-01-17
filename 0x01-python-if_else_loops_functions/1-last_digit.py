#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    final_d = number % -10
else:
    final_d = number % 10
if final_d > 5:
    print(f"Last digit of {number} is {final_d} and is greater than 5")
elif final_d == 0:
    print(f"Last digit of {number} is {final_d} and is 0")
else:
    print(f"Last digit of {number} is {final_d} and is less than 6 and not 0")
