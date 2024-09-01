"""A3-02.Write a program to check whether a given number is an Armstrong number or not."""

#1^3+5^3 +3^3 =1+125+27=153
num = int(input("Enter a number: "))

original_num = num

count = 0
temp_num = num
while temp_num != 0:
    temp_num //= 10
    count += 1

result = 0
temp_num = num
while temp_num != 0:
    digit = temp_num % 10
    result += digit ** count
    temp_num //= 10
    if result > original_num:
        break

if result == original_num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
