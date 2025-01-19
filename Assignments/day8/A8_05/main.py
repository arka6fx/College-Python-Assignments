# A8_05. Write a program to shuffle elements of a list of random numbers between given ranges.

import random


low = int(input("Enter the lower limit of the range: "))
high = int(input("Enter the upper limit of the range: "))
n = int(input("Enter the number of random numbers to generate: "))
        
random_numbers = [random.randint(low, high) for _ in range(n)]
print("Unshuffled numbers: ", random_numbers)

random.shuffle(random_numbers)
print(f"Shuffled numbers: {random_numbers}")
