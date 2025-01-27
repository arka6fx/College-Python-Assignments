"""A3-03.write a program to compute the lcm of two positive integers."""
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
  
    
max_num = num1 if num1>num2 else num2
    
 
for i in range(max_num,(num1*num2)+1,max_num):
    if i%num1==0 and i%num2==0:
        lcm=i
        print("LCM is : ",lcm)
        break  
    
        





    