# A8_06. Write a program to create a list of random numbers using list comprehension.

import random

low = int(input("Enter the lower limit of the range: "))
high = int(input("Enter the upper limit of the range: "))
n = int(input("Enter the number of random numbers to generate: "))

random_numbers = [random.randint(low, high) for _ in range(n)]

print(f"Generated list of random numbers: {random_numbers}")
