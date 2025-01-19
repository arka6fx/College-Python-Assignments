# A9_04.  Write a program to print random numbers infinitely.
# Raise the Stop Iteration exception after displaying 10 numbers to exit from the program.

import random

count = 0

try:
    while True:
        number = random.randint(1, 100)  # Random number between 1 and 100
        print(number)
        count += 1
        if count >= 10:
            raise StopIteration("Displayed 10 numbers, stopping the program.")

except StopIteration as e:
    print(e)
