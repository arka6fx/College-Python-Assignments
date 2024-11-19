#A5_09. write a program to calculate the mean of elements in a tuple of integers.

myTupple= ()
n = int(input("Enter the number of elements: "))

myTuple = tuple(int(input(f'Enter element no. {i + 1}: ')) for i in range(n))

sum = 0
count = 0
for i in myTupple:
    sum+=i
    count+=1
      
print("Mean =",sum/count)







