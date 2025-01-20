# A9_03.  Write a program to read a number from the user and print its square. 
# Generate KeyboardInterrupt exception if Ctrl + C is pressed instead of a number.


try:
    number = float(input("Enter a number: "))
    
    square = number ** 2
    
    print(f"The square of {number} is {square}")


except KeyboardInterrupt:
    print("\nError: You pressed Ctrl + C. Program interrupted.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
