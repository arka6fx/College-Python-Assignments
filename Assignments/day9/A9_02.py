# A9_02.   Write a program to read two numbers from the user and perform basic mathematical operations 
# (addition, multiplication, subtraction, division) by handling all possible exceptions.


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    division = num1 / num2
    
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")


except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
