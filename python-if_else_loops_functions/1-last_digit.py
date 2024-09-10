#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
o_v = last_digit

if number < 0:
    o_v *= -1
if o_v > 5:
    print(f"Last digit of {number} is {o_v} and is greater than 5")
elif o_v == 0:
    print(f"Last digit of {number} is {o_v} and is 0")
else:
    print(f"Last digit of {number} is {o_v} and is less than 6 and not 0")
