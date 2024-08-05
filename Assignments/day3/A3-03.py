"""A3-03.write a program to compute the lcm of two positive integers."""
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

if num1<=0 or num2<=0:
    print("LCM is not defined for negative numbers")
    pass  
else:    
    if num1>num2:
       max_num=num1
    else:
       max_num=num2
    
    lcm=max_num
 
    while True:
        
        if lcm%num1==0 and lcm%num2==0:
            print("LCM is : ",lcm)
            break  
        else:
            lcm+=max_num
            continue 


# Alternate approach         
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# or_num1 = num1
# or_num2 = num2


# if num1 < num2:
#     num1, num2 = num2, num1


# while num2 != 0:
#     num1, num2 = num2, num1 % num2 
#     pass
#     if num2 == 0:
#         break
#     if num1 % 2 != 0:
#         continue

# hcf = num1

# lcm = (or_num1 * or_num2) / hcf
# print(f"The LCM is {lcm}.")




    