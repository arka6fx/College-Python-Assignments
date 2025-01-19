# 2/12/24 A9_01. Write a program to read a number from the user. 
# If the number is positive or zero, print it, otherwise raise an exception.


try:
    number = float(input("Enter a number: "))
    
    if number < 0:
        raise ValueError("The number is negative. Please enter a positive number or zero.")
    
    print(f"The entered number is: {number}")

except ValueError as e:
    print(f"Error: {e}")
