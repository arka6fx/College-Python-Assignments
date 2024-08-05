"""A3-03.write a program to compute the lcm of two positive integers."""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


or_num1 = num1
or_num2 = num2


if num1 < num2:
    num1, num2 = num2, num1


while num2 != 0:
    num1, num2 = num2, num1 % num2 
    pass
    if num2 == 0:
        break
    if num1 % 2 != 0:
        continue

hcf = num1

lcm = (or_num1 * or_num2) / hcf
print(f"The LCM is {lcm}.")
