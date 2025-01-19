# A8_02. Create a module to check whether a number is a prime or not. 
# Write a program to find the prime number between two limits using this module.

import prime

low = int(input("Enter the lower limit: "))
high = int(input("Enter the upper limit: "))


print(f"Prime numbers between {low} and {high} are:")
for num in range(low, high + 1):
    if prime.is_prime(num):
        print(num, end=" ")
