#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    final_digit = number % -10
else:
    final_digit = number % 10
if final_digit > 5:
    print(f"Last digit of {number} is {final_digit} and is greater than 5")
elif final_digit == 0:
    print(f"Last digit of {number} is {final_digit} and is 0")
else:
    print(f"Last digit of {number} is {final_digit} and is less than 6 and not 0")
