# 25/11/24  A7_01. Write a program to find GCD and LCM of two numbers by 
# defining a function to compute GCD and LCM.

def gcd(a, b):
    """Computes the greatest common divisor (GCD) of two integers a and b."""
    while(b!=0):
        a, b = b, a % b  
    return a

def lcm(a, b):
    """Computes the least common multiple (LCM) of two integers a and b."""
    return (a * b) // gcd(a, b) 

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


# Print the results
print(f"The GCD of {num1} and {num2} is: ",gcd(num1, num2))
print(f"The LCM of {num1} and {num2} is: ",lcm(num1, num2))