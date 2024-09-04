#!/usr/bin/python3
i = 1
while i <= 100:
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz', end=' ')
    elif i % 5 == 0:
        print('Buzz', end=' ')
    elif i % 3 == 0:
        print('Fizz', end=' ')
    else:
        print(f'{i}', end=' ')
    i += 1
print()
