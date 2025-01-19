a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while b != 0:
    a, b = b, a % b

print(f"The GCD of the given numbers is {a}")
 

# def gcd(a,b):
#     if(a%b==0):
#         return b
#     else:
#         return gcd(b,a%b)