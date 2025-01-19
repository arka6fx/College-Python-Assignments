# A8_04. Write a program to find the mean, median, and standard deviation 
# of a list of random numbers between 1 and 10.


import random
import statistics


n = int(input("Enter the number of random numbers to generate: "))
random_numbers = [random.randint(1, 10) for _ in range(n)]


mean = statistics.mean(random_numbers)
median = statistics.median(random_numbers)
std_dev = statistics.stdev(random_numbers)


print(f"Generated numbers: {random_numbers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
