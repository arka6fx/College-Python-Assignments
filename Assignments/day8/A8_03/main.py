# A8_03. Create a module to find the factorial of a number and import the module from the main program
# to find the factorial of a given number.

from factorial import fact

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {fact(num)}")

