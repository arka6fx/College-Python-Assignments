# 25/11/24  A7_01. Write a program to find GCD and LCM of two numbers by 
# defining a function to compute GCD and LCM.

def gcd(a, b):
    while(b!=0):
        a, b = b, a % b  
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b) 


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The GCD of {num1} and {num2} is: ",gcd(num1, num2))
print(f"The LCM of {num1} and {num2} is: ",lcm(num1, num2))