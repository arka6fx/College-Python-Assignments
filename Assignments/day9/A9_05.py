# A9_05.  Write a program to generate a random number. 
# Raise a user-defined exception if the number is below 0.5.

import random


try:
    number = random.random()  # Generates a random float between 0 and 1
    print(f"Generated number: {number}")
    
    if number < 0.5:
        raise Exception("The generated number is below 0.5.")
    
except Exception as e:
    print(f"Error: {e}")
