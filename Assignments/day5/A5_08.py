#A5_08. write a program to add elements in a tuple without using built-in functions.

myTuple= ()

n = int(input("Enter the number of elements: "))

for i in range(n):
   
    element = int(input(f'Enter element no. {i + 1}: '))
    myTuple += (element,)

sum = 0
for i in myTuple:
    sum+=i
      
print("sum =",sum)







