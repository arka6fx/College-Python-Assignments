#A5_08. write a program to add elements in a tuple without using built-in functions.

myTupple= ()

n = int(input("Enter the number of elements: "))

for i in range(n):
   
    element = int(input(f'Enter element no. {i + 1}: '))
    myTupple += (element,)

sum = 0
for i in myTupple:
    sum+=i
      
print("sum =",sum)







