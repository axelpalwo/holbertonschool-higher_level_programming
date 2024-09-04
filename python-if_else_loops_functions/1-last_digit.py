#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10
if number < 0:
    last_digit *= -1
if last_digit > 5:
    print(f'Last digit of {number} is {lastd} and is greater than 5')
elif last_digit < 0:
    print(f'Last digit of {number} is {lastd} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {lastd} and is 0')
