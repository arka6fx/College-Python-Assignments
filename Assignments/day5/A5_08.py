#A5_08. write a program to add elements in a tuple without using built-in functions.

myTuple= ()

n = int(input("Enter the number of elements: "))

myTuple = tuple(int(input(f'Enter element no. {i + 1}: ')) for i in range(n))

sum = 0
for i in myTuple:
    sum+=i
      
print("sum =",sum)







